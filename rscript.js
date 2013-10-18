/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-10-18
 */

const MODULE = 'rscript';

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var fs = require('fs');

var logger = cfg.logger;

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
        logging.debug('remove working directory: %s', (e) ? e : js.WorkingDir);
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
      logging.debug('2nd "external.call"');
      external.call(pRef, js, cleanUp);
    },
    function (error) {
      prepareError(pRef, js, error);
    }
  );
}

exports.call = call;


