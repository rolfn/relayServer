
/**
 * Wandelt DCF77 String in ms seit 1970
 *
 * @author wactbprot
 * @param  String str String mit enthaltener Zahl.
 * @return Number Zahl.
 */
function extractDcf77(s) {
  var regex = /D:([0-9\.]*);T:[0-9];U:([0-9\.]*);.\s/
    , yy    = new Date().getFullYear()
    , r     = regex.exec(s)
  if(r != null){
    var D     = r[1].split(".")
      , U     = r[2].split(".")
      , ds    = new Date(yy + "-" +
                        D[1] +"-" +
                        D[0] +" " +
                        U[0] +":" +
                        U[1] +":" +
                        U[2]);
    return ds.getTime();
  }else{
    return null;
  }
}
exports.extractDcf77 = extractDcf77;

