
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus SRG-3 Antwort
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractSRG3(s) {
  var regex = /^([\s]?)([0-9]{1}\.?[0-9]{4}[E][-+][0-9]{2})([\s]?\r\n\>)$/;

  var n = x.strToNum(regex.exec(s), 2)

  return n == 0 ? NaN: n;

}
exports.extractSRG3 = extractSRG3;
