/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-11-26
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var response = require('./response.js');
var fs = require('fs');
var os = require('os');
var path = require('path');
var tmp = require('temp'); tmp.track();

var logger = cfg.logger;

/**
 * TODO: Code vom Vorgänger übernehmen und anpassen.
 */

function call(pRef, js) {

  function post(pRef, js) {
    var resultFile = path.join(js.WorkingDir, cfg.TEX_FILE.replace('.tex',
      '.' + cfg.DEFAULT_TEX_DESTFMT));
    fs.readFile(resultFile, function (err, data) {
      if (err) response.prepareError(pRef, js, err);
      logger.debug('successful read: ' + resultFile);
      if (!js.KeepFiles) {
        logger.debug('remove working directory: %s: ', js.WorkingDir);
        tmp.cleanup();
      }
      response.prepareResult(pRef, js, data);
    });
  }

  function getCmd() {
    if (!!!js.Command) return cfg.DEFAULT_TEX_CMD;
    if (cfg.TEX_CMDS.indexOf(js.Command) === -1) return null;
    else return js.Command;
  }

  var cmd = getCmd();
  if (!cmd) response.prepareError(pRef, js, 'invalid TeX command');

  if (!js.Body) response.prepareError(pRef, js, 'missing document data');
  var content = (Array.isArray(js.Body)) ? js.Body.join('\n') : js.Body;

  js.KeepFiles = typeof js.KeepFiles === 'undefined' ? false : !!js.KeepFiles;
  js.Repeat = tools.getInt(js.Repeat, cfg.DEFAULT_TEX_RUNS);
  js.ContentType = 'application/pdf';
  js.OutputType = 'stream';
  js.OutputEncoding = 'binary';
  js.execStr = cmd + ' ' + cfg.TEX_FILE;

  // "js.WorkingDir" anlegen und "js.Body" in Datei "cfg.R_FILE"
  //  schreiben, dann zweiter Aufruf von "external.call" ("/usr/bin/Rscript")
  tmp.mkdir({dir:os.tmpDir(), prefix:'latex.'}, function(err, p) {
    js.WorkingDir = p;
    var fname = path.join(p, cfg.TEX_FILE)
    fs.writeFile(fname, content, function(err) {
      if (err) {
        var e = 'File creation error: ' + err;
        logger.error(e);
        response.prepareError(pRef, js, e);
      } else {
        delete js.Body;
        // Zweiter Aufruf mit Dateinamen-Parameter statt 'Body';
        logger.debug('2nd "external.call"');
        external.call(pRef, js, post);
      }
    });
  });

}

exports.call = call;
