
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus Strings des Geräts Paroscientific
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractParo(s) {
  var regex = /^(\*0001)([+-]?[0-9]{0,4}\.?[0-9]{1,4})/;

  return x.strToNum(regex.exec(s),2);
}
exports.extractParo = extractParo;
