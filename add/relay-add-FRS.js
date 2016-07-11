
var misc = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus String welcher von
 * der FRS geliefert wird
 * Es wird nicht auf lb getested: Bei großen
 * Drücken kann der Druck ruhig in der letzten
 * Stelle schwanken (also das lb verschwinden)
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractFRS(s) {
    var regex = /^([+-]{0,1}[\s]{0,2}[0-9]{1,2}\.?[0-9]{6})/;

    return misc.strToNum(regex.exec(misc.vlTrim(s)), 1);
};
exports.extractFRS =  extractFRS;
