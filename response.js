/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-11-25
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var vm = require('vm');
var addon = null;

var logger = cfg.logger;

/**
 * Wenn vorhanden, Datei "relay-add.js" laden.
 */
try {
  addon = require('./relay-add.js');
  logger.info('"relay-add.js" loaded');
} catch(e) {
  logger.info('"relay-add.js" not found');
}

/**
 * Aufbereitung der zu sendenden Daten; html-Header erzeugen; Daten senden.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {object} _data zu sendende Daten
 */
function sendResponse(pRef, js, _data) {
  js.OutputType = js.OutputType || 'json';
  //logger.debug('_data: ', _data.toString().slice(0,100));
  logger.debug('_data: ', tools.inspect(_data));
  var data, head = js.Head ? js.Head : {};
  logger.debug('OutputType: %s', js.OutputType);
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

  if ((js) && (js.PostProcessing)) {
    // Einfache Strings und String-Arrays unterstützen.
    var evalStr = (Array.isArray(js.PostProcessing)) ?
      js.PostProcessing.join('') : js.PostProcessing;
    logger.debug('evalStr: %s', evalStr);

    var sandbox = {};
    sandbox._x = x;
    if (jsonRes.t_start !== undefined) {
      sandbox._t_start = jsonRes.t_start;
      delete jsonRes.t_start; //???
    }
    if (jsonRes.t_stop !== undefined) {
      sandbox._t_stop = jsonRes.t_stop;
      delete jsonRes.t_stop;
    }
    if (addon !== undefined) sandbox._ = addon;
    logger.debug('addon: ', addon);
    try{
      // Benutzer-JS-Anweisungen innerhalb der sandbox ausführen.
      vm.runInNewContext(evalStr, sandbox);
    } catch(err) {
      prepareError(pRef, js, 'Postprocessing failed: ' + err);
    }
    // sandbox-Variablen der Rückgabe-Struktur zuweisen.
    for (var key in sandbox) {
      // "runInNewContext" bringt Funktion "gc" mit.
      if (key != 'gc') {
        logger.debug('sandbox[%s]', key, sandbox[key]);
        // temporäre Variablen ignorieren
        if (key[0] != '_') jsonRes[key] = sandbox[key];
      }
    }
  } else {
    jsonRes.Result = x;
  }
  //logger.debug('jsonRes: ', jsonRes);
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

exports.prepareResult = prepareResult;

/**
 * Aufbereitung der zu sendenden Daten im Fehlerfall.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {object} data zu sendende Daten
 */
function prepareError(pRef, js, data) {
  js.OutputType = 'json';
  var jsonRes = {error:data};
  sendResponse(pRef, js, jsonRes);
}

exports.prepareError = prepareError;

