
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus String
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractMKT50(s) {
  var regex = /(T1=\s*\+)([0-9]{2}\.?[0-9]{3,5})/;
  return x.strToNum(regex.exec(s), 2);
}
exports.extractMKT50 = extractMKT50;
