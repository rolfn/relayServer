/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-11-04
 */

const MODULE = 'tools';

var util = require('util');
var fs = require('fs');

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

exports.getTempDir = getTempDir;  // TODO: Modul "tmp" verwenden.

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
        logger.debug('dir: %s', dir);
        return fs.rmdir(dir, clbk);
      }
      var file = dir+'/'+filename;
      fs.stat(file, function(err, stat){
        if (err) return clbk(err);
        if (stat.isDirectory()) {
          logger.debug('dir: %s', file);
          rmdirRecursive(file, rmFile);
        } else {
          fs.unlink(file, rmFile);
          logger.debug('unlink: %s', file);
        }
      });
    })();
  });
};

exports.rmdirRecursive = rmdirRecursive;

/**
 * Erzeugt in einem temporären Verzeichnis eine Datei mit Inhalt.
 * @param {string} dir temporäres Verzeichnis
 * @param {string} name Name der Datei
 * @param {Buffer} buf Inhalt der Datei
 * @param {function} success Aufruf bei Erfolg
 * @param {function} error Aufruf im Fehlerfall
*/
function createTempFile(dir, name, buf, success, error) {
  fs.mkdir(dir, '700', function (e) {
    logger.debug('create working directory: %s', e ? e : dir);
    if (e) {
      error(e);
    } else {
      fs.open(dir + '/' + name, 'w', '600', function(e, fd) {
        logger.debug('file open: %s', e ? e : name);
        if (e) {
          error(e);
        } else {
          fs.write(fd, buf, 0, buf.length, null, function(e, nb, buf){
            logger.debug('file write: %s', e ? e : nb + ' Bytes');
            if (e) {
              error(e);
            } else {
              fs.close(fd, function(e){
                logger.debug('file close: %s', e ? e : ' --> next step');
                if (e) {
                  error(e);
                } else {
                  success();
                }
              });
            }
          });
        }
      });
    }
  });
}

exports.createTempFile = createTempFile;
