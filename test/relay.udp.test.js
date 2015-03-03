var assert    = require("assert")
  , http      = require("http")
  , _         = require("underscore")
  , hlp       = require("./hlp.js")
  , testhost  = process.env.TESTHOST;

describe('test of relayServer UDP functionality', function(){

  if(_.isUndefined(testhost)){

    var relay     = require("../relay.js")
      , server    = http.createServer(relay.start);

    before("run the server before start", function(done){
      server.listen(hlp.testport, function(){
        console.log("start& listen");
        done();
      });
    });

    after("shut down when everything is done", function(done){
      server.close(function(){
        console.log("shut down");
        done();
      });
    });
  }else{
    console.log("test installed server at: " + testhost)
  }


  describe('#Action:UDP', function(){
    it('should connect and read out PPC4', function(done){

      var task = {"Action":"UDP" ,
                  "Host": "172.30.56.30",
		  "Port": 2362,
                  "Value": "*IDN?"};
	
	var req = hlp.req( function(d){
                  var data = JSON.parse(d);
	    assert.equal(_.isObject(data) , true);
            assert.equal(_.isString(data.Result) , true);
	    
            done()
        });
	
	req.write(JSON.stringify());
	req.end();

    });
  });

});
