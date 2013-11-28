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
    var texFile = js.execStr.replace(js.Command, '').trim();
    var resultFile = path.join(js.WorkingDir,
      texFile.replace('.tex', '.' + cfg.DEFAULT_TEX_DESTFMT));
    fs.readFile(resultFile, function (err, data) {
      if (err) {
        // TODO: Stattdessen neue Datei "tex-error.tex" erzeugen. Darin
        // "texput.log" einladen und weiteren "external.call" mit geändertem
        // "js.execStr". Vorsicht vor Endlosschleife!
        response.prepareError(pRef, js, err);
      } else {
        logger.debug('successful read: ' + resultFile);
        if (!js.KeepFiles) {
          logger.debug('remove working directory: %s: ', js.WorkingDir);
          tmp.cleanup();
        }
        response.prepareResult(pRef, js, data);
      }
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

  // "js.WorkingDir" anlegen und "js.Body" in Datei "cfg.TEX_FILE"
  //  schreiben, dann zweiter Aufruf von "external.call".
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
        // Aufruf mit Dateinamen-Parameter statt 'Body';
        logger.debug('switch to "external.call"');
        external.call(pRef, js, post);
      }
    });
  });

}

exports.call = call;
