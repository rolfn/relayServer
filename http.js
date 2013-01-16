/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-01-15
 */

const MODULE = 'http';

var cfg = require('./config.js');
var tools = require('./tools.js');
var response = require('./response.js');
var url = require('url');
var request = require('/usr/lib/node_modules/request');
                   
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
 * @param item meist Funktionsname
 * @param subitem spezifische Aktion innerhalb der Funktion.
 * @param info Daten
 * @param level
 */
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
 * Konfiguration der nötigen Datenstrukturen und Aufnahme der HTTP-Kommunikation.
 * Wait/Repeat wird derzeit nicht unterstützt. Die Umgebungsvariablen proxy und
 * no_proxy werden berücksichtigt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var host = url.parse(js.Url).hostname;
  var method = (js.Body) ? 'POST' : 'GET';
  var proxy = process.env.http_proxy;
  var np = process.env.no_proxy.split(',');
  var json = js.Json || false;
  for (var i=0;i<np.length;i++) {
    if (host.indexOf(np[i].trim()) != -1) {
      fdebug('no_proxy', np[i]);
      proxy = ''; break;
    }
  }
  fdebug('method', method);
  fdebug('proxy', proxy);
  fdebug('json', json);
  request(
    { method: method,
      uri: js.Url,
      proxy: proxy,
      body: js.Body,
      timeout: js.Timeout,
      json: json
    },
    function (e, res, body) {
      if (!e && res.statusCode == 200) {
        fdebug('response body', inspect(body));
        response.prepareResult(pRef, js, body);
      } else {
        fdebug('error', e);
        var x = ((res) && (res.statusCode)) ? res.statusCode :
          'no response';
        fdebug('statusCode', x);
        response.prepareError(pRef, js, x);
      }
    }
  );
}

exports.call = call;

