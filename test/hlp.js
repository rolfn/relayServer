var _         = require("underscore")
  , http      = require("http")
  , testport  = 55556
  , testhost  = process.env.TESTHOST;

exports.testport = testport;
exports.req = function(cb){
  var con = {
    path: "/",
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  };

  if(_.isUndefined(testhost)){
    con.hostname = "localhost";
    con.port     =  testport;
  }else{
    con.hostname = testhost;
    con.port     = 55555;
  }
  var req = http.request(con, function(res) {
              res.setEncoding("utf8");
              res.on("data",   cb);
              res.on("error", function(e) {
                console.log("res.error " + e);
              });
            });

  req.on("error", function(e) {
    console.log("req.error " + e);
  });

  return req;
};
