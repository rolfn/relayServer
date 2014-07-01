/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2014-03-21
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var dgram = require('dgram');

var logger = cfg.logger;

/**
 * Konfiguration der nötigen Datenstrukturen und Aufnahme der UDP-Kommunikation.
 * Wait/Repeat wird unterstützt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  function doIt(b, next) {
    var host = js.Host, port = tools.getInt(js.Port);
    var buf = new Buffer((js.Value) ? js.Value : '');
    var client = dgram.createSocket('udp4');
    client.send(buf, 0, buf.length, port, host, function(err, bytes) {
      client.close();
      if (!err) {
        logger.debug('success (%d Bytes sendet)', bytes);
        b.push('OK');
        next();
      } else {
        logger.error('error: %s', err);
        b.push('error: ' + err);
        // evtl. auch hier "next();"?
      }
    });
  }

  //var wait = js.Wait < cfg.MIN_TCP_WAIT ? cfg.MIN_TCP_WAIT : js.Wait;
  utils.repeat(js.Repeat, js.Wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;

