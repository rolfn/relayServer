var assert    = require("assert")
  , _         = require("underscore")
  , http      = require("http")
  , cfg       = require('../config.js')

cfg.logger = require('vlogger')()

var relay     = require("../relay.js")
  , testport  = 55556
  , server    = http.createServer(relay.start);

var con = {hostname: "localhost",
           port: cfg.RELAY_PORT,
           path: "/",
           method: 'POST',
           headers: {
             'Content-Type': 'application/json'
           }
          };

var  httpreq = function(con, cb){
  var req = http.request(con, function(res) {
              res.setEncoding("utf8");
              res.on("data",   cb);
              res.on("end", function() {
                console.log("req.end ");
              } );
              res.on("error", function(e) {
                console.log("res.error " + e);
              });
            });

  req.on("error", function(e) {
    console.log("req.error " + e);
  });
  return req;
};

describe('relay', function(){
  before("run the server before start", function (done) {
    server.listen(testport, function(){
      console.log("start& listen");
      done();
    });
  });
  after("shut down when everything is done", function (done) {
    server.close(function(){
      console.log("shut down");
      done();
    });
  });

  describe('#Action:VXI11', function(){
    it('should initialize digits at FM3 1T CDG MKS', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75481",
                  "Device":"gpib0,8",
                  "Value": ":digit 5.5"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);
                  assert.equal(_.isObject(data) , true);
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });


  describe('#Action:VXI11', function(){
    it('should initialize range X0.1 at FM3 1T CDG MKS', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75481",
                  "Device":"gpib0,8",
                  "Value": ":sens:scan(@1):gain X0.1"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);
                  assert.equal(_.isObject(data) , true);
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });
});
