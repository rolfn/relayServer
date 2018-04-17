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
  if (!isNaN(parseInt(js.Timeout))) params.readTimeout = js.Timeout;
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
    var diff = new Date().getTime() - cfg.vxi11_last_time, 
        addWait = diff < cfg.MIN_VXI11_WAIT ? cfg.MIN_VXI11_WAIT-diff : 0;
    logger.info('VXI (last): ' + (cfg.vxi11_last_time ? diff + ' ms' : '?'));
    if (addWait) logger.info('VXI (addWait): %d ms', addWait);
    // TODO: mehrfach überprüfen!
    setTimeout(function() {// warten, wenn zu wenig Zeit vergangen
      cfg.vxi11_last_time = new Date().getTime();
      vxi(params, function(result) {
        b.push(result);
        next();
      }, function(error) {
        logger.error(error);
        response.prepareError(pRef, js, error);
      });              
    }, addWait);  
  }
  utils.repeat(js.Repeat, js.Wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;
