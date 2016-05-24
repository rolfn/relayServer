//
// TODO (RN): Überlegen, ob ggf. eines der Pakete geladen werden sollte:
//
// * https://github.com/jstat/jstat
// * https://github.com/pseudosavant/psMathStats
//

var misc = require('./relay-add-MISC.js');

/**
 * Berechnet Mittelwert und Standardabweichung
 * eines gegebenen Vectors (bzw. Arrays).
 *
 *
 * @author wactbprot
 * @param x Array Datenreihe
 * @return res Object res.mv (Mittelwert) res.sd (Standardabweichung) und re.N (Länge)
 */
function vlStat(x) {

  var res = {N: NaN,
             mv:NaN,
             sd:NaN};
  if (x) {
    var ck = misc.checkNumArr(x);
    if(ck.Arr.length > 2){
      var y      = ck.Arr,
          mv     = 0,
          sdhelp = 0,
          n      = y.length;

      mv = y.reduce(function(a, b) {
           return a + b;
           }) / n;
      res.mv = mv;
      res.N = n;
      y.map(function(i) {
        sdhelp += Math.pow((i - mv), 2);
    });

      res.sd = Math.sqrt(1 / (n - 1) * sdhelp);
    }
    return res;
  }
}
exports.vlStat = vlStat;


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
          vec = misc.rmByIndex(vec, [l]);
          t = misc.rmByIndex(t, [l]);
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
	var ret      = {},
        sumX     = 0,
        XArr     = [],
        sumY     = 0,
        YArr     = [],
        remainN  = 0,
        SSxy     = 0,
        SSxx     = 0,
        SSyy     = 0;
	for (var i = 0; i < y.length; i++) {
	    if (misc.isNumber(y[i]) && misc.isNumber(x[i])) {
		sumX = sumX + x[i];
		XArr.push(x[i]);
		sumY = sumY + y[i];
		YArr.push(y[i]);
		remainN++;
	    }
	}
	var mvX = sumX / remainN;
	var mvY = sumY / remainN;
	for (var j = 0; j < YArr.length; j++) {
	    SSxy = SSxy + (XArr[j] - mvX) * (YArr[j] - mvY);
	    SSxx = SSxx + Math.pow(XArr[j] - mvX, 2);
	    SSyy = SSyy + Math.pow(YArr[j] - mvY, 2);
	}
	ret.remainN = remainN;
	ret.min = Math.min.apply(null, 	YArr);
	ret.max = Math.max.apply(null, 	YArr);
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
