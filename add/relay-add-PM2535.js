
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus String welcher vom Phillips
 * 2535 geliefert wird
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractPhillipsTemp(s) {
  // TODO: Richtig: PHILIPS; besserer Name "extractPM2535Temp"
  var regex = /^(TDC\s*)([-+]{1}[0-3]{3}\.?[0-9]{2}[E]{1}[-+]{1}[0-1]{2})(\n)$/;

  return x.strToNum(regex.exec(s),2);
}
exports.extractPhillipsTemp= extractPhillipsTemp;
