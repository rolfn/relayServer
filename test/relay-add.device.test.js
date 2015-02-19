var assert = require("assert")
  , _      = require("underscore")
  , add    = require("../relay-add.js");

describe('relay-add.Device', function(){
  describe('#extractFRS', function(){
    it('should return clean numbers or NaN', function(){

      assert.equal( add.extractFRS("0.024380 lb \r\n"),0.02438);
      assert.equal( add.extractFRS("+ 0.929080 lb \r\n"), 0.92908);
      assert.equal( add.extractFRS("+\n \r\n 0.929078 lb \r\n"),0.929078);
      assert.equal( add.extractFRS("+ 0.929076 lb "),0.929076);
      assert.equal( add.extractFRS("+ 0.929076 lb \r\n\n+ 0.929076 lb \r\n+ 0.929076 lb \r\n"),0.929076);
      assert.equal( add.extractFRS("+ 0.929076 lb \r\n+ 0.929074 lb \r\n"),0.929076);
      assert.equal( add.extractFRS("+10.929076 lb \r\n+ 0.929074 lb \r\n"),10.929076);
      assert.equal( add.extractFRS("+ 0.929074 lb \r\n+ 0.929074 lb \r\n"),0.929074);
      assert.equal( add.extractFRS("  0.000000 lb \r\n\n  0.000000 lb \r\n"),0);
      assert.equal( add.extractFRS("  0.000000 lb \r\n"),0);
      assert.equal( add.extractFRS("  0.00000\n0 lb \r\n"),0);
      assert.equal( add.extractFRS("  0.000000 lb \r\n\n  0.000000 lb \r\n  0.000000 lb \r\n"),0);
      assert.equal( add.extractFRS("+ 0.000000 lb \r\n  0.000000 lb \r\n"),0);
      assert.equal( add.extractFRS("- 0.000000 lb \r\n  0.000000 lb \r\n"),0);

      assert.equal(_.isNaN( add.extractFRS("+ 0.92900.929074 lb \r\n")),true);
      assert.equal(_.isNaN( add.extractFRS("+929074 lb \r\n+ 0.929074 lb \r\n")), true);
    });
  });


  describe('#extractSRG3', function(){
    it('should return clean numbers or NaN', function(){
      assert.equal( _.isNaN(add.extractSRG3("?")), true);
      assert.equal( add.extractSRG3(' 1.1110E-06 \r\n>'), 1.1110E-06);

    });
  });

  describe('#extractKeithleyTemp', function(){
    it('should return clean numbers or NaN, returned string should have sign', function(){
      assert.equal( _.isNaN(add.extractKeithleyTemp("+1.13830698E+00VDC,1.13830698E+00+9.9E37SECS,+9571748RDNG#\n")), true);
      assert.equal( _.isNaN(add.extractKeithleyTemp("2.37396679E+01,2.37396679E+01+9.9E37SECS,+9571749RDNG#\n")), true);

      assert.equal( add.extractKeithleyTemp("+2.37396679E+01,2.37396679E+01+9.9E37SECS,+9571749RDNG#\n"), 2.37396679E+01);
      assert.equal( add.extractKeithleyTemp("-2.37396679E+01,2.37396679E+01+9.9E37SECS,+9571749RDNG#\n"), -2.37396679E+01);
    });
  });

  describe('#extractKeithleyVolt', function(){
    it('should return clean numbers or NaN, returned string should have sign', function(){
      assert.equal( _.isNaN(add.extractKeithleyVolt("-1.77311995E-05,+1210.560SECS,+09883RDNG#\n")), true);
      assert.equal( _.isNaN(add.extractKeithleyVolt("1.77311995E-05,+1210.560SECS,+09883RDNG#\n")), true);

      assert.equal( add.extractKeithleyVolt("-1.80353454E-05VDC,+1210.666SECS,+09884RDNG#\n"), -1.80353454E-05);
      assert.equal( add.extractKeithleyVolt("+1.80353454E-05VDC,+1210.666SECS,+09884RDNG#\n"), 1.80353454E-05);
    });
  });

  describe('#extractVM212DCR', function(){
    it('should return clean numbers or NaN', function(){
      assert.equal( _.isNaN(add.extractVM212DCR(" MBAR +3.4492E-05\n")), true);
      assert.equal( _.isNaN(add.extractVM212DCR("+3.4492E-05\n")), true);
      assert.equal( _.isNaN(add.extractVM212DCR("+3.4492E05\n")), true);
      assert.equal( _.isNaN(add.extractVM212DCR("+3.44.92E05\n")), true);
      assert.equal( _.isNaN(add.extractVM212DCR("+3.44.92\n")), true);

      assert.equal( add.extractVM212DCR(" DCR  +3.4540E-05\n"),3.4540E-05);
      assert.equal( add.extractVM212DCR(" DCR  -3.4540E-05\n"),-3.4540E-05);
    });
  });

  describe('#extractF250', function(){
    it('should return clean numbers or NaN', function(){
      assert.equal( _.isNaN(add.extractF250("A123.234C\r\n")),true);
      assert.equal( _.isNaN(add.extractF250("A23.234C\r\n")),true);
      assert.equal( _.isNaN(add.extractF250("A23.234\r\n")),true);
      assert.equal( _.isNaN(add.extractF250("A23.234\r")),true);
      assert.equal( _.isNaN(add.extractF250("23.234\r")),true);
      assert.equal( _.isNaN(add.extractF250("234\r")),true);

      assert.equal( add.extractF250("A 23.234C\r\n"),23.234);
      assert.equal( add.extractF250("A 33.234C\r\n"),33.234);


    });
  });

  describe('#extractAtmion', function(){
    it('should return clean numbers or NaN', function(){

      assert.equal( _.isNaN(add.extractAtmion("0,9600E-09\r")),true);
      assert.equal( _.isNaN(add.extractAtmion("\t0,9600E09\r")),true);
      assert.equal( _.isNaN(add.extractAtmion("0,\t0.9600E09\r")),true);

      assert.equal( add.extractAtmion("0,\t1.9600E-09\r"),1.9600E-09);

    });
  });

  describe('#extractMKSCDG', function(){
    it('should return clean numbers or NaN', function(){

      assert.equal( _.isNaN(add.extractMKSCDG("MEASURIN3")),true);
      assert.equal( _.isNaN(add.extractMKSCDG("MEASURING 290.67E-3")),true);
      assert.equal( _.isNaN(add.extractMKSCDG("MEASURING 90.64E-3")),true);
      assert.equal( _.isNaN(add.extractMKSCDG("MEASURING  290")),true);

      assert.equal( add.extractMKSCDG("MEASURING  .05"),0.05);
      assert.equal( add.extractMKSCDG("MEASURING  290.63E-3"), 290.63E-3);

    });
  });

  describe('#se1ValveClosed', function(){
    it('open close??', function(){

      var v6zu  = "00310EFE0E\r";
      var v6auf = "00112EFE2E\r";

      assert.equal( add.se1ValveClosed(v6auf).Valve_closed, false);
      assert.equal( add.se1ValveClosed(v6zu).Valve_closed, false);

    });
  });

  describe('#extractIm540', function(){
    it('should return clean numbers or NaN', function(){

      assert.equal( _.isNaN(add.extractIm540("BAR 7.50E-08\r\n")),true);
      assert.equal( _.isNaN(add.extractIm540("MES R\rMBAR 750E-08\r\n")),true);

      assert.equal( add.extractIm540("MES R\rMBAR 7.49E-08"), 7.49E-08);

    });
  });

  describe('#extractCombi', function(){
    it('should return clean numbers or NaN', function(){

      assert.equal( _.isNaN(add.extractCombi(" 2: MBAR  0.  E-03   \r")),true);
      assert.equal( _.isNaN(add.extractCombi(" 2: MBAR    E-03   ")), true);
      assert.equal( _.isNaN(add.extractCombi("BAR  6.75E-01   \r")), true);

      assert.equal( add.extractCombi(" 1: MBAR  6.75E-01   \r"), 6.75E-01);

    });
  });

});
