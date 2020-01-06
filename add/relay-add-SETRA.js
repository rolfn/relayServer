
var x = require('./relay-add-MISC.js');

/**
 * Extrahiert Float-Zahl aus Strings des Setras
 * 
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractSetra(s) {
  // ' +799.31   mbar A OK\r\n'
    var regex = /^([\s]*)([+]?[0-9]{0,5}\.?[0-9]{1,5})([\s]*mbar A OK)/;

  return x.strToNum(regex.exec(s),2);
}
exports.extractSetra =extractSetra;
