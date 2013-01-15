
fm3CalQsp = function(psoll,pist,Vopen){

    if(psoll && pist && typeof Vopen == "boolean"){

        var ret  = {},
        pfill_ok = false, // Fülldruck ok
        mq       = Vopen ? 0.0133 : 0.0155, // experimentall best. Steigungen
        ts       = 10,    // sollzeit
        bord     = 0.8,     // start Regelung rel. Abw. von psoll
        sscbord  = 2,     // start 2. Regler
        eps      = 0.005  // ende Regelung rel. Abw. von psoll
        md       = 1,     // Dämpf./verst. der Regel.
        ret.dp   = Math.abs(psoll/pist - 1);

        q = psoll / ts / mq;
        f = md * ret.dp/bord;

        if(typeof ret.dp == "number"){
            // Gas
            if(ret.dp > bord){

                if( q && q < 2){
                    ret.sp1  = q;
                    ret.sp2  = 0;
                }else {
                    ret.sp1  = q/100;
                    ret.sp2  = q;
                }

            };

            // Kupplung
            if(ret.dp <= bord ){

                ret.pfill_ok     = false;

                if( q*f && q*f < 2){
                    ret.sp1  = q*f;
                    ret.sp2  = q*f/100;
                }else {
                    ret.sp1  = q*f/100;
                    ret.sp2  = q*f;
                }
            };

            // Bremse
            if(ret.dp < eps || pist > psoll ){

                ret.pfill_ok     = true,

                ret.sp1          = 0;
                ret.sp2          = 0;

            }
            return ret;
        }
    }
}
exports.fm3CalQsp = fm3CalQsp;

vlStat = function(x){

    if (x && x.length > 2){
        var res = {},
        mv      = 0,
        sdhelp  = 0,
        n       = x.length;

        mv = x.reduce(function(a, b){
            return a + b;
        })/n;

        res.mv = mv;
        res.N = n;

        x.map(function(i){
            sdhelp += Math.pow((i - mv),2);
        });

        sd     = Math.sqrt(1/(n-1) * sdhelp);
        res.sd = sd

        return res;
    }
};
exports.vlStat = vlStat;

checkNumArr = function(arr){
    if(arr && Array.isArray(arr)){
        var res  = {};
        res.Arr  = [],
        res.Skip = [];
        arr.map(function(v,i){
            if(isNumber(v)){
                res.Arr.push(v);
            }else{
                res.Skip.push(i);
            }
        });
        return res;
    }
};
exports.checkNumArr = checkNumArr;

rmByIndex = function(Arr, Idx){
    Idx.map(function(i){
        Arr.splice(i,1);
    });

    return Arr
}
exports.rmByIndex = rmByIndex;


/**
 * vaclab slope fn
 * - erzeugt zunächst aus den Vektoren
 *   tstart & tstop ein t
 * - versucht Ausreiser auf einfache art
 *   zu elim.
 * -- max _iter_ Punkte werden verworfen
 * -- verworfen werden Pkt., die weiter
 *    als relative _d_border_ (0.6 entsp. 60%)
 *    von der Geraden weg liegen
 */
vlSlope = function(vec, tstart, tstop){
    var  t    = [],
    rel_diff  = [],
    iter_N    = 5,
    again     = true,
    d_border  = 0.6;

    for(var k = 0; k < tstart.length; k++){
        t.push((tstart[k] + tstop[k])/2)
    }

    var hs = slope(vec,t),
    vlm    = hs.bx,
    vlc    = hs.Cx;

    for(var m = 0; m < iter_N; m++){
        if(again){
            again = false;
            for(var l = 0; l < t.length; l++){
                var predict_val = vlm * t[l] +  vlc;

                if(Math.abs((vec[l] - predict_val )/predict_val) > d_border){
                    vec    = rmByIndex(vec,[l]);
                    t      = rmByIndex(t,[l]);
                    hs     = slope(vec,t);
                    vlm    = hs.bx;
                    vlc    = hs.Cx;
                    again  = true;
                }
            }// l
        }//again
    }//m
    return slope(vec,t);
};
exports.vlSlope = vlSlope;

/**
 * reine slope fn
 *
 */
slope = function(y,x){

    if(x.length == y.length){
        var ret   = {},
        sumX     = 0,
        XArr     = [],
        sumY     = 0,
        YArr     = [],
        remainN  = 0,
        SSxy    = 0,
        SSxx    = 0,
        SSyy    = 0;

        for(var i = 0; i < y.length; i++){

            if(isNumber(y[i]) && isNumber(x[i])){
                sumX  = sumX + x[i];
                XArr.push(x[i]);

                sumY  = sumY + y[i];
                YArr.push(y[i]);
                remainN++;
            };
        };
        mvX     = sumX/remainN;
        mvY     = sumY/remainN;

        for(var j   = 0; j < YArr.length; j++){
            SSxy = SSxy + (XArr[j] - mvX) * (YArr[j] - mvY);
            SSxx = SSxx + Math.pow(XArr[j] - mvX,2);
            SSyy = SSyy + Math.pow(YArr[j] - mvY,2);
        };

        ret.remainN  = remainN
        ret.mvX      = mvX
        ret.mvY      = mvY

        ret.bx      = SSxy / SSxx;
        ret.by      = SSxy / SSyy;
        ret.R       = (SSxy * SSxy)/(SSxx * SSyy);
        ret.Cx      = mvY - ret.bx * mvX

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
 * @param str String mit Zahl.
 * @return number.
 */
extractValue = function(s) {
    var regex = /^(\w*\s*)([-+]?[0-9]*\.?[0-9]+)([eE][-+]?[0-9]+)?(\s*\w*)$/;
    return parseFloat(s.replace(regex,"$2$3"));
}

exports.extractValue = extractValue;

/**
 * http://stackoverflow.com/questions/18082/validate-numbers-in-javascript-isnumeric
 *
 */
isNumber = function(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
};
exports.isNumber = isNumber

/**
 *
 * vaclab result erzeugt die üblich gewordene
 * Type-,  Value-, Unit- (Comment-) Struktur
 *
 */
vlRes = function(t,v,u,c){
    res = {'Type'  :t,
           'Value' :v,
           'Unit'  :u }
    if(c){
        res.Comment = c
    }
    return res

};
exports.vlRes = vlRes;
