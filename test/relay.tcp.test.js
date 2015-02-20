var assert    = require("assert")
  , http      = require("http")
  , _         = require("underscore")
  , hlp       = require("./hlp.js")
  , cfg       = require('../config.js')

cfg.logger = require('vlogger')();

var relay     = require("../relay.js")
   , server    = http.createServer(relay.start);

describe('test of relayServer TCP functionality', function(){

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

});