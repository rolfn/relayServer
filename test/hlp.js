var http      = require("http")
  , testport  = 55556;

exports.testport = testport;
exports.req = function(cb){
  var con = {
    // hostname: "e73462.berlin.ptb.de",
    // port: 55555,
    hostname: "localhost",
    port: testport,
    path: "/",
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  }
    , req = http.request(con, function(res) {
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
