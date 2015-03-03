/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2015-02-27
 */

var cfg = require('./config.js');
var util = require('util');
var fs = require('fs');
var Fs = require('fs');
var path = require('path');

/**
 * Erzeugt String-Repräsentation der inneren Struktur einer JS-Variable
 * (Rekursion bis Ebene 2, coloriert)                                 F
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
};

/**
 * Ergänzt für Zahlen n < 10 eine führende Null.
 * @param {number} n Ganzzahl
 * @return {string} auf zwei Stellen ergänzte Zahl
 */
function pad2(n) {
  return n<10 ? '0'+n : n;
}

exports.pad2 = pad2;

/**
 * Liefert ähnlich zu parseFloat eine Float-Zahl, die der String s repräsentiert.
 * Misslingt die Wandlung, so wird der Wert von d geliefert. Der Rückgabewert
 * ist also in jedem Fall eine Float-Zahl.
 * @param {string} s die Zahl als String.
 * @param {number} d default-Wert (ohne Angabe 0.0).
 * @return {number} Float-Zahl
 */
exports.getFloat = function(s, d) {
  var _d = d === undefined ? 0.0 : d;
  var x = parseFloat(s);
  return isNaN(x) ? _d : x;
};
/**
 * Liefert ähnlich zu parseInt eine Int-Zahl, die der String s repräsentiert.
 * Misslingt die Wandlung, so wird der Wert von d geliefert. Der Rückgabewert
 * ist also in jedem Fall eine Int-Zahl.
 * @param {string} s die Zahl als String.
 * @param {number} d default-Wert (ohne Angabe 0).
 * @return {number} Int-Zahl
 */
exports.getInt = function(s, d) {
  var _d = d === undefined ? 0 : d;
  var x = parseInt(s);
  return isNaN(x) ? _d : x;
};

/**
 * Testet, ob das übergebene Objekt leer ist.
 * @param {object} obj
 * @return {boolean} true, wenn leeres Objekt
 */
var isEmpty = function(obj) {
  return Object.keys(obj).length === 0;
};

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
