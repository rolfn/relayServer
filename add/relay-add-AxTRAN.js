
var x = require('./relay-add-MISC.js');
/**
 * Extrahiert Float-Zahl aus AxTRAN Antwort
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */

function extractAxtran(s) {
  var regex = /^([0-9]{1}\.?[0-9]{1,2}[E][-+][0-9]{2})/;

  return x.strToNum(regex.exec(s), 1);
}
exports.extractAxtran = extractAxtran;
