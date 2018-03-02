/**
 *
 * Funktion gibt Status der Ventile an SE1 zurück.
 * Es muss für die toString Wandlung eine genügende
 * Anzahl von Bits sichergestellt werden (2^32 = 4294967296:
 * 100000000000000000000000000000000) damit V[pos]
 * sicher funktioniert (pos ändert sich bei führenden 0en).
 *
 * @author wactbprot
 * @param {string} hexstr  Ventilrückmeldung
 * @param {string} valve  Ventilbezeichnung
 * @return {object} mit {'Valve_closed': true| false, 'Valve_opened':  false|true}
 *
 */
function se1ValveStatus(hexStr,valve) {

    var BN = 4294967296,
    V={V6:3,
       V5:4,
       V4:5,
       V3:6,
       V2:7,
       V1:8
      },
    num = parseInt(hexStr,16) + BN,
    pat = num.toString(2).split('');

    return {'Valve_closed': pat[V[valve]] == '1',
      'Valve_opened': pat[V[valve]] == '0' };

}
exports.se1ValveStatus = se1ValveStatus;

/**
 * Berechnet, in Abhängigkeit von Ziel- und Istdruck
 * den aktuellen Sollfluß für die SE1/FM3 Fülldruckeinstellung.
 *
 *
 * @author wactbprot
 * @param {number} psoll Solldruck in mbar
 * @param {number} psoll Istdruck in mbar
 * @param {number} Vopen kleines oder großes Volumen
 * @return {object} Zielfluß bzw. Setpoint für Regler 1&2
 */
function calQsp(psoll, pist, mq){
  var ret = {};
  if (psoll                    &&
      pist                     &&
      typeof psoll == "number" &&
      typeof pist  == "number"   ){
    mq      = mq || 0.018; // [mq] = mbar/s/sccm 0.018 passt ~ für SE1 und FM3
    // FM3 war:  mq = Vopen ? 0.0133 : 0.0155,

   var  ts      = 20,          // Sollzeit (p wird theor. in ts erreicht)
        bord    = 0.7,         // Start Regelung rel. Abw. von psoll
        sscbord = 2.0,        // Start 2. Regler
        eps     = 0.005,        // Ende Regelung rel. Abw. von psoll
        md      = 1;           // Dämpf./verst. der Regel.

    // genauere Einstellung durch psoll * (1 + eps)
    ret.dp       = Math.abs(psoll * (1 + eps)/ pist - 1);
    ret.pfill_ok = false;
    // es dauert theor. ts sec bis psoll erreicht wird,
    // wenn der Druck mit mq ansteigt
    var q        = psoll / ts / mq,
        f        = md * ret.dp;

    if (typeof ret.dp == "number") {

      // Gas
      if (ret.dp > bord) {
        if (q && q < sscbord) {

	  ret.sp1 = q ;
	  ret.sp2 = 0;
        }
        if (q && q > sscbord){
	  ret.sp1 = q ;
	  ret.sp2 = q / 2;
        }
      }
      // Kupplung
      if (ret.dp <= bord) {
        ret.pfill_ok = false;
        if (q * f && q * f < sscbord) {
          ret.sp1 = q * f;
          ret.sp2 = 0;
        }
        if (q * f && q * f > sscbord) {
          ret.sp1 = q * f ;
          ret.sp2 = q * f / 2;
        }
      }
      // Bremse
      if (ret.dp < eps || pist > psoll) {
        ret.pfill_ok = true;
        ret.sp1 = 0;
        ret.sp2 = 0;
      }
      return ret;
    }
  }else{
    ret.pfill_ok = false;
    ret.sp1 = 0;
    ret.sp2 = 0;
    return ret;
  }
}
exports.calQsp = calQsp;

