
// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'tools';

var util = require('util');

var debugLevel = (process.argv[2]) ? process.argv[2] : 0; // 5, 99

function isDebug(level) {
  var l = 99;
  if (level != undefined){
    l = level;
  }
  return (l <= debugLevel);
}

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

exports.debug = debug;

var functions = {
  debug: 'var debug = function(item, subitem, info, level) {' +
         'tools.debug(MODULE, item, subitem, info, level); };',
  fdebug: 'var fdebug = function fdebug (subitem, info, level) {' +
          'var item = arguments.callee.caller.name ? ' +
          'arguments.callee.caller.name : "::";' +
          'debug(item, subitem, info, level); };'
}

getFunctionCode = function(name) {
  return functions[name];
}

exports.getFunctionCode = getFunctionCode;

exports.inspect = function(o) {
  return util.inspect(o, false, 2, true);
}

String.prototype.trim = function() {
  return this.replace(/^\s+|\s+$/g,"");
}

exports.pad2 = function(n) {
  return n<10 ? '0'+n : n
}

/**
 * Liefert ähnlich zu parseFloat ein Float-Zahl, die der String s repräsentiert.
 * Misslingt die Wandlung, so wird der Wert von d geliefert. Der Rückgabewert 
 * ist also in jedem Fall eine Float-Zahl.
 * @param s die Zahl als String.
 * @param d default-Wert (ohne Angabe 0.0).
 * @returns Float-Zahl
 */
exports.getFloat = function(s, d) {
  var _d = d == undefined ? 0.0 : d;
  var x = parseFloat(s);
  return isNaN(x) ? _d : x;
}
/**
 * Liefert ähnlich zu parseInt ein Int-Zahl, die der String s repräsentiert.
 * Misslingt die Wandlung, so wird der Wert von d geliefert. Der Rückgabewert 
 * ist also in jedem Fall eine Int-Zahl.
 * @param s die Zahl als String.
 * @param d default-Wert (ohne Angabe 0).
 * @returns Float-Zahl
 */
exports.getInt = function(s, d) {
  var _d = d == undefined ? 0 : d;
  var x = parseInt(s);
  return isNaN(x) ? _d : x;
}

/**
 * Testet, ob das übergebene Objekt leer ist.
 * @param obj 
 * @returns true oder false
 */
var isEmpty = function(obj) {
  return Object.keys(obj).length === 0;
}

exports.isEmpty = isEmpty;

exports.getEnv = function(target, next, body) {
  var next_args = [].slice.call(arguments, 2);
  // Array ab 3. Parameter erzeugen [body, ..., ...]
  if (isEmpty(target)) {// Erster Aufruf?
  // target muss ein Objekt sein, damit es per Referenz übergeben wird.
    var spawn = require('child_process').spawn;
    var env = spawn('/usr/bin/printenv');
    var result = null;
    env.stdout.on('data', function (data) {
      result = data;
    });
    env.on('exit', function (code) {
      if (result) {
        var e0 = result.toString().split('\n');
        for (var i in e0) {
          var e = e0[i].split('=');
          target[e[0]] = e[1];
        }
      }
      //fdebug('e0', inspect(e0), 102);
      if (!target.TMPDIR) target.TMPDIR = '/tmp';
      next.apply(this, next_args); 
    });
  } else {
    next.apply(this, next_args);
  }
}

// Siehe: https://github.com/ryanmcgrath/wrench-js
exports.rmdirRecursive = function(dir, clbk){
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

