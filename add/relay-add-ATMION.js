
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus String wie von
 * Atmion IG (z.B. SE1) gesendet
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractAtmion(s) {
  var regex = /^(0,\t)([0-9]{1}\.?[0-9]{4}[Ee][-+][0-9]{2})(\r)$/;

  return x.strToNum(regex.exec(s), 2);
}
exports.extractAtmion = extractAtmion;

