// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'http';

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var request = require('/usr/lib/node_modules/request');

eval(tools.getFunctionCode('debug'));
eval(tools.getFunctionCode('fdebug'));
var inspect = tools.inspect;

function call(pRef, js) {
  var host = url.parse(js.Url).hostname;
  var method = (js.Body) ? 'POST' : 'GET';
  var proxy = process.env.http_proxy;
  var np = process.env.no_proxy.split(',');
  var json = js.Json || false;
  for (var i=0;i<np.length;i++) {
    if (host.indexOf(np[i].trim()) != -1) {
      fdebug('no_proxy', np[i]);
      proxy = ''; break;
    }
  }
  fdebug('method', method);
  fdebug('proxy', proxy);
  fdebug('json', json);
  request(
    { method: method,
      uri: js.Url,
      proxy: proxy,
      body: js.Body,
      timeout: js.Timeout,
      json: json
    },
    function (e, res, body) {
      if (!e && res.statusCode == 200) {
        fdebug('response body', inspect(body));
        prepareResult(pRef, js, body);
      } else {
        fdebug('error', e);
        var x = ((res) && (res.statusCode)) ? res.statusCode :
          'no response';
        fdebug('statusCode', x);
        prepareError(pRef, js, x);
      }
    }
  );
}

exports.call = call;

