var assert    = require("assert")
  , http      = require("http")
  , _         = require("underscore")
  , hlp       = require("./hlp.js")
  , testhost  = process.env.TESTHOST;

describe('test of relayServer TCP functionality', function(){

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


  describe('#Action:TCP', function(){
    it('should connect to Corvus_1 (e75468)', function(done){

      var task = {"Action":"TCP" ,
                  "VxiTimeout": 0,
                  "Host": "e75468",
                  "Port": 23,
                  "Value": "status\r"};

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

  describe('#Action:TCP', function(){
    it('should connect to Corvus_2 (e75469)', function(done){

      var task = {"Action":"TCP" ,
                  "VxiTimeout": 0,
                  "Host": "e75469",
                  "Port": 23,
                  "Value": "status\r"};

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

  describe('#Action:TCP', function(){
    it('should connect to MKS Flow Controller SE1/CE3/FM3 (e75491)', function(done){

      var task = {"Action":"TCP" ,
                  "VxiTimeout": 0,
                  "Host": "e75491",
                  "Port": 10002,
                  "Value": "?ID\r"};

      var req = hlp.req( function(d){
                  var data = JSON.parse(d);
                  assert.equal(_.isObject(data) , true);
                  assert.equal(_.isString(data.Result) , true);
                  assert.equal(data.Result.substring(0, 2) , "PR");

                  done()
                });

      req.write(JSON.stringify(task));
      req.end();

    });
  });

});