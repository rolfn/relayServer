/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2014-05-22
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var vxi = require('vxi11').vxiTransceiver;

var logger = cfg.logger;

/**
 * Konfiguration der nötigen Datenstrukturen und Aufnahme der VXI-Kommunikation.
 * Wait/Repeat wird unterstützt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var params = { host:js.Host, device:js.Device, command:js.Value,
    encoding: js.Encoding,
    logger: {
      log:logger.debug,
      error:logger.error
    }
  };
  var timeout = parseInt(js.Timeout);
  // "I/O Timeout" und "Lock Timeout" bei DEVICE_READ
  if (isFinite(timeout)) params.readTimeout = timeout;
  function doIt(b, next) {
    vxi(params, function(result) {
      b.push(result);
      next();
    }, function(error) {
      logger.error(error);
      b.push(error);
      next(); // oder besser "response.prepareError(pRef, js, e);"?
    });
  }
  var wait = js.Wait < cfg.MIN_VXI11_WAIT ? cfg.MIN_VXI11_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;
