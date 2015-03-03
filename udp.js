/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2015-03-03
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
    var timeout = tools.getInt(js.Timeout, cfg.DEFAULT_UDP_TIMEOUT);
    var client = dgram.createSocket('udp4');

    client.on('error', function (e) {
      logger.error(e.toString());
      client.close();
      response.prepareError(pRef, js, s);
    });
    client.send(buf, 0, buf.length, port, host, function(err, bytes) {
      if (!err) {
        logger.debug('%d Bytes sended: %s', bytes, buf.toString('utf8', 0, bytes));
      } else {
        logger.error(err);
        response.prepareError(pRef, js, err);
      }
    });

    if (timeout) {
      client.on('message', function (msg, rinfo) {
        var value = msg.toString('utf8', 0, msg.length);
        logger.debug('%d Bytes received: %s', msg.length, value);
        b.push(value);
        client.close();
        next(); // ?
      });
      setTimeout(function() {
        try{
          client.close();
          logger.error('Timeout > %d', timeout);
          response.prepareError(pRef, js, 'Timeout');
        } catch(err) {
        }
      }, timeout);
    } else {// Spezialfall, falls keine Antwort vom Gerät erwartet werden kann
      logger.debug('send "OK" back ("timeout==0")');
      b.push('OK');
      client.close();
      next();
    }

  }

  var wait = js.Wait < cfg.MIN_UDP_WAIT ? cfg.MIN_UDP_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;

