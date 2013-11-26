/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-11-26
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var response = require('./response.js');
var Tmp = require('tmp');
var Fs = require('fs');
var Path = require('path');
Tmp.setGracefulCleanup();

var logger = cfg.logger;

/**
 * TODO: Code vom Vorgänger übernehmen und anpassen.
 */

function call(pRef, js) {

  function post(pRef, js) {
    var rfile = Path.join(js.WorkingDir, cfg.TEX_FILE.replace('.tex', '.' +
      cfg.DEFAULT_TEX_DESTFMT));
    logger.debug('result file: ' + rfile);
    logger.debug('remove: ' + js.WorkingDir);
    // TODO: Ersetzen durch Tmp.rmdirRecursiveSync(...)
    //       falls der Autor Funktion public macht.
    if (!js.KeepFiles) tools.rmdirRecursiveSync(js.WorkingDir);
    // TODO: result <-- "texput.pdf"
    ///var result = 'Inhalt von ' + rfile;
    Fs.readFile(rfile, function (err, data) {
      if (err) response.prepareError(pRef, js, err);
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

  Tmp.dir({ prefix:'node-latex.', keep:js.KeepFiles, unsafeCleanup:true },
    function (err, path) {
      if (err) response.prepareError(pRef, js, err);

      logger.debug('Tempdir: ' + path);

      js.WorkingDir = path;
      js.execStr = cmd + ' ' + cfg.TEX_FILE;
      //js.execStr = '/usr/bin/echo ' + js.execStr;
      var fname = Path.join(path, cfg.TEX_FILE);
      Fs.writeFile(fname, content, function (err) {
        if (err) {
          var e = 'File creation error: ' + err;
          logger.error(e);
          response.prepareError(pRef, js, e);
        }
        logger.debug('File created: ' + fname);
        external.call(pRef, js, post);
      });
    }
  );

}

exports.call = call;
