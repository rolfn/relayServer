
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus Inficon Cube RS232
 * Antwort
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractInfCube(s) {

//PRE\r\n-0.003126628\n\rSL>"
  var regex = /(PRE\r\n)([-+]?[0-9]*\.?[0-9]*)(\n\rSL\>)$/;

  return x.strToNum(regex.exec(s), 2);
}
exports.extractInfCube = extractInfCube;
