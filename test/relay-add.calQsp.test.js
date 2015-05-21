var assert = require("assert")
  , _      = require("underscore")
  , add    = require("../relay-add.js");

describe('relay-add', function(){
  describe('#calQsp()', function(){
    it('should handle NaN psoll', function(){
      var res = add.calQsp(NaN, 0.1);

      assert.equal(res.pfill_ok, false);
      assert.equal(res.sp1, 0);
      assert.equal(res.sp2, 0);
    });

    it('should handle NaN pist', function(){
      var res = add.calQsp(0.1, NaN);

      assert.equal(res.pfill_ok, false);
      assert.equal(res.sp1, 0);
      assert.equal(res.sp2, 0);
    });

  });
});