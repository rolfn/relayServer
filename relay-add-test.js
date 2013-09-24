#!/usr/bin/env node

var add =require("./relay-add.js");

/**
 * Test der extractKeithleyTemp  function
 */
s = [
   "+1.13830698E+00VDC,1.13830698E+00+9.9E37SECS,+9571748RDNG#\n",
   "+2.37396679E+01,2.37396679E+01+9.9E37SECS,+9571749RDNG#\n",
   "+2.37396679E+01,2.37396679E+01+9.9E37SECS,+9571749RDNG#\n",
   "+2.37435799E+01,2.37435799E+01+9.9E37SECS,+9571750RDNG#\n",
   "+2.37435799E+01,2.37435799E+01+9.9E37SECS,+9571750RDNG#\n",
   "+2.37483959E+01,2.37483959E+01+9.9E37SECS,+9571751RDNG#\n",
   "+2.37483959E+01,2.37483959E+01+9.9E37SECS,+9571751RDNG#\n",
   "+2.37514629E+01,2.37514629E+01+9.9E37SECS,+9571752RDNG#\n",
   "+2.37514629E+01,2.37514629E+01+9.9E37SECS,+9571752RDNG#\n",
   "+2.37530746E+01,2.37530746E+01+9.9E37SECS,+9571753RDNG#\n"
];
console.log("---------------extractKeithleyTemp-------------");
console.log(s.map(add.extractKeithleyTemp));

/**
 * Test der extractKeithleyVolt  function
 */
var s = [ '-1.77311995E-05,+1210.560SECS,+09883RDNG#\n',
	  '-1.80353454E-05VDC,+1210.666SECS,+09884RDNG#\n',
	  '-1.80762017E-05VDC,+1210.878SECS,+09886RDNG#\n',
	  '-1.82509721E-05VDC,+1210.985SECS,+09887RDNG#\n',
	  '-1.82509721E-05VDC,+1210.985SECS,+09887RDNG#\n',
	  '-1.77675156E-05VDC,+1211.091SECS,+09888RDNG#\n',
	  '-1.76063622E-05VDC,+1211.408SECS,+09890RDNG#\n',
	  '-1.76040921E-05VDC,+1211.514SECS,+09891RDNG#\n',
	  '-1.79604449E-05VDC,+1211.620SECS,+09892RDNG#\n',
	  '-1.81658579E-05VDC,+1211.726SECS,+09893RDNG#\n',
	  '-1.81454288E-05VDC,+1211.939SECS,+09895RDNG#\n',
	  '-1.81454288E-05VDC,+1211.939SECS,+09895RDNG#\n',
	  '-1.78639802E-05VDC,+1212.046SECS,+09896RDNG#\n',
	  '-1.76460835E-05VDC,+1212.258SECS,+09897RDNG#\n',
	  '-1.72091550E-05VDC,+1212.470SECS,+09899RDNG#\n',
	  '-1.79309372E-05VDC,+1212.576SECS,+09900RDNG#\n',
	  '-1.80308070E-05VDC,+1212.683SECS,+09901RDNG#\n',
	  '-1.78140453E-05VDC,+1212.789SECS,+09902RDNG#\n',
	  '-1.72182336E-05VDC,+1212.895SECS,+09903RDNG#\n',
	  '-1.81261366E-05VDC,+1213.002SECS,+09904RDNG#\n' ];

console.log("---------------extractKeithleyVolt-------------");
console.log(s.map(add.extractKeithleyVolt));

/**
 * Test der extractF250  function
 */
var s = ["A 23.234C\r\n","A 23.23C\r\n", "A23.45C","A 23.23"];
console.log("---------------extractF250-------------");
console.log(s.map(add.extractF250));

/**
 * Test der extractAtmion  function
 */
var s = ['0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r',
  '0,\t1.9600E-09\r' ];
var _vec = s.map(add.extractAtmion);
console.log("---------------extractAtmion-------------");
console.log(_vec);
_ret =add.checkNumArr(_vec);
console.log(_ret);

/**
 * Test der vlStat function
 */

var arr =  [1.14223873,
            0.01283644,
            -0.45056385,
            1.17646101,
            0.30347168 ,
            0.01957568,
            -1.53945684 ,
            1.77889768,
            -1.39850969,
            -0.24774159];
console.log("---------------vlStat-------------");
console.log(add.vlStat(arr));


var arr =  [1.14223873,
            '',
            -0.45056385,
            1.17646101,
            0.30347168 ,
            0.01957568,
            'c' ,
            1.77889768,
            -1.39850969,
            -0.24774159];

console.log(arr);
console.log(add.checkNumArr(arr));


/**
 * ergibt:
 * { mv: 0.07972092500000003, <<-- 1
 * N: 10,
 * sd: 1.078706836758906 }    <<-- 2
 *
 *R liefert:
 * >  arr <- c(1.14223873 , 0.01283644 ,-0.45056385 , 1.17646101,
 *             0.30347168 , 0.01957568 , -1.53945684  ,1.77889768,
 *            -1.39850969, -0.24774159)
 * > sd(arr)
 * [1] 1.078707                <<-- 2
 * > mean(arr)
 * [1] 0.07972093              <<-- 1
 */

/**
 * Test der Funktion slope
 *
 **/

var raw_vec = [ 'MEASURING  290.64E-3',
		'MEASURIN3',
		'MEASURING 290.67E-3',
		'MEASURING  290',
		'MEASURING  290.65E-3',
		'MEASURING  90.64E-3',
		'MEASURING  290.63E-3',
		'MEASURING  290.64E-3',
		'MEASURING  290.64E-3',
		'MEASURING  290.65E-3',
		'MEASURING  290.67E-3',
		'MEASURING  290.65E-3',
		'MEASURING  290.70E-3',
		'MEASURING  290.64E-3',
		'MEASURING  290.62E-3',
		'MEASURING  290.68E-3',
		'MEASURING  290.63E-3',
		'MEASURING  290.67E-3',
		'MEASURING  290.69E-3',
		'MEASURING  290.69E-3' ],
t_start = [ 1348666058346,
	    1348666059342,
	    1348666060345,
	    1348666061059,
	    1348666062062,
	    1348666063064,
	    1348666064065,
	    1348666065069,
	    1348666066072,
	    1348666067075,
	    1348666068077,
	    1348666069080,
	    1348666070082,
	    1348666071084,
	    1348666072087,
	    1348666073095,
	    1348666074099,
	    1348666075102,
	    1348666076103,
	    1348666077106 ],
t_stop = [ 1348666058399,
	   1348666059377,
	   1348666060379,
	   1348666061091,
	   1348666062094,
	   1348666063096,
	   1348666064098,
	   1348666065124,
	   1348666066115,
	   1348666067107,
	   1348666068113,
	   1348666069112,
	   1348666070135,
	   1348666071117,
	   1348666072119,
	   1348666073127,
	   1348666074135,
	   1348666075139,
	   1348666076145,
	   1348666077140 ];

console.log("-------- extractMKSCDG -----------");
 var vec = raw_vec.map(add.extractMKSCDG);
console.log(vec);
console.log("---------------vlslope-------------");
console.log(add.vlSlope(vec,t_start,t_stop));
console.log("---------------------------------");

var v6zu  = '00310EFE0E\r';
var v6auf = '00112EFE2E\r';

console.log("se1ValveClosed");
console.log("zu");
console.log(add.se1ValveClosed(v6zu, "V6"));
console.log("auf");
console.log(add.se1ValveClosed(v6auf, "V6"));



/**
 * test der extractIM540 function
 */

s = ['MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.49E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n',
     'MES R\rMBAR 7.50E-08\r\n'];


console.log("extractIm540");
console.log(s.map(add.extractIm540));
