/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-09-18
 */

const MODULE = 'rscript';

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var fs = require('fs');

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
 * Schreibt Inhalt von js.Body in temporäre Datei und ergänzt js.Value
 * (R-Parameter) durch Namen und Pfad dieser temporären Datei. Zum Schluss wird
 * js.Body beseitigt und per external.call das Programm Rscript aufgerufen.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var cleanUp = function(pRef, js) {
    if (!js.KeepFiles) {
      tools.rmdirRecursive(js.WorkingDir, function (e) {
        fdebug('remove working directory', (e) ? e : js.WorkingDir);
      });
    }
  };
  if ((js.KeepFiles == undefined) || (js.KeepFiles != true))
    js.KeepFiles = false;
  var params = [];
  js.WorkingDir = tools.getTempDir() + '/' + pRef.jobId;
  params.push(cfg.R_FILE);
  if (js.Value != undefined) {
    if (Array.isArray(js.Value)) {
      params = params.concat(js.Value);
    } else {
      params = params.concat(js.Value.split(' '));
    }
  }
  // Alte Parameter zuvorderst ergänzt durch Namen von "cfg.R_FILE".
  js.Value = params;
  // "fs.write" erfordert Buffer! "string" und "string[]" unterstützen.
  var content = (Array.isArray(js.Body)) ? new Buffer(js.Body.join('\n'))
    : new Buffer(js.Body);

  // "js.WorkingDir" anlegen und "js.Body" in Datei "cfg.R_FILE"
  //  schreiben, zweiter Aufruf von "external.call" ("/usr/bin/Rscript")
  tools.createTempFile(js.WorkingDir, cfg.R_FILE, content,
    function() {
      delete js.Body;
      // Zweiter Aufruf mit Dateinamen-Parameter statt 'Body';
      fdebug('2nd "external.call"');
      external.call(pRef, js, cleanUp);
    },
    function (error) {
      prepareError(pRef, js, error);
    }
  );
}

exports.call = call;


