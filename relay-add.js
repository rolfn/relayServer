/**
 * Dedizierte Funktionen zur Vereinfachung des
 * Postprocessing einer Task.
 *
 * Eine hier definierte Funktion
 * z.B. helloSandbox() kann über:
 *
 *  _.helloSandbox()
 *
 * im Postprocessing ausgeführt werden.
 *
 * @author wactbprot (thsteinbock@web.de)
 * version: 2013-06-07
 */

/**
 * Berechnet, in Abhängigkeit von Ziel- und Istdruck
 * den aktuellen Sollfluß für die SE1/FM3 Fülldruckeinstellung.
 *
 *
 * @author wactbprot
 * @param psoll Number Solldruck in mbar
 * @param psoll Number Istdruck in mbar
 * @param Vopen Number kleines oder großes Volumen
 * @return Object Zielfluß bzw Setpoint für Regler 1&2
 */
function calQsp(psoll, pist, mq){

  if (psoll                    &&
      pist                     &&
      typeof psoll == "number" &&
      typeof pist  == "number"   ){
    mq      = mq || 0.018; // [mq] = mbar/s/sccm 0.018 passt ~ für SE1 und FM3
    // FM3 war:  mq = Vopen ? 0.0133 : 0.0155,
    var ret     = {},
        ts      = 20,          // Sollzeit (p wird theor. in ts erreicht)
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
        f        = md * ret.dp / bord;

    if (typeof ret.dp == "number") {
      // Gas
      if (ret.dp > bord) {
        if (q && q < sscbord) {

	  ret.sp1 = q ;
	  ret.sp2 = 0;
        }
        if (q && q > sscbord){
	  ret.sp1 = q / 10;
	  ret.sp2 = q;
        }
      }
      // Kupplung
      if (ret.dp <= bord) {
        ret.pfill_ok = false;
        if (q * f && q * f < sscbord) {
          ret.sp1 = q * f;
          ret.sp2 = q * f / 100;
        }
        if (q * f && q * f > sscbord) {
          ret.sp1 = q * f / 100;
          ret.sp2 = q * f;
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
  }
}
exports.calQsp = calQsp;


/**
 * Berechnet Mittelwert und Standardabweichung
 * eines gegebenen Vectors (bzw. Arrays).
 *
 *
 * @author wactbprot
 * @param x Array Datenreihe
 * @return res Object   res.mv (Mittelwert) res.sd (Standardabweichung) und re.N (Länge)
 */
function vlStat(x) {
  if (x && x.length > 2) {
    var res = {},
    mv = 0,
      sdhelp = 0,
      n = x.length;
    mv = x.reduce(function(a, b) {
      return a + b;
    }) / n;
    res.mv = mv;
    res.N = n;
    x.map(function(i) {
      sdhelp += Math.pow((i - mv), 2);
    });
    sd = Math.sqrt(1 / (n - 1) * sdhelp);
    res.sd = sd;
    return res;
  }
}
exports.vlStat = vlStat;


/**
 * Testet Array auf numerische Einträge und sortiert ggf. aus
 *
 *
 * @author wactbprot
 * @param arr Array Datenreihe
 * @return res Object   res.Arr "sauberes" Array, res.Skip Indizes der verworfenen Einträge
 */
function checkNumArr(arr) {
  if (arr && Array.isArray(arr)) {
    var res = {};
    res.Arr = [];
    res.Skip = [];
    arr.map(function(v, i) {
      if (isNumber(v)) {
        res.Arr.push(v);
      }
      else {
        res.Skip.push(i);
      }
    });
    return res;
  }
}
exports.checkNumArr = checkNumArr;

/**
 * Entfernt Einträge aus einer Datenreihe.
 *
 *
 * @author wactbprot
 * @param arr Array Datenreihe
 * @param arr Integer "skip" Index
 * @return res Array resultierendes Array
 */
function rmByIndex(Arr, Idx) {
  Idx.map(function(i) {
    Arr.splice(i, 1);
  });
  return Arr;
}
exports.rmByIndex = rmByIndex;

/**
 * Berechnung der Steigung und zugeordneter Parameter.
 * - erzeugt zunächst aus den Vektoren
 *   tstart & tstop ein t
 * - versucht Ausreiser auf einfache Art
 *   zu eliminieren (Residuen > d_border werden verworfen)
 * -- max _iter_ Punkte werden verworfen
 * -- verworfen werden Pkt., die weiter
 *    als relative _d_border_ (0.6 entsp. 60%)
 *    von der Geraden weg liegen
 *
 *
 * @author wactbprot
 * @param vec Array Datenreihe
 * @param tstart Array Startzeiten
 * @param tstop  Array Stopzeiten
 * @return res Object Ausgabe der slope Function
 */
function vlSlope(vec, tstart, tstop) {
  var t = [],
    rel_diff = [],
    iter_N = 5,
    again = true,
    d_border = 0.6;
  for (var k = 0; k < tstart.length; k++) {
    t.push((tstart[k] + tstop[k]) / 2);
  }
  var hs = slope(vec, t),
    vlm = hs.bx,
    vlc = hs.Cx;
  for (var m = 0; m < iter_N; m++) {
    if (again) {
      again = false;
      for (var l = 0; l < t.length; l++) {
        var predict_val = vlm * t[l] + vlc;
        if (Math.abs((vec[l] - predict_val) / predict_val) > d_border) {
          vec = rmByIndex(vec, [l]);
          t = rmByIndex(t, [l]);
          hs = slope(vec, t);
          vlm = hs.bx;
          vlc = hs.Cx;
          again = true;
        }
      } // l
    } //again
  } //m
  return slope(vec, t);
}
exports.vlSlope = vlSlope;

/**
 * Reine Statistikfunktion zur Berechnung der Parameter der
 * linearen Regression x~y.
 *
 * @author wactbprot
 * @param y Array y-Werte (z.B. Spannung, Druck)
 * @param x Array x-Werte (z.B. Zeit)
 * @return ret Object mit  Mittelwert X, Mittelwert Y, Korrelationskoeff R, Achsenabschnitt Cx, Steigungen bx, by
 */
function slope(y, x) {
  if (x.length == y.length) {
    var ret = {},
    sumX = 0,
      XArr = [],
      sumY = 0,
      YArr = [],
      remainN = 0,
      SSxy = 0,
      SSxx = 0,
      SSyy = 0;
    for (var i = 0; i < y.length; i++) {
      if (isNumber(y[i]) && isNumber(x[i])) {
        sumX = sumX + x[i];
        XArr.push(x[i]);
        sumY = sumY + y[i];
        YArr.push(y[i]);
        remainN++;
      }
    }
    mvX = sumX / remainN;
    mvY = sumY / remainN;
    for (var j = 0; j < YArr.length; j++) {
      SSxy = SSxy + (XArr[j] - mvX) * (YArr[j] - mvY);
      SSxx = SSxx + Math.pow(XArr[j] - mvX, 2);
      SSyy = SSyy + Math.pow(YArr[j] - mvY, 2);
    }
    ret.remainN = remainN;
    ret.mvX = mvX;
    ret.mvY = mvY;
    ret.bx = SSxy / SSxx;
    ret.by = SSxy / SSyy;
    ret.R = (SSxy * SSxy) / (SSxx * SSyy);
    ret.Cx = mvY - ret.bx * mvX;
    return ret;
  }
}
exports.slope = slope;

/**
 * Das Ergebnis von regexpr.exec sieht so aus:
 *
 * ```
 *   s = "A 23.234C\r\n"
 *  'A 23.234C\r\n'
 *  >  var regex = /^(A\s)([2-3]{2}\.?[0-9]{2,3})(C\r\n)$/;
 *  > regex.exec(s)
 *  [ 'A 23.234C\r\n',
 *    'A ',
 *    '23.234',
 *    'C\r\n',
 *    index: 0,
 *    input: 'A 23.234C\r\n' ]
 *  > regex.exec(s)[2]
 *  '23.234'
 * ```
 * D.h. die 0te position ist der Eingangsstring und
 * erst dann kommen die Gruppen.
 *
 */

var strToNum = function(numStr, pos){
  var res;
  if(numStr && numStr.length > pos){
    res = parseFloat(numStr[pos]);
  } else {
    res = NaN;
  }
  return res;
};

/**
 * Entfernt einfach alle whitespaces im String
 */
var vlTrim = function(str) {
    return str.replace(/\s/g, "");
};

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

  return strToNum(regex.exec(s), 2);
};
exports.extractVM212DCR =  extractVM212DCR;

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

    return strToNum(regex.exec(vlTrim(s)), 1);
};
exports.extractFRS =  extractFRS;

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
    return strToNum(regex.exec(s), 2);
}
exports.extractMKSCDG = extractMKSCDG;

