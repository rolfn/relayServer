/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2018-04-17
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
    function addDelay(nb, success, error) {
      nb--;
      if (!nb) error(); // letzter Versuch erfolglos
      var diff = new Date().getTime() - cfg.vxi11_last_time, 
        addWait = diff < cfg.MIN_VXI11_WAIT ? cfg.MIN_VXI11_WAIT-diff : 0;
      logger.info('[' + nb + '] VXI11 (last): ' + 
        (cfg.vxi11_last_time ? diff + ' ms' : '?'));
      if (addWait) logger.info('[' + nb + '] VXI11 (addWait): %d ms', addWait);
      else success();      
      setTimeout(function() {// warten, wenn zu wenig Zeit vergangen
        addDelay(nb, success, error);
      }, addWait);
    }
    addDelay(5, // max. Anzahl Versuche, "race condition" zu vermeiden
      function() {// success
        cfg.vxi11_last_time = new Date().getTime();
        vxi(params, function(result) {
          b.push(result);
          next();
        }, function(error) {
          logger.error(error);
          response.prepareError(pRef, js, error);
        });      
      }, 
      function() {// error
        var e = 'Unresolved race condition';
        logger.error(e);
        response.prepareError(pRef, js, e);
      }
    );
  }
    
  utils.repeat(js.Repeat, js.Wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;
