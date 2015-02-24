/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2015-02-24
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
 * @method call
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

  if (typeof js.lockDevice == 'boolean') params.lockDevice = js.lockDevice;
  if (!isNaN(parseInt(js.VxiTimeout))) params.readTimeout = js.VxiTimeout;
  if (!isNaN(parseInt(js.readTimeout))) params.readTimeout = js.readTimeout;
  if (!isNaN(parseInt(js.ioTimeout))) params.ioTimeout = js.ioTimeout;
  if (!isNaN(parseInt(js.lockTimeout))) params.lockTimeout = js.lockTimeout;
  if (js.termChar) params.termChar = js.termChar;

  /**
   * Funktion, die dem repeat-Ablauf übergeben wird und die eigentliche Arbeit erledigt
   * @method doIt
   * @param {string[]} b
   * @param {function} next
   */
  function doIt(b, next) {
    vxi(params, function(result) {
      b.push(result);
      next();
    }, function(error) {
      logger.error(error);
      response.prepareError(pRef, js, error);
    });
  }
  var wait = js.Wait < cfg.MIN_VXI11_WAIT ? cfg.MIN_VXI11_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;