/**
 * Extrahiert Float-Zahl aus String welcher vom Temperaturnormal
 * F250 geliefert wird
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractF250(s) {
  var regex = /^(A\s)([2-3]{2}\.?[0-9]{2,3})(C\r\n)$/;

  return strToNum(regex.exec(s),2);
}
exports.extractF250 = extractF250;

/**
 * Extrahiert Float-Zahl aus String wie von
 * Atmion IG (z.B. SE1) gesendet
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractAtmion(s) {
  var regex = /^(0,\t)([0-9]{1}\.?[0-9]{4}[Ee][-+][0-9]{2})(\r)$/;

  return strToNum(regex.exec(s), 2);
}
exports.extractAtmion = extractAtmion;

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

  return strToNum(regex.exec(s), 1);

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
  return strToNum(regex.exec(s), 1);
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

  return strToNum(regex.exec(s), 1);

}
exports.extractKeithleyTemp = extractKeithleyTemp;

/**
 * Extrahiert Float-Zahl aus AxTRAN Antwort
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */

function extractAxtran(s) {
  var regex = /^([0-9]{1}\.?[0-9]{1,2}[E][-+][0-9]{2})/;

  return strToNum(regex.exec(s), 1);
}
exports.extractAxtran = extractAxtran;

/**
 * Extrahiert Float-Zahl aus IM540 Antwort
 * Achtung: IM540 im IM520 Mode betreiben
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */

