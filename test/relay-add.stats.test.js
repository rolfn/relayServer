var assert = require("assert")
  , _      = require("underscore")
  , add    = require("../relay-add.js");

describe('relay-add.Stats', function(){

  describe('#vlStat', function(){
    it('should return mean (.mv), standard deviation (.sd) and length (.N)', function(){
      var arr =  [1.14223873,
                  0.01283644,
                 -0.45056385,
                  1.17646101,
                  0.30347168,
                  0.01957568,
                 -1.53945684 ,
                  1.77889768,
                 -1.39850969,
                 -0.24774159];
      // R>  inp <-        c(1.14223873,
      // R>  +                   0.01283644,
      // R>  +                  -0.45056385,
      // R>  +                   1.17646101,
      // R>  +                   0.30347168,
      // R>  +                   0.01957568,
      // R>  +                  -1.53945684 ,
      // R>  +                   1.77889768,
      // R>  +                  -1.39850969,
      // R>  +                  -0.24774159)
      // R>  > mean(inp)
      // R>  [1] 0.07972093
      // R>  > sd(inp)
      // R>  [1] 1.078707
      // R>  > length(inp)
      // R>  [1] 10
      // R>  >

      assert.equal(add.vlStat(arr).mv,  0.07972092500000003);
      assert.equal(add.vlStat(arr).sd, 1.078706836758906);
      assert.equal(add.vlStat(arr).N, 10);

      assert.equal(add.vlStat([1, NaN, 1, 1]).N, 3);
      assert.equal(add.vlStat([1, NaN, 1, 1]).mv, 1);
      assert.equal(add.vlStat([1, NaN, 1, 1]).sd, 0);

    });
  });

  describe('#vlSlope', function(){
    it('should return slope and params', function(){


 var raw_vec = [ "MEASURING  290.64E-3",
                 "MEASURIN3",
                 "MEASURING 290.67E-3",
                 "MEASURING  290",
                 "MEASURING  290.65E-3",
                 "MEASURING 90.64E-3",
                 "MEASURING  290.63E-3",
                 "MEASURING  290.64E-3",
                 "MEASURING  290.64E-3",
                 "MEASURING  290.65E-3",
                 "MEASURING  290.67E-3",
                 "MEASURING  290.65E-3",
                 "MEASURING  290.70E-3",
                 "MEASURING  290.64E-3",
                 "MEASURING  290.62E-3",
                 "MEASURING  290.68E-3",
                 "MEASURING  290.63E-3",
                 "MEASURING  290.67E-3",
                 "MEASURING  290.69E-3",
                 "MEASURING  .05"],
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

      var vec = raw_vec.map(add.extractMKSCDG)
        , res = add.vlSlope(vec,t_start,t_stop);

      assert.equal(res.remainN , 15);
      assert.equal(res.mvX     , 1348666068785.9 );
      assert.equal(res.mvY     , 0.2906533333333333);
      assert.equal(res.bx      , 1.7684955914446549e-9 );
      assert.equal(res.by      , 82117241.37926348 );
      assert.equal(res.R       , 0.14522397936082404);
      assert.equal(res.Cx      , -2384.819343645524 );

    });
  });

});
