/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-11-26
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var response = require('./response.js');
var Tmp = require('tmp');
Tmp.setGracefulCleanup();

var logger = cfg.logger;

/**
 * TODO: Code vom Vorgänger übernehmen und anpassen.
 */

function call(pRef, js) {

  function clear(pRef, js) {
    logger.debug('remove: ' + js.WorkingDir);
    // TODO: Ersetzen durch Tmp.rmdirRecursiveSync(...)
    //       falls der Autor Funktion public macht.
    if (!js.KeepFiles) tools.rmdirRecursiveSync(js.WorkingDir);
  }

  function getCmd() {
    if (!!!js.Command) return cfg.DEFAULT_TEX_CMD;
    if (cfg.TEX_CMDS.indexOf(js.Command) === -1) return null;
    else return js.Command;
  }

  var cmd = getCmd();
  if (!cmd) response.prepareError(pRef, js, 'invalid TeX command');

  js.Repeat = js.Repeat || cfg.DEFAULT_TEX_RUNS;

  Tmp.dir({ prefix:'node-latex.', keep:js.KeepFiles, unsafeCleanup:true },
    function (err, path) {
    if (err) {
      logger.error(err); // ???
      response.prepareError(pRef, js, err);
    }
    logger.debug('Tempdir: ' + path);

    js.WorkingDir = path;
    js.execStr = 'TEXINPUTS=".:' + path + ':" ' + cmd + ' ' + cfg.TEX_FILE;
    js.execStr = '/usr/bin/echo ' + path + ' ' + cmd;

    external.call(pRef, js, clear);

  });
}

exports.call = call;
