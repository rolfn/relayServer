
/**
 * Wandelt bestimmte 4 Bytes, die das Modbus-Profibus-Gateway "NT 100-RE-DP"
 * nach Zugriff auf am Profibus angeschlossene CDGs (Inficon; z.B. CDG045D) 
 * liefert. Es wird eine Konfiguration für ein oder mehrere CDGs mit der 
 * Moduleinstellung "ExS,PVF,ChS,TpS" angenommen (siehe Datei "CDGX0B7E.GSD").
 * 
 * Der relayServer wird mit "Action" "MODBUS" angesprochen.
 * Als Parameter "Address" ist 0 und für "Quantity" mindestens
 *     "höchste Messkopfadresse" * 4
 * anzugeben. Kontinuierliche Adressvergabe für die Messköpfe bei 1 beginnend 
 * vorausgesetzt, können auf diese Weise maximal 31 Messköpfe angesprochen 
 * werden (31*4 Doppelbytes < 125 Doppelbytes).
 *
 * @author Rolf Niepraschk
 * @param Buffer buf Rückgabe des Modbus-Profibus-Gateways
 * @param _pAdr Number Profibus-Adresse (default: 1) 
 * @param _cnt Number Anzahl der Druckwerte (default: 1) 
 * @return Number/Array Float-Zahl(en); bei Fehler (z.B. Anheizphase): NaN
 */
function readPBusCDG(buf, _pAdr, _cnt) {
  // Problem: Es werden auch für einen Einzelwerte immer alle vorhandenen 
  // Messköpfe ausgelesen, was u.U. zu Zeitproblemen führt. Ist das nicht 
  // tolerierbar, müsste das Verfahren modizifiert werden: "Address" 
  // entsprechend der Profibus-Adresse verändern (mit "Quantity":4). 
  var pAdr = parseInt(_pAdr), cnt = parseInt(_cnt), a = [], pos, err;
  if (isNaN(pAdr)) pAdr = 1;
  if (isNaN(cnt)) cnt = 1;
  for (var i=0; i<cnt; i++) {
    pos = 8 * (pAdr+i) - 8;
    err = buf.readUInt8(pos+4) != 0;
    if (err) a.push(NaN); else a.push(buf.readFloatBE(pos));
  }  
  return (a.length > 1) ? a : a[0];
}

exports.readPBusCDG = readPBusCDG;
