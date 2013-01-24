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
 */

/**
 * Berechnet, in Abhängigkeit von Ziel- und Istdruck
 * den aktuellen Sollfluß für die FM3 Fülldruckeinstellung.
 *
 *
 *
 * @param psoll Number Solldruck in mbar
 * @param psoll Number Istdruck in mbar
 * @param Vopen Number kleines oder großes Volumen
 * @return Object Zielfluß bzw Setpoint für Regler 1&2
 */
function fm3CalQsp(psoll, pist, Vopen) {
    if (psoll && pist && typeof Vopen == "boolean") {
        var ret = {},
        pfill_ok = false,               // Fülldruck ok
        mq = Vopen ? 0.0133 : 0.0155, // experimentall best. Steigungen
        ts = 10,                      // Sollzeit
        bord = 0.8,                   // Start Regelung rel. Abw. von psoll
        sscbord = 2,                  // Start 2. Regler
        eps = 0.005                   // Ende Regelung rel. Abw. von psoll
        md = 1,                       // Dämpf./verst. der Regel.
        ret.dp = Math.abs(psoll / pist - 1);
        q = psoll / ts / mq;
        f = md * ret.dp / bord;
        if (typeof ret.dp == "number") {
            // Gas
            if (ret.dp > bord) {
                if (q && q < 2) {
                    ret.sp1 = q;
                    ret.sp2 = 0;
                }
                else {
                    ret.sp1 = q / 100;
                    ret.sp2 = q;
                }
            };
            // Kupplung
            if (ret.dp <= bord) {
                ret.pfill_ok = false;
                if (q * f && q * f < 2) {
                    ret.sp1 = q * f;
                    ret.sp2 = q * f / 100;
                }
                else {
                    ret.sp1 = q * f / 100;
                    ret.sp2 = q * f;
                }
            };
            // Bremse
            if (ret.dp < eps || pist > psoll) {
                ret.pfill_ok = true,
                ret.sp1 = 0;
                ret.sp2 = 0;
            }
            return ret;
        }
    }
}
exports.fm3CalQsp = fm3CalQsp;


/**
 * Berechnet Mittelwert und Standardabweichung
 * eines gegebenen Vectors (bzw. Arrays).
 *
 *
 *
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
        res.sd = sd
        return res;
    }
};
exports.vlStat = vlStat;


/**
 * Testet Array auf numerische Einträge und sortiert ggf. aus
 *
 *
 *
 * @param arr Array Datenreihe
 * @return res Object   res.Arr "sauberes" Array, res.Skip Indizes der verworfenen Einträge
 */
function checkNumArr(arr) {
    if (arr && Array.isArray(arr)) {
        var res = {};
        res.Arr = [],
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
};
exports.checkNumArr = checkNumArr;

/**
 * Entfernt Einträge aus einer Datenreihe.
 *
 *
 *
 * @param arr Array Datenreihe
 * @param arr Integer "skip" Index
 * @return res Array resultierendes Array
 */
function rmByIndex(Arr, Idx) {
    Idx.map(function(i) {
        Arr.splice(i, 1);
    });
    return Arr
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
 *
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
        t.push((tstart[k] + tstop[k]) / 2)
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
};
exports.vlSlope = vlSlope;

/**
 * Reine Statistikfunktion zur Berechnung der Parameter der
 * linearen Regression x~y.
 *
 *
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
            };
        };
        mvX = sumX / remainN;
        mvY = sumY / remainN;
        for (var j = 0; j < YArr.length; j++) {
            SSxy = SSxy + (XArr[j] - mvX) * (YArr[j] - mvY);
            SSxx = SSxx + Math.pow(XArr[j] - mvX, 2);
            SSyy = SSyy + Math.pow(YArr[j] - mvY, 2);
        };
        ret.remainN = remainN
        ret.mvX = mvX
        ret.mvY = mvY
        ret.bx = SSxy / SSxx;
        ret.by = SSxy / SSyy;
        ret.R = (SSxy * SSxy) / (SSxx * SSyy);
        ret.Cx = mvY - ret.bx * mvX
        return ret
    }
}
exports.slope = slope;

/**
 * Extrahiert Float-Zahl aus String mit Pre- und Postfix. Die Float-Zahl kann
 * Vorzeichen bei Mantisse oder Exponent enthalten. Pre- und Postfix können
 * auch leer sein. Im Fehlerfall wird Number.NaN geliefert. Siehe auch:
 *    http://www.regular-expressions.info/floatingpoint.html
 * <pre>
 * Beispiele: "MEASURING     -1.13E-3 BLAFASEL" --> -0.00113
 *            "MEASURING .4711"                 -->  0.4711
 * </pre>
 *
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractValue(s) {
    var regex = /^(\w*\s*)([-+]?[0-9]*\.?[0-9]+)([eE][-+]?[0-9]+)?(\s*\w*)$/;
    return parseFloat(s.replace(regex, "$2$3"));
}
exports.extractValue = extractValue;

/**
 * Extrahiert Float-Zahl aus String s.relay-add-test.js.
 *
 *
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractF250(s) {
    var regex = /^(A\s)([2-3]{2}\.?[0-9]{2,3})(C\r\n)$/
        return parseFloat(s.replace(regex, "$2"));
}
exports.extractF250 = extractF250

/**
 * Extrahiert Float-Zahl aus String s.relay-add-test.js.
 *
 *
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */

function extractAtmion(s) {
    var regex = /^(0,\t)([0-9]{1}\.?[0-9]{4}[Ee][-+][0-9]{2})(\r)$/
        return parseFloat(s.replace(regex, "$2"));
}
exports.extractAtmion = extractAtmion

/**
 * Extrahiert Float-Zahl aus String s.relay-add-test.js.
 *
 *
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */

function extractKeithley(s) {
    var regex = /^([0-9]{1}\.?[0-9]{1,8}[Ee][-+][0-9]{2})/
        return parseFloat(s.replace(regex, "$1"));
}
exports.extractKeithley = extractKeithley

/**
 * Testet, ob sich der übergebene Parameter in eine Zahl wandeln lässt. Siehe auch:
 * http://stackoverflow.com/questions/18082/validate-numbers-in-javascript-isnumeric
 *
 *
 * @param n String Zahlen-String
 * @return Boolean true, wenn Wandlung in Zahl erfolgreich war.
 */
function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
};
exports.isNumber = isNumber

/**
 *
 * Funktion erzeugt die üblich gewordene
 * Type-,  Value-, Unit- (Comment-) Struktur.
 *
 *
 * @param t String  Type
 * @param v Number|Array  Value
 * @param u String  Unit
 * @param c String  Comment
 * @return Object vaclab-Struktur
 *
 */
function vlRes(t, v, u, c) {
    res = {
        'Type': t,
        'Value': v,
        'Unit': u
    }
    if (c) {
        res.Comment = c
    }
    return res
};
exports.vlRes = vlRes;

/**
 *
 * Funktion gibt Status der Ventile an SE1 zurück.
 * Es muss für die toString Wandlung eine genügende
 * Anzahl von Bits sichergestellt werden (2^32 = 4294967296:
 * 100000000000000000000000000000000) damit V[pos]
 * sicher funktioniert (pos ändert sich bei führenden 0en).
 *
 *
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
       V1:8,
      },
    num = parseInt(hexStr,16) + BN,
    pat = num.toString(2).split('');

    return {'Valve_closed': pat[V[valve]] == '1',
            'Valve_opened': pat[V[valve]] == '0' };

};
exports.se1ValveClosed = se1ValveClosed;
