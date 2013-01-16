
// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-15

const MODULE = 'tools';

var util = require('util');
var fs = require('fs');

var debugLevel = (process.argv[2]) ? process.argv[2] : 0; // 5, 99

function isDebug(level) {
  var l = 99;
  if (level != undefined){
    l = level;
  }
  return (l <= debugLevel);
}

exports.isDebug = isDebug;

const BOLD = 1;
const DEFCOLOR = 39;
const UNBOLD = 22;
const COLOR = 30;
const RED = 1;
const BLUE = 4;
const RESET = 0;

function sgr(code) {// Select Graphic Rendition
  return '\u001b[' + code + 'm';
}

function debug(module, item, _subitem, _info, _level) {
  var info = '';
  var level = 99;
  if (isDebug(_level)) {
    
    if (typeof _info == 'number') {
      level = _info;
    } else if (_info != undefined) {
      info = ': ' + _info;
      if (typeof _level == 'number') {
        level = _level;
      }
    } 
    var subitem = ((_subitem != undefined) && (_subitem != '')) ? ',' +
      sgr(BOLD + ';' + (COLOR + RED)) + _subitem + sgr(RESET) : '';

    process.stderr.write('[' + module + ',' +
      sgr(BOLD + ';' + (COLOR + BLUE)) + item + sgr(RESET) + 
        subitem + ']' + info + '\n');
  }
}

exports.debug = debug;  // ???

var functionsX = {
  debug: 'function(item, subitem, info, level) {' +
         'tools.debug(MODULE, item, subitem, info, level); };',
  fdebug: 'function(subitem, info, level) {' +
          'var item = arguments.callee.caller.name ? ' +
          'arguments.callee.caller.name : "---";' +
          'debug(item, subitem, info, level); };'
};

var functions = {
  debug:  function(param) {
            return function (item, subitem, info, level) {
              debug(param, item, subitem, info, level);
            };
          },
  fdebug: function(param) {
            return function (subitem, info, level) {
              var item = arguments.callee.caller.name ?
                arguments.callee.caller.name : "---";
              param(item, subitem, info, level);
            };
          }
}

exports.createFunction = function(name, p1, p2, p3) {
  return functions[name](p1, p2, p3);
}

function fdebug(subitem, info, level) {
  item = arguments.callee.caller.name ? arguments.callee.caller.name : '---';
  debug(MODULE, item, subitem, info, level);
}

function inspect(o) {
  return util.inspect(o, false, 2, true);
}

exports.inspect = inspect;

String.prototype.trim = function() {
  return this.replace(/^\s+|\s+$/g,"");
}

exports.pad2 = function(n) {
  return n<10 ? '0'+n : n
}

function getTempDir() {
  return process.env.TMPDIR ? process.env.TMPDIR : '/tmp'
}

exports.getTempDir = getTempDir;

/**
 * Liefert ähnlich zu parseFloat eine Float-Zahl, die der String s repräsentiert.
 * Misslingt die Wandlung, so wird der Wert von d geliefert. Der Rückgabewert 
 * ist also in jedem Fall eine Float-Zahl.
 * @param s die Zahl als String.
 * @param {number} d default-Wert (ohne Angabe 0.0).
 * @return {number} Float-Zahl
 */
exports.getFloat = function(s, d) {
  var _d = d == undefined ? 0.0 : d;
  var x = parseFloat(s);
  return isNaN(x) ? _d : x;
}
/**
 * Liefert ähnlich zu parseInt eine Int-Zahl, die der String s repräsentiert.
 * Misslingt die Wandlung, so wird der Wert von d geliefert. Der Rückgabewert 
 * ist also in jedem Fall eine Int-Zahl.
 * @param s die Zahl als String.
 * @param {number} d default-Wert (ohne Angabe 0).
 * @return {number} Int-Zahl
 */
exports.getInt = function(s, d) {
  var _d = d == undefined ? 0 : d;
  var x = parseInt(s);
  return isNaN(x) ? _d : x;
}

/**
 * Testet, ob das übergebene Objekt leer ist.
 * @param {object} obj 
 * @return {boolean} true oder false
 */
var isEmpty = function(obj) {
  return Object.keys(obj).length === 0;
}

exports.isEmpty = isEmpty;

/**
 * Liefert ein Object target mit den definierten Umgebungsvariablen.
 * @param {object} target Ergebnis (Übergabe per Referenz!)
 * @param {function} next wird ausgeführt, wenn das Ergebnis vollständig ist.
 * @param {string | object} param1 1. Parameter für next
*/
function getEnv(target, next, param1) {
  // reicht process.env vielleicht auch aus?
  var next_args = [].slice.call(arguments, 2);
  // Argument-Array ab 3. Parameter erzeugen [param1, ..., ...]
  if (isEmpty(target)) {// Erster Aufruf?
    var spawn = require('child_process').spawn;
    var env = spawn('/usr/bin/printenv');
    var result = null;
    env.stdout.on('data', function (data) {
      result = data;
      fdebug('data', inspect(data));
      var e0, e;
      if (result) {
        e0 = result.toString().split('\n');
        for (var i in e0) {
          e = e0[i].split('=');
          target[e[0]] = e[1];
        }
      }
      fdebug('e0', inspect(e0), 102);
      fdebug('e', inspect(e), 102);
      if (!target.TMPDIR) target.TMPDIR = '/tmp'; // weil so wichtig ...
      // Weiterführende Funktion mit allen Parametern ausführen.
      next.apply(this, next_args); 
    });
  } else {
    // Umgebungsvariablen sind bereits bekannt.
    next.apply(this, next_args);
  }
}

exports.getEnv = getEnv;

/**
 * Löscht rekursiv eine Verzeichnisstruktur.
 * @see https://github.com/ryanmcgrath/wrench-js
 * @param {string} dir zu löschende Verzeichnisstruktur.
 * @param {function} clbk Aufruf bei Erfolg oder Fehler.
*/
function rmdirRecursive(dir, clbk){
  fs.readdir(dir, function(err, files){
    if (err) return clbk(err);
    (function rmFile(err){
      if (err) return clbk(err);
      var filename = files.shift();
      if (filename === null || typeof filename == 'undefined') {
        fdebug('rmdir', dir);
        return fs.rmdir(dir, clbk);
      }
      var file = dir+'/'+filename;
      fs.stat(file, function(err, stat){
        if (err) return clbk(err);
        if (stat.isDirectory()) {
          rmdirRecursive(file, rmFile);
          fdebug('rmdir', file);
        } else {
          fs.unlink(file, rmFile);
          fdebug('unlink', file);
        }
      });
    })();
  });
};

exports.rmdirRecursive = rmdirRecursive;

/**
 * Schreibt in einem temporären Verzeichnis eine Datei.
 * @param {string} dir Temporäres Verzeichnis
 * @param {string} name Name der Datei
 * @param {Buffer} content Inhalt der Datei
 * @param {function} error Aufruf im Fehlerfall
 * @param {function} success Aufruf bei Erfolg
*/
function createTempFile(dir, name, content, error, success) {

}

exports.createTempFile = createTempFile;


/**
 * Analysiert BASE64-String.
 * Test ist nicht 100%ig sicher, aber vermutlich ausreichend.
 * @param {string} b Evtl. BASE64-kodiert.
 * @return {boolean} 
*/
function isBASE64(b) {
  // Test nicht 100%ig sicher, aber vermutlich ausreichend.
  r = /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/;
  return r.test(b);
}

exports.isBASE64 = isBASE64;
