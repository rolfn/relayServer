
/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-10-08
 */

const MODULE = 'relay';

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var internal = require('./internal.js');
var external = require('./external.js');
var response = require('./response.js');

/**
 * Erzeugt String-Repräsentation der inneren Struktur einer JS-Variable
 * (Rekursion bis Ebene 2, coloriert)
 * @param {object} o Zu untersuchende JS-Variable.
 * @return {string}  String-Repräsentation
 */
function inspect(o) {};
inspect = tools.inspect;

/**
 * In Abhängigkeit von "level" Ausgabe von Informationen. Der aktuelle
 * Modulname wird ebenfalls ausgegeben.
 * @param {string} item meist Funktionsname
 * @param {string} subitem spezifische Aktion innerhalb der Funktion.
 * @param {string} info Daten
 * @param {number} level
 */
// TODO: Hier und anderswo auf "winston" umsteigen.
function debug(item, subitem, info, level) {};
debug = tools.createFunction('debug', MODULE);

/**
 * Wie "debug", aber "item" (Funktionsname) wird selbst ermittelt.
 * @param subitem
 * @param info
 * @param level
 */
function fdebug(subitem, info, level) {};
fdebug = tools.createFunction('fdebug', debug);

/**
 * Analysiert den Action-Typ. Rückgabe:
 * <pre>
 * -1: "internal action",
 *  0: "invalid external action",
 *  1: "valid external action"
 * </pre>
 * @param {string} str Action-String.
 * @return {number} Action-Typ
*/
function getActionType(str) {
  var ret = str.indexOf('/');
  if (ret > -1) {
    ret = 0;
    for (i in cfg.bin) {
      if (cfg.bin[i] == str) {
        ret = 1; break;
      }
    }
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
  fdebug('js', inspect(js));
  js.Repeat = tools.getInt(js.Repeat, 1);
  js.Wait = tools.getInt(js.Wait, 0);
  if (js.OutputType == undefined) js.OutputType = 'json';
  if (js.OutputEncoding == undefined) js.OutputEncoding = 'utf8';
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
    fdebug('aType', '' + aType);
    if (aType == -1) {
      internal.call(pRef, js);
    } else if (aType == 1) {
      external.call(pRef, js);
    } else {
      response.prepareError(pRef, js, 'unknown external action');
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
  if (js.Passwd != undefined) {
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
      response.prepareError(pRef, js, 'data error');
    }
    analyzeActions2(pRef, js);
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
  fdebug('time', '' + new Date().getTime(), 1);
  var pRef = {req:_req, res:_res, jobId:'NJS'+new Date().getTime()};
  fdebug('_req', inspect(_req), 102);
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
    debug('close connection', 'time', '' + new Date().getTime(), 1);
    debug('close connection');
  });
};

exports.start = start;
