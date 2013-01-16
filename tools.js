/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-01-16
 */

const MODULE = 'tools';

var util = require('util');
var fs = require('fs');

/**
 * Kommandozeilenwert zur Steuerung der debug-Ausgabe ermitteln. Ohne
 * Angabe wird "0" verwendet.
 */
var debugLevel = (process.argv[2]) ? process.argv[2] : 0; // 5, 99

/**
 * Liefert true, wenn level kleiner oder gleich dem Wert, der auf der
 * Kommandozeile übergeben wurde, ist. Ohne Kommandozeilenwert wird "99"
 * angenommen.
 * @param {number} level 
 * @return {boolean} 
 */
function isDebug(level) {
  var l = 99;
  if (level != undefined){
    l = level;
  }
  return (l <= debugLevel);
}

exports.isDebug = isDebug;

/**
 * Konstanten für SGR-Code
 */
const BOLD = 1;
const DEFCOLOR = 39;
const UNBOLD = 22;
const COLOR = 30;
const RED = 1;
const BLUE = 4;
const RESET = 0;

/**
 * Erzeugt ESC-Code ("Select Graphic Rendition")
 * (Rekursion bis Ebene 2, coloriert)
 * @param {number} code Farb-/Schriftkonstante
 * @return {string} ESC-Code 
 */
function sgr(code) {// Select Graphic Rendition
  return '\u001b[' + code + 'm';
}

/**
 * In Abhängigkeit von "level" Ausgabe von Informationen nach stderr. 
 * @param {string} module meist Modulname
 * @param {string} item meist Funktionsname
 * @param {string} _subitem spezifische Aktion innerhalb der Funktion.
 * @param {string} _info Daten
 * @param {number} _level
 */
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

/**
 * Datenstruktur mit zu konfigurierenden Funktionen @see createFunction
 */
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

/**
 * Erzeugt aufgrund von Eintrag name in "functions" eine Funktion und
 * liefert diese zurück. Die Funktion kann aufgrund von maximal 3 Parametern
 * statisch konfiguriert werden.
 * @param {string} name Schlüsselwort für "functions" 
 * @param {???} p1 Konfigurationsparameter
 * @param {???} p2 Konfigurationsparameter
 * @param {???} p3 Konfigurationsparameter
 * @return {function} Konfigurierte Funktion
 */
function createFunction(name, p1, p2, p3) {
  return functions[name](p1, p2, p3);
}

exports.createFunction = createFunction;

/**
 * In Abhängigkeit von "level" Ausgabe von Informationen. Der aktuelle 
 * Modulname und Funktionsname wird ebenfalls ausgegeben.
 * @param item meist Funktionsname
 * @param subitem spezifische Aktion innerhalb der Funktion.
 * @param info Daten
 * @param level
 */
function fdebug(subitem, info, level) {
  item = arguments.callee.caller.name ?
    arguments.callee.caller.name : '---';
  debug(MODULE, item, subitem, info, level);
}

/**
 * Erzeugt String-Repräsentation der inneren Struktur einer JS-Variable
 * (Rekursion bis Ebene 2, coloriert)
 * @param {object} o Zu untersuchende JS-Variable.
 * @return {string}  String-Repräsentation
 */
function inspect(o) {
  return util.inspect(o, false, 2, true);
}

exports.inspect = inspect;

/**
 * Beseitigt am Anfang und am Ende eines Strings "whitespaces".
 * @return {string} 
 */
String.prototype.trim = function() {
  return this.replace(/^\s+|\s+$/g,"");
}

/**
 * Ergänzt für Zahlen n < 10 eine führende Null.
 * @param {number} n Ganzzahl
 * @return {string} auf zwei Stellen ergänzte Zahl
 */
function pad2(n) {
  return n<10 ? '0'+n : n
}

exports.pad2 = pad2;

/**
 * Liefert das systemübliche temporäre Verzeichnis, sofern definiert (TMPDIR),
 * ansonsten '/tmp'.
 * @return {string} temporäres Verzeichnis
 */
function getTempDir() {
  return process.env.TMPDIR ? process.env.TMPDIR : '/tmp'
}

exports.getTempDir = getTempDir;

/**
 * Liefert ähnlich zu parseFloat eine Float-Zahl, die der String s repräsentiert.
 * Misslingt die Wandlung, so wird der Wert von d geliefert. Der Rückgabewert 
 * ist also in jedem Fall eine Float-Zahl.
 * @param {string} s die Zahl als String.
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
 * @param {string} s die Zahl als String.
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
 * @return {boolean} true, wenn leeres Objekt
 */
var isEmpty = function(obj) {
  return Object.keys(obj).length === 0;
}

exports.isEmpty = isEmpty;

/**
 * Löscht rekursiv eine Verzeichnisstruktur (siehe: <a href="https://github.com/ryanmcgrath/wrench-js" target="_blank">wrench-js</a>).
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
 * Erzeugt in einem temporären Verzeichnis eine Datei mit Inhalt.
 * @param {string} dir Temporäres Verzeichnis
 * @param {string} name Name der Datei
 * @param {Buffer} content Inhalt der Datei
 * @param {function} error Aufruf im Fehlerfall
 * @param {function} success Aufruf bei Erfolg
*/
function createTempFile(dir, name, content, error, success) {
  // TODO: von "rscript.js" in allg. Form übernehmen!
}

exports.createTempFile = createTempFile;


/**
 * Analysiert übergebenen String, ob es sich um BASE64-Code handelt.
 * (Test ist nicht 100%ig sicher, aber vermutlich ausreichend.)
 * @param {string} b 
 * @return {boolean} true, wenn  BASE64-Code
*/
function isBASE64(b) {
  r = /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/;
  return r.test(b);
}

exports.isBASE64 = isBASE64;
