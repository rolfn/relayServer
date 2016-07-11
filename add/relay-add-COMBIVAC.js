
var misc = require('./relay-add-MISC.js')
  , stat = require('./relay-add-STATISTICS.js');

/**
 * Extrahiert Float-Zahl aus Combivac Antwort
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl
 */

function extractCombi(s) {
  var regex = /^([1-3][\:]MBAR{0,2})([0-9]{0,2}\.?[0-9]{0,3}E[-+][0-9]{2})/

  var n = misc.strToNum(regex.exec(misc.vlTrim(s)), 2)

  return n == 0 ? NaN: n;

}
exports.extractCombi = extractCombi;
