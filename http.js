/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2016-04-14
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var url = require('url');
var request = require('request');

var logger = cfg.logger;

/**
 * Konfiguration der nötigen Datenstrukturen und Aufnahme der HTTP-Kommunikation.
 * Wait/Repeat wird derzeit nicht unterstützt. Die Umgebungsvariablen proxy und
 * no_proxy werden berücksichtigt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var host = url.parse(js.Url).hostname;
  var method;
  var json = js.Json || false;
  var proxy = process.env.http_proxy;
  if (js.Body) {
    method = 'POST';
  } else {
    method = 'GET';
  }
  if (process.env.no_proxy) {
    var np = process.env.no_proxy.split(',');
    for (var i=0;i<np.length;i++) {
      if (host.indexOf(np[i].trim()) != -1) {
        logger.debug('no_proxy: %s', np[i]);
        proxy = ''; break;
      }
    }
  }
  logger.debug('method: %s, proxy: %s, json: %s', method, proxy, json);
  utils.addStartTime(js);
  request(
    { method: method,
      uri: js.Url,
      proxy: proxy, // TODO: Test ob unnötig/schädlich
      body: js.Body,
      timeout: js.Timeout,
      headers: js.Headers || {},
      encoding: js.Encoding || 'utf8',
      json: json
    },
    function (e, res, body) {
      if (!e && res.statusCode > 199 && res.statusCode < 300) {
        utils.addStopTime(js);
        logger.debug('response body', body);
        response.prepareResult(pRef, js, body);
      } else {
        var x = res && res.statusCode ? res.statusCode : e.toString();
        logger.error(x);
        response.prepareError(pRef, js, x);
      }
    }
  );
}

exports.call = call;

