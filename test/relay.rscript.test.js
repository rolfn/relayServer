var assert    = require("assert")
  , http      = require("http")
  , _         = require("underscore")
  , hlp       = require("./hlp.js")
  , testhost  = process.env.TESTHOST;

describe('test of relayServer Rscript functionality', function(){

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

  describe('#Action:Rscript', function(){
    it('should connect to /usr/local/lib/r4vl/test', function(done){

      var task = {"Action":"/usr/bin/Rscript" ,
                  "Value": [
                    "/usr/local/lib/r4vl/test.R"
                  ]};

      var req = hlp.req( function(d){
                  var data = JSON.parse(d);
                  assert.equal(_.isObject(data) , true);
                  assert.equal(_.isString(data.Result) , true);
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();

    });
  });

  describe('#Action:Rscript', function(){
    it('should answer with error', function(done){

      var task = {"Action":"/usr/bin/Rscript" ,
                  "Value": [
                    "/usr/local/lib/r4vl/not-there.R"
                  ]};

      var req = hlp.req( function(d){
                  var data = JSON.parse(d);
                  assert.equal(_.isObject(data) , true);
                  assert.equal(_.isString(data.error) , true);
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();

    });
  });

});