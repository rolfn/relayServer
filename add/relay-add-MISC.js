
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

// TODO: Statt: "@param t String  Type" Besser: "@param {string} t Type"
// --> JSDoc3

 /**
 *
 * Funktion erzeugt die üblich gewordene
 * Type-,  Value-, Unit- (Comment-) Struktur.
 * Struktur wird mit SdValue und N erweitert.
 *
 * @author wactbprot
 * @param t String  Type
 * @param v Number | Array  Value
 * @param u String  Unit
 * @param c String  Comment
 * @return Object vaclab-Struktur
 *
 */
function vlRes(t, v, u, c, s, n) {
  var res = {'Type': t,
             'Value': v,
             'Unit': u
            };
  if (c) {
    res.Comment = c;
  }
  if (s || isNaN(s) || isNumber(s)) {
    res.SdValue = s;
  }
  if (n || isNaN(s) || isNumber(s)) {
    res.N = n;
  }
    return res;
}
exports.vlRes = vlRes;

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
exports.strToNum = strToNum;

/**
 * Entfernt einfach alle whitespaces im String
 */
var vlTrim = function(str) {
    return str.replace(/\s/g, "");
};
exports.vlTrim = vlTrim;

/**
 * Testet Array auf numerische Einträge.
 * Indizes nicht-numerischer Einträge landen
 * in res.Skip
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
    for (var i=0; i < arr.length; i++) {
      if (isNumber(arr[i])) {
        res.Arr.push(arr[i]);
      }
      else {
        res.Skip.push(i);
      }
    };
    return res;
  }
}
exports.checkNumArr = checkNumArr;

/**
 * Entfernt Einträge aus einer Datenreihe (array).
 * Bem.: Bie alte splice methode funktioniert plötzlich
 * im _. relay-Kontext nicht mehr; Tests in der
 * node-Umgebung (auf Kommandozeile) verhalten sich
 * erwartungsgemäß (deshalb diese plumpere Umsetzung)
 *
 * @author wactbprot
 * @param Arr Array Datenreihe
 * @param Idx Integer "skip" Index
 * @return res Array resultierendes Array
 */
function rmByIndex(Arr, Idx) {
  narr = [];
  for (var i=0; i < Arr.length; i++) {
    if(Idx.indexOf(i) == -1){
        narr.push(Arr[i]);
    }
  }
  return narr;
}
exports.rmByIndex = rmByIndex;
