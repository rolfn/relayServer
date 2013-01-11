// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'tcp';

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var net = require('net');

eval(tools.getFunctionCode('debug'));
eval(tools.getFunctionCode('fdebug'));
var inspect = tools.inspect;

function call(pRef, js) {

  function doIt(b, next) {
    var result = [], host = js.Host, port = tools.getInt(js.Port),
      cmd = (js.Value) ? js.Value : '';
    var conn = net.createConnection(port, host);
    conn.setTimeout(2000); // ???
    conn.setEncoding('ascii');
    conn.addListener('connect', function(){ 
      conn.write(cmd);
      try {// 2012-03-05
        conn.flush(); // required for legacy support (Node <0.5)?
      } catch(err) {}
    });
    conn.addListener('end', function () {
      fdebug('result 1', JSON.stringify(result));
      for (var i=0; i<result.length;i++) {
        if ((result[i] == '\r\n') || (result[i] == '\n') ||
          (result[i] == '\r')) {
          fdebug('result 2', JSON.stringify(result));  
          result.splice(i,1); // Leerzeilen beseitigen.
        }
      }
      result = result.join('\n');
      js.t_stop = new Date().getTime();
      b.push(result);
      next();
    });
    conn.addListener('error', function (e) {
      conn.destroy();
      //response.prepareError(pRef, js, e.toString());
      var s = 'error:' + e.toString();
      b.push(s);
    });
    conn.addListener('timeout', function () {
      conn.destroy();
      //response.prepareError(pRef, js, 'timeout');
      var s = 'error:timeout';
      b.push(s);
    });
    conn.addListener('data', function(data){
      result.push(data);
      conn.end(); // Half-closes the stream.
    });
  }

  var wait = js.Wait < cfg.MIN_TCP_WAIT ? cfg.MIN_TCP_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;

