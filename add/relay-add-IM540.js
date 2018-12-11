
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus IM540 Antwort
 * Achtung: IM540 im IM520 Mode betreiben
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractIm540(s) {
// var regex = /^(MES\sR\rMBAR\s)([0-9]{1}\.[0-9]{1,2}[E][-+][0-9]{2})(\r\n)$/;
// schwächer:
// jetzt in Pa
// "MES R\r\nPA   1.48E-08\r\n"
  var regex = /(PA\s*)([0-9]{1}\.[0-9]{1,2}[E][-+][0-9]{2})(\r\n)$/;

  return x.strToNum(regex.exec(s), 2);
}
exports.extractIm540 = extractIm540;
