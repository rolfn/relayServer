
var crc = require('crc');

/**
 * Wandelt Hex-kodierte Kommando/Subkommando und ggf. 16 Datenbytes in
 * VACOM-Binärdaten (einschließlich der Checksumme). Beispiele:
 * 
 * "0100" --> "VMG"          (Gerätename)
 * "0101" --> "1.3.3c"       (Softwareversion)
 * "0102" --> "26884000050"  (Seriennummer)  
 * "2010" --> "1.330000E-03" (mbar) 
 * "2011" --> "1.330000E-01" (Pa)
 * "2012" --> "9.975000E-04" (Torr) 
 *
 * @author Rolf Niepraschk
 * @param String s Hex-String (4 oder 4+32 Nibble-Character)
 * @return Buffer Resultat (24 Bytes)
 */
function encodeVACOM(s) {
  // (Kommadobyte + Subkommandobyte + 16 Datenbytes) * (Lo + Hi) = 36 Bytes 
  if (s.length > 36) return ''; 
  // var buf = Buffer.alloc(24); // default: zero-filled; erst ab 5.10
  var buf = new Buffer(24), sbuf = new Buffer(s, 'hex');
  buf.fill(0);
  buf[0] = 0xA5; // Frame-Beginn
  buf[1] = 0x50; // Kommandobyte gültig, erster Frame, Antwort erforderlich
  buf[2] = 0x00; // Empfängeradresse 
  buf[3] = 0x00; // Absenderadresse
  for (var i=0; i<sbuf.length; i++) { 
    buf[i+4] = sbuf[i];
  }
  var c = crc.crc16modbus(buf.slice(0, -2)); // CRC bestimmen; ohne CRC-Bytes 
  buf[22] = c & 0x00ff; buf[23] = c >> 8;
  return buf;
}
exports.encodeVACOM = encodeVACOM;

/**
 * Wandelt Binär-Antwort, welche einen max. 16 Byte langen String enthält.
 *
 * @author Rolf Niepraschk
 * @param String b Binärdaten
 * @return String Resultat
 */
function decodeVACOMstring(b) {
  // TODO: CRC der Daten überprüfen und geeignete Fehlermeldung generieren.
  // TODO: Außer Strings noch Float-Format unterstützen (???).
  // TODO: Muti-Frames unterstützen (???).
  var str = b instanceof Buffer ? b.toString('binary') : b;
  var ch = '', a = [];
  for (var i=6; i<22; i++) {
    ch = str[i];
    if (ch == '\0') break;
    a.push(ch);
  }
  return a.join('');
}
exports.decodeVACOMstring = decodeVACOMstring;