function extractIm540(s) {
  var regex = /^(MES\sR\rMBAR\s)([0-9]{1}\.?[0-9]{1,2}[E][-+][0-9]{2})(\r\n)$/;

  return strToNum(regex.exec(s), 2);
}
exports.extractIm540 = extractIm540;

/**
 * Extrahiert Float-Zahl aus SRG-3 Antwort
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */

function extractSRG3(s) {
  var regex = /^([\s]?)([0-9]{1}\.?[0-9]{4}[E][-+][0-9]{2})([\s]?\r\n\>)$/;

  var n = strToNum(regex.exec(s), 2)

  return n == 0 ? NaN: n;

}
exports.extractSRG3 = extractSRG3;


/**
 * Testet, ob sich der übergebene Parameter in eine Zahl wandeln lässt. Siehe auch:
 * http://stackoverflow.com/questions/18082/validate-numbers-in-javascript-isnumeric
 *
 * @author wactbprot
 * @param n String Zahlen-String
 * @return Boolean true, wenn Wandlung in Zahl erfolgreich war.
 */
function isNumber(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}
exports.isNumber = isNumber;

/**
 *
 * Funktion erzeugt die üblich gewordene
 * Type-,  Value-, Unit- (Comment-) Struktur.
 *
 * @author wactbprot
 * @param t String  Type
 * @param v Number|Array  Value
 * @param u String  Unit
 * @param c String  Comment
 * @return Object vaclab-Struktur
 *
 */
function vlRes(t, v, u, c) {
    var res = {
  'Type': t,
  'Value': v,
  'Unit': u
    };
    if (c) {
  res.Comment = c;
    }
    return res;
}
exports.vlRes = vlRes;

/**
 *
 * Funktion gibt Status der Ventile an SE1 zurück.
 * Es muss für die toString Wandlung eine genügende
 * Anzahl von Bits sichergestellt werden (2^32 = 4294967296:
 * 100000000000000000000000000000000) damit V[pos]
 * sicher funktioniert (pos ändert sich bei führenden 0en).
 *
 * @author wactbprot
 * @param hexstr String Ventilrückmeldung
 * @param valve String Ventilbezeichnung
 * @return Object mit {'Valve_closed': true| false}
 *
 */
function se1ValveClosed(hexStr,valve) {

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
exports.se1ValveClosed = se1ValveClosed;
