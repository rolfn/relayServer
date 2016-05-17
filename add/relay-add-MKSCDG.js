
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus String welcher von den MKS CDGs
 * geliefert wird
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractMKSCDG(s) {

  var regex = /^(\w*\s\s)([-+]?[0-9]*\.[0-9]{1,5}[eE]*[-+]*[0-9]*)/;
    return x.strToNum(regex.exec(s), 2);
}
exports.extractMKSCDG = extractMKSCDG;
