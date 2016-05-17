
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus String welcher von
 * den Leybold SRG- Kontrollern VM212 geliefert wird
 * Es wird auch auf DCR getestet
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractVM212DCR(s) {
  var regex = /^(\sDCR\s\s)([+-][0-9]{1}\.?[0-9]{4}[E][-][0-9]{2})/;

  return x.strToNum(regex.exec(s), 2);
};
exports.extractVM212DCR =  extractVM212DCR;



