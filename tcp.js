/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-10-18
 */

const MODULE = 'tcp';

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var net = require('net');

var logger = cfg.logger;

/**
 * Konfiguration der nötigen Datenstrukturen und Aufnahme der TCP-Kommunikation.
 * Wait/Repeat wird unterstützt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  function doIt(b, next) {
    var result = [], host = js.Host, port = tools.getInt(js.Port),
      cmd = (js.Value) ? js.Value : '';
    var conn = net.createConnection(port, host);
    var timeout = tools.getInt(js.Timeout, cfg.DEFAULT_TCP_TIMEOUT);
    conn.setTimeout(timeout);
    conn.setEncoding('ascii');
    conn.addListener('connect', function(){
      conn.write(cmd);
      try {// 2012-03-05
        conn.flush(); // required for legacy support (Node <0.5)?
      } catch(err) {}
    });
    conn.addListener('end', function () {
      logger.debug('end 1: %s', JSON.stringify(result));
      for (var i=0; i < result.length;i++) {
        if ((result[i] == '\r\n') || (result[i] == '\n') ||
          (result[i] == '\r')) {
          logger.debug('end 2: %s', JSON.stringify(result));
          result.splice(i,1); // Leerzeile beseitigen.
        }
      }
      result = result.join('\n');
      b.push(result);
      next();
    });
    conn.addListener('error', function (e) {
      //response.prepareError(pRef, js, e.toString());
      var s = 'error:' + e.toString();
      logger.error('error: %s', s);
      result.push(s);
      conn.end();
    });
    conn.addListener('timeout', function () {
      logger.error('timeout');
      //response.prepareError(pRef, js, 'timeout');
      var s = 'error:timeout';
      result.push(s);
      conn.end();
    });
    conn.addListener('data', function(data){
      result.push(data);
      logger.debug('data', data);
      conn.end(); // Half-closes the stream.
    });
  }

  var wait = js.Wait < cfg.MIN_TCP_WAIT ? cfg.MIN_TCP_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;

