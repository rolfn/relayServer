
/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2019-01-25
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var internal = require('./internal.js');
var external = require('./external.js');
var response = require('./response.js');
var process = require('./processing.js');

var logger = cfg.logger;

/**
 * Analysiert den Action-Typ. Rückgabe:
 * <pre>
 * -1: "internal action",
 *  1: "valid external action"
 * </pre>
 * @param {string} str Action-String.
 * @return {number} Action-Typ
*/
function getActionType(str) {
  if (!str) return 99;
  var ret = 0;
  if (str == 'EXECUTE') {
    ret = 1;
  } else {
    ret = -1;
  }

  return ret;
}

/**
 * Default-Werte ergänzen;
 * Wenn 'DemoMode', dann sofort 'DemoResponse' zurücksenden, sonst
 * Analyse von "Action" und entsprechende Verzweigung
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function analyzeActions3(pRef, js) {
  logger.debug(js);
  //js.Repeat = tools.getInt(js.Repeat, 1);
  js.Wait = tools.getInt(js.Wait, 0);
  //if (js.OutputType === undefined) js.OutputType = 'json';
  if (js.OutputEncoding === undefined) js.OutputEncoding = 'utf8';
  js.t_start = []; js.t_stop = [];
  if (('DemoMode' in js) && (js.DemoMode) && ('DemoResponse' in js)) {
    var doIt = function(b, next) {
      b.push(js.DemoResponse);
      next();
    };
    utils.repeat(js.Repeat, js.Wait, doIt, function(repeatResult) {
      response.prepareResult(pRef, js, repeatResult);
    }, pRef, js);
  } else if ('Action' in js) {
    var aType = getActionType(js.Action);
    logger.info(`aType: ${aType}`);
    if (aType == -1) {
      internal.call(pRef, js);
    } else if (aType == 1) {
      external.call(pRef, js);
    } else {
      response.prepareError(pRef, js, 'unknown action');
    }
  } else response.prepareError(pRef, js, 'action not found');
}

/**
 * Enthält die empfangene JSON-Struktur das Schlüsselwort "Passwd", so wird
 * der zugeordnete Wert verschlüsselt, damit er in nachfolgenden debug-Ausgaben
 * nicht lesbar ist.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function analyzeActions2(pRef, js) {
  if (js.Passwd !== undefined) {
    zlib.deflate(js.Passwd, function(err, buf) {
      if (err) {
        response.prepareError(pRef, js, 'internal error');
      } else {
        js.Passwd = buf;
        analyzeActions3(pRef, js);
      }
    });
  } else {
    analyzeActions3(pRef, js);
  }
}

/**
 * Parsen der empfangene Daten zu JS-Objekt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {string} data empfangene Daten
 */
function analyzeActions1(pRef, data) {
  var js = {};
  if (data) {
    try{
      js = JSON.parse(data);
    } catch(err) {
      response.prepareError(pRef, js, 'data error (invalid JSON)');
    }    
    // Preprocessing
    if (js.PreProcessing) {
      process(js, js, js.PreProcessing, function(error) {
        if (error) response.prepareError(pRef, js, error);
        analyzeActions2(pRef, js);
      });
    } else analyzeActions2(pRef, js);
  } else {
    response.prepareError(pRef, js, 'no data');
  }
}

/**
 * Interne Serverdaten (req, res, ...) für später speichern, Daten empfangen.
 * @param {object} _req request-Objekt
 * @param {object} _res response-Objekt
 */
function start(_req, _res) {
  var pRef = {req:_req, res:_res, jobId:'NJS'+new Date().getTime()};
  logger.info('open connection: ', new Date().getTime());
  _req.setEncoding('utf8');
  _req.socket.setTimeout(0);
  var body = '';
  _req.on('data', function (chunk) {
    body += chunk;
  });
  _req.on('end', function () {
    analyzeActions1(pRef, body);
  });
  _res.connection.on('close', function () {
    logger.info('close connection: ', new Date().getTime());
    if (typeof gc == 'function') gc();
  });
}

exports.start = start;
