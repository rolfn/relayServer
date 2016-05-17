
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus String welcher vom Temperaturnormal
 * F250 geliefert wird
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractF250(s) {
  var regex = /^(A\s{1,2})([2-3]{2}\.?[0-9]{2,3})(C\r\n)$/;

  return x.strToNum(regex.exec(s),2);
}
exports.extractF250 = extractF250;
