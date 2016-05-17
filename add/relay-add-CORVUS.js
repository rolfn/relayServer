
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Array mit zwei Float-Zahl aus
 * String welcher vom Corvus Kontroller geliefert wird
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Array Achsen.
 */
function extractCorvusArray(s) {
  var regex = /^[\s]{0,4}([-]?[0-9]{1,3}\.[0-9]{4,6})[\s]{1,5}([-]?[0-9]{1,3}\.[0-9]{4,6})/
    , ns    = regex.exec(s);
  return [x.strToNum(ns, 1), x.strToNum(ns, 2)] ;
};
exports.extractCorvusArray = extractCorvusArray;

