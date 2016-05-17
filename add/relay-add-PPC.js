
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus PPC4 Antwort
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl
 */

function extractPPC(s) {
  var regex = /^(R\,)([+-]?[0-9]{1,4}\.?[0-9]{1,3})\s*mbar/

  var n = x.strToNum(regex.exec(s), 2)
  return n;

}
exports.extractPPC = extractPPC;


