
var misc = require('./relay-add-MISC.js')
  , stat = require('./relay-add-STATISTICS.js');

/**
 * Extrahiert Float-Zahl aus String
 * z.B. SE1 CDG 10, 100, 1000
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractKeithleyVolt(s) {
  var regex = /^([+-][0-9]{1}\.?[0-9]{1,8}[Ee][-+][0-9]{2})(VDC)/;

  return misc.strToNum(regex.exec(s), 1);

}
exports.extractKeithleyVolt = extractKeithleyVolt;

/**
 * Extrahiert Float-Zahl aus String
 * z.B. SE2 Temperaturen
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractKeithleyC(s) {
  var regex = /^([+-][0-9]{1}\.?[0-9]{1,8}[Ee][-+][0-9]{2})([_,])/;
  return misc.strToNum(regex.exec(s), 1);
}
exports.extractKeithleyC = extractKeithleyC;

/**
 * Extrahiert Float-Zahl aus String
 * z.B. SE1  Temperatursensoren
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractKeithleyTemp(s) {
var regex = /^([+-][0-9]{1}\.?[0-9]{1,8}[Ee][-+][0-9]{2})(,)/;

  return misc.strToNum(regex.exec(s), 1);

}
exports.extractKeithleyTemp = extractKeithleyTemp;

/**
 * Erstellt Array aus Temperatur Scan Resultaten
 * wie sie von Keithley 2700s
 * geliefert werden
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractKeithleyTempScan(sObj, e) {
  var  regex_sc  = /^,?(\+[1-3]{1}\.?[0-9]{8}E\+01)/
    return extractKeithleyScan(sObj,  e, regex_sc);
}
exports.extractKeithleyTempScan = extractKeithleyTempScan;

/**
 * Erstellt Array aus Temperatur Scan Resultaten
 * wie sie von Keithley 2700s
 * geliefert werden
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractKeithleyPressScan(sObj, e) {
  var  regex_sc  = /^,?([+-]?[0-9]*\.?[0-9]{8}E[+-]?[0-9]{2})/
    return extractKeithleyScan(sObj,  e, regex_sc);
}
exports.extractKeithleyPressScan = extractKeithleyPressScan;


function extractKeithleyScan(sObj, e, regex_sc){
  var regex_ch  = /^(\(\@)([0-9]{3}):([0-9]{3})\)$/
    , ch        = regex_ch.exec(e)
    , start_ch  = parseInt(ch[2],10)
    , end_ch    = parseInt(ch[3],10)
    , r1        = {}
    , r2        = {}
    , ret       = {}
  // Einsortieren
  for(var l in sObj){
    r1[l] = {};
    var s1 = sObj[l].split("#")
      , j  = 0
    for(var i = start_ch; i  < end_ch +1; i++){
      r1[l][i] = misc.strToNum(regex_sc.exec(s1[j]), 1)
      j++;
    }
  }
  // Umsortieren
  for(var k = start_ch; k  < end_ch +1; k++){
    r2[k] = [];
    for(var m in sObj){
      r2[k].push(r1[m][k])
    }
  }
  // stat
  for(var n = start_ch; n  < end_ch +1; n++){
    ret[n] = stat.vlStat(r2[n])
  }
  return ret;
}
