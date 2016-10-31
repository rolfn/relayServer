var x = require('./relay-add-MISC.js');
/**
 * Extrahiert Float-Zahl aus String welcher vom Phillips
 * 2535 geliefert wird
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractPM2535Temp(s) {
    var regex = /([+][0-9]{3}\.?[0-9]{2}[E]{1}[-+]{1}[0-1]{2})(\n)$/;
    return x.strToNum(regex.exec(s),1);
}
exports.extractPM2535Temp = extractPM2535Temp;
