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

      assert.equal( add.extractF250("A  22.79C\r\n"),22.79);

    });
  });
 describe('#extractPhillipsTemp', function(){
    it('should return clean numbers or NaN', function(){

      assert.equal( _.isNaN(add.extractPhillipsTemp("VDC    0.0001\n")),true);

      assert.equal( add.extractPhillipsTemp("TDC     +022.80E+00\n"), 22.8);

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
    it('should return clean numbers or NaN; test 1', function(){
      assert.equal( _.isNaN(add.extractIm540("BAR 7.50E-08\r\n")),true);
    });
  });

  describe('#extractIm540', function(){
    it('should return clean numbers or NaN; test 2', function(){
      assert.equal( _.isNaN(add.extractIm540("MES R\rMBAR 750E-08\r\n")),true);
    });
  });

  describe('#extractIm540', function(){
    it('should return clean numbers or NaN; test 3', function(){

      assert.equal( add.extractIm540("MES R\rMBAR 7.49E-08\r\n"), 7.49E-08);

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

  describe('#extractKeithleyTempScan', function(){
    it('should return mean value by channel key', function(){

      var res = add.extractKeithleyTempScan({"0":"+2.25772018E+01_C,+0.000SECS,+00000RDNG#,"
                                                + "+2.25894833E+01_C,+0.469SECS,+00001RDNG#,"
                                                + "+2.25676708E+01_C,+0.938SECS,+00002RDNG#,"
                                                + "+2.27207241E+01_C,+1.407SECS,+00003RDNG#,"
                                                + "+2.25786743E+01_C,+1.876SECS,+00004RDNG#,"
                                                + "+2.25920391E+01_C,+2.450SECS,+00005RDNG#,"
                                                + "+2.25677280E+01_C,+2.919SECS,+00006RDNG#,"
                                                + "+2.27227287E+01_C,+3.388SECS,+00007RDNG#,"
                                                + "+2.25797749E+01_C,+3.857SECS,+00008RDNG#,"
                                                + "+2.25934544E+01_C,+4.326SECS,+00009RDNG#\n",
                                             "1":"+2.25772018E+01_C,+0.000SECS,+00000RDNG#,"
                                                + "+2.25894833E+01_C,+0.469SECS,+00001RDNG#,"
                                                + "+2.25676708E+01_C,+0.938SECS,+00002RDNG#,"
                                                + "+2.27207241E+01_C,+1.407SECS,+00003RDNG#,"
                                                + "+2.25786743E+01_C,+1.876SECS,+00004RDNG#,"
                                                + "+2.25920391E+01_C,+2.450SECS,+00005RDNG#,"
                                                + "+2.25677280E+01_C,+2.919SECS,+00006RDNG#,"
                                                + "+2.27227287E+01_C,+3.388SECS,+00007RDNG#,"
                                                + "+2.25797749E+01_C,+3.857SECS,+00008RDNG#,"
                                                + "+2.25934544E+01_C,+4.326SECS,+00009RDNG#\n",
                                             "2":"+2.25772018E+01_C,+0.000SECS,+00000RDNG#,"
                                                + "+2.25894833E+01_C,+0.469SECS,+00001RDNG#,"
                                                + "+2.25676708E+01_C,+0.938SECS,+00002RDNG#,"
                                                + "+2.27207241E+01_C,+1.407SECS,+00003RDNG#,"
                                                + "+2.25786743E+01_C,+1.876SECS,+00004RDNG#,"
                                                + "+2.25920391E+01_C,+2.450SECS,+00005RDNG#,"
                                                + "+2.25677280E+01_C,+2.919SECS,+00006RDNG#,"
                                                + "+2.27227287E+01_C,+3.388SECS,+00007RDNG#,"
                                                + "+2.25797749E+01_C,+3.857SECS,+00008RDNG#,"
                                                + "+2.25934544E+01_C,+4.326SECS,+00009RDNG#\n"}
                                            , "(@101:110)")


      assert.equal( res["101"].mv - 2.25772018E+01< 1e-6, true )
      assert.equal( res["102"].mv - 2.25894833E+01< 1e-6, true )
      assert.equal( res["103"].mv - 2.25676708E+01< 1e-6, true )
      assert.equal( res["104"].mv - 2.27207241E+01< 1e-6, true )
      assert.equal( res["105"].mv - 2.25786743E+01< 1e-6, true )
      assert.equal( res["106"].mv - 2.25920391E+01< 1e-6, true )
      assert.equal( res["107"].mv - 2.25677280E+01< 1e-6, true )
      assert.equal( res["108"].mv - 2.27227287E+01< 1e-6, true )
      assert.equal( res["109"].mv - 2.25797749E+01< 1e-6, true )
      assert.equal( res["110"].mv - 2.25934544E+01< 1e-6, true ) ;
    });
  });

  describe('#extractPPC', function(){
    it('should return clean numbers or NaN, returned string should have sign', function(){
	assert.equal( _.isNaN(add.extractPPC("ar/s,1013.111 mbara,0,0.1014\n16 mbar\r\n")), true);
        assert.equal( add.extractPPC("R,1014.147 mbara,0.000    mb\nar/s,1013.103 mbara,0,0.101416 mbar\r\n"), 1014.147);

	assert.equal( add.extractPPC("R,4.263    mbara,0.008    mb\nar/s,1013.404 mbara,0,0.048778 mbar\r\n"), 4.263);

    });
    it('should return 0.0', function(){
      assert.equal(add.extractPPC("R,0.000    mbara,0.008    mb\nar/s,1013.404 mbara,0,0.048778 mbar\r\n"), 0)
    });
  });


  describe('#extractMKT50', function(){
    it('should return a number', function(){
      assert.equal(add.extractMKT50("31.07.15  09:16:32\r\nR1= +108.56190 Ohm\r\nR2= not valid\r\nT1=  +21.9098 C\r\nT2= not valid\r\nSENSOR1= No:00000001\r\nSENSOR2= No:00000001\r\n"), 21.9098);
    });

    it('should return a number', function(){
      assert.equal(add.extractMKT50( '31.07.15  09:44:32\r\nR1= +108.55855 Ohm\r\nR2= not valid\r\nT1=  +21.9012 C\r\nT2= not valid\r\nSENSOR1= No:00000001\r\nSENSOR2= No:00000001\r\n'), 21.9012);
    });

    it('should return a NaN', function(){
      //      assert.equal(_.isNaN(add.extractMKT50('')), true);
    });
  });

  describe('#extractDcf77', function(){
    it('should return null (not in sync)', function(){
      assert.equal(add.extractDcf77("\u0002D:16.12.15;T:3;U:11.04.34; *  \u0003")
                  , null);
    });

    it('should return null on wrong data format', function(){
      assert.equal(add.extractDcf77(":16.12.15;T:3;U:11.04.34; *  \u0003")
                  , null);
    });

    it('should return integer (ms since 1970)', function(){
      assert.equal(add.extractDcf77("\u0002D:16.12.15;T:3;U:11.04.34;   \u0003")
                  , 1481882674000);
    });
  });
});
