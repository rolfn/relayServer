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
                  assert.equal(_.isString(data.Result) , true);
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });

  describe('#Action:VXI11', function(){
    it('should read value from FM3 1T CDG MKS', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75481",
                  "Device":"gpib0,8",
                  "Value": ":meas:func"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);
                  assert.equal(data.Result.substring(0, 9) , "MEASURING");
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });


  describe('#Action:VXI11', function(){
    it('should initialize digits at FM3 10T CDG MKS', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75481",
                  "Device":"gpib0,10",
                  "Value": ":digit 5.5"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);

                  assert.equal(_.isObject(data) , true);
                  assert.equal(_.isString(data.Result) , true);

                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });

  describe('#Action:VXI11', function(){
    it('should read value from FM3 10T CDG MKS', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75481",
                  "Device":"gpib0,10",
                  "Value": ":meas:func"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);
                  assert.equal(data.Result.substring(0, 9) , "MEASURING");
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });

  describe('#Action:VXI11', function(){
    it('should initialize digits at FM3 1000T CDG MKS', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75481",
                  "Device":"gpib0,9",
                  "Value": ":digit 5.5"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);

                  assert.equal(_.isObject(data) , true);
                  assert.equal(_.isString(data.Result) , true);

                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });

  describe('#Action:VXI11', function(){
    it('should read value from FM3 1000T CDG MKS', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75481",
                  "Device":"gpib0,9",
                  "Value": ":meas:func"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);
                  assert.equal(data.Result.substring(0, 9) , "MEASURING");
                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });


  describe('#Action:VXI11', function(){
    it('should initialize the F250@e75465', function(done){

      var task = {"Action":"VXI11" ,
                  "VxiTimeout": 0,
                  "Host": "e75465",
                  "Device":"gpib0,2",
                  "Value": "P0\n"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);

                  assert.equal(_.isObject(data) , true);
                  assert.equal(_.isString(data.Result) , true);

                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });

  describe('#Action:VXI11', function(){
    it('should connect to SE1 Keithley', function(done){

      var task = {"Action":"VXI11" ,
                  "Host": "e75465",
                  "Device":"gpib0,10",
                  "Value": "*IDN?"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);

                  assert.equal(data.Result.substring(0, 8) , "KEITHLEY");

                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });


  describe('#Action:VXI11', function(){
    it('should connect to CE3 Agilent', function(done){

      var task = {"Action":"VXI11" ,
                  "Host": "e75481",
                  "Device":"gpib0,5",
                  "Value": "*IDN?"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);

                  assert.equal(data.Result.substring(0, 15) , "HEWLETT-PACKARD");

                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });

  describe('#Action:VXI11', function(){
    it('should connect to VS-CE3/FM3', function(done){

      var task = {"Action":"VXI11" ,
                  "Host": "e75481",
                  "Device":"gpib0,18",
                  "Value": "*IDN?"};

      var req = httpreq(con, function(d){
                  var data = JSON.parse(d);

                  assert.equal(data.Result.substring(0, 2) , "00");

                  done()
                });

      req.write(JSON.stringify(task));
      req.end();
    });
  });


});
