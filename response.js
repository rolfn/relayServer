/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2019-01-25
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var process = require('./processing.js');
var vm = require('vm');
var addon = null;
var util = require('util');
var logger = cfg.logger;
var sandbox = {};

/**
 * Aufbereitung der zu sendenden Daten; html-Header erzeugen; Daten senden.
 * @method sendResponse
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {object} _data zu sendende Daten
 */
function sendResponse(pRef, js, _data) {
  js.OutputType = js.OutputType || 'json';
  logger.debug('_data: ', _data);
  var data, head = js.Head ? js.Head : {};
  logger.debug('OutputType: ', js.OutputType);
  if (js.OutputType == 'stream') {
    if (!head['Content-Type']) head['Content-Type'] =
      'application/octet-stream;charset=ISO-8859-1';
      // Hier 8-Bit-Charset nötig!
    data = _data;
  } else {
    head['Content-Type'] = 'application/json';
    data = JSON.stringify(_data) + '\n';
  }
  head['Access-Control-Allow-Origin'] = '*';
  logger.debug('head: ', head);
  pRef.res.writeHead(200, head);
  pRef.res.end(data);
  pRef.req.connection.end();
  return;
}


/**
 * Aufbereitung der zu sendenden Daten im Erfolgsfall, Postprocessing.
 * @method prepareResult
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {object} data zu sendende Daten
 */
function prepareResult(pRef, js, data) {
  var x = data;
  var jsonRes = {};

  logger.debug('js: ', js);

  if (js.t_start !== undefined) jsonRes.t_start = js.t_start;
  if (js.t_stop !== undefined) jsonRes.t_stop = js.t_stop;
  if (js.exitCode !== undefined) jsonRes.exitCode = js.exitCode;

  if (!jsonRes.t_start.length || !jsonRes.t_stop.length) {
    delete jsonRes.t_start;
    delete jsonRes.t_stop;
  } else if (jsonRes.t_start.length == 1) {
    jsonRes.t_start = jsonRes.t_start[0];
    jsonRes.t_stop = jsonRes.t_stop[0];
  } // TODO: Sinnhaftigkeit überprüfen!

  function _prepareResult() {  
    if (js.OutputType == 'stream') {
      if (jsonRes.Result !== undefined) {
        sendResponse(pRef, js, jsonRes.Result);
      } else {
        sendResponse(pRef, js, x);
      }
    } else {// 'json'
      sendResponse(pRef, js, jsonRes);
    }
  }  

  if ((js) && (js.PostProcessing)) {
    // Postprocessing
    var processResult = {};
    process(jsonRes, x, js.PostProcessing, function(error) {
      if (error) prepareError(pRef, js, error);   
      _prepareResult();
    }, js);
  } else {
    jsonRes.Result = x;
    _prepareResult();
  }
}
exports.prepareResult = prepareResult;

/**
 * Aufbereitung der zu sendenden Daten im Fehlerfall.
 * @method prepareError
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {object} data zu sendende Daten
 */
function prepareError(pRef, js, data) {
  js.OutputType = 'json';
  var jsonRes = {error:data};
  if (js.exitCode) jsonRes.exitCode = js.exitCode;
  sendResponse(pRef, js, jsonRes);
}

exports.prepareError = prepareError;
