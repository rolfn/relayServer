
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
 * @return Object (o) mit Property o.Status Int und o.Value Number/Array Float-Zahl(en)
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
    a.push(buf.readFloatBE(pos));
  }

  // s. Inficon CDG Manual
  // Abschnitt 7.1.11  Exeption Status
  // Druck kleiner Auflösung liefert:
  //  5 (bit 0+2)
  // im Status byte 4 (mehr Sinn würde bit 7+5
  // ergeben)
  //
  // > b = new Buffer(1)
  // <Buffer 00>
  // > b[0] = 05
  // > b.readIntLE(0)
  // 5
  // > b.readIntBE(0)
  // undefined

  return {"Status": buf.readInt8(pos+4),
          "Value": (a.length > 1) ? a : a[0]};
}

exports.readPBusCDG = readPBusCDG;
