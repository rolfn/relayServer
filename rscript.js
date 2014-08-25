/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-11-26
 */

var cfg = require('./config.js');
var response = require('./response.js');
var tools = require('./tools.js');
var external = require('./external.js');
var fs = require('fs');
var os = require('os');
var path = require('path');
var tmp = require('temp'); tmp.track();

var logger = cfg.logger;

/**
 * Schreibt Inhalt von js.Body in temporäre Datei und ergänzt js.Value
 * (R-Parameter) durch Namen und Pfad dieser temporären Datei. Zum Schluss wird
 * js.Body beseitigt und per external.call das Programm Rscript aufgerufen.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var cleanUp = function(pRef, js, data) {
    if (!js.KeepFiles) {
      logger.debug('remove working directory: %s: ', js.WorkingDir);
      tmp.cleanup();
    }
    response.prepareResult(pRef, js, data);
  };

  js.KeepFiles = typeof js.KeepFiles === 'undefined' ? false : !!js.KeepFiles;

  var params = [];

  params.push(cfg.R_FILE);
  if (js.Value !== undefined) {
    if (Array.isArray(js.Value)) {
      params = params.concat(js.Value);
    } else {
      params = params.concat(js.Value.split(' '));
    }
  }
  // Alte Parameter zuvorderst ergänzt durch Namen von "cfg.R_FILE".
  js.Value = params;

  if (!js.Body) response.prepareError(pRef, js, 'missing program code');
  // "String" und "String[]" unterstützen.
  var content = Array.isArray(js.Body) ? js.Body.join('\n') : js.Body;

  // "js.WorkingDir" anlegen und "js.Body" in Datei "cfg.R_FILE"
  //  schreiben, dann zweiter Aufruf von "external.call" ("/usr/bin/Rscript")
  tmp.mkdir({dir:os.tmpDir(), prefix:'R.'}, function(err, p) {
    js.WorkingDir = p;
    var fname = path.join(p, cfg.R_FILE)
    fs.writeFile(fname, content, function(err) {
      if (err) {
        var e = 'File creation error: ' + err;
        logger.error(e);
        response.prepareError(pRef, js, e);
      } else {
        delete js.Body;
        // Zweiter Aufruf mit Dateinamen-Parameter statt 'Body';
        logger.debug('2nd "external.call"');
        external.call(pRef, js, cleanUp);
      }
    });
  });

}

exports.call = call;


