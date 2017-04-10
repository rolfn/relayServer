/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2017-04-10
 */

var exec = require('child_process').exec;
var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var prgTempfile = require('./prgTempfile.js');
var response = require('./response.js');

var logger = cfg.logger;

/**
 * Konfiguration je nach externem Action-Typ; Ausführung des externen Programms
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {function} Aufruf nach Beendigung des externen Programmaufrufs
 */
function call(pRef, js, postFunc) {
  var execStr = '';
  logger.debug('Action: %s', js.Action);
  if (js.execStr === undefined) {

    execStr = js.Action;

    switch (js.Action) {// Spezifische Ergänzungen der Aufrufe
      case cfg.bin.DATE:
        execStr = execStr + ' "+%Y-%m-%d %H:%M:%S"';
        break;
      case cfg.bin.RSCRIPT:
        if (js.Body !== undefined) {
          prgTempfile.call(pRef, js);
          // Kehrt später noch mal zu dieser Funktion zurück.
          return;
        }
        // TODO: LaTeX ähnlich wie RSCRIPT handhaben. (???)
        // TODO: RSCRIPT ergänzen und dazu Script-Behandlung generalisieren.
        break;
      default:
        break;
    }

    if (js.Value !== undefined) {
      if (Array.isArray(js.Value)) {
        for (var i=0; i < js.Value.length; i++) {
          execStr = execStr + ' "' + js.Value[i] + '"';
        }
      } else {
        execStr = execStr + ' "' + js.Value + '"';
      }
    }

  } else {// Sonderfall
    execStr = js.execStr; // z.B. "TEX"
  }

  logger.info('execStr: %s', execStr);

  var execOpt = {};
  execOpt.timeout = tools.getInt(js.Timeout, cfg.DEFAULT_EXEC_TIMEOUT);
  execOpt.maxBuffer = tools.getInt(js.MaxBuffer, cfg.DEFAULT_EXEC_MAXBUFFER);
  if (js.WorkingDir !== undefined) execOpt.cwd = js.WorkingDir;
  //execOpt.env = (js.ENV != undefined) ? js.ENV : process.env;
  if (js.OutputEncoding == 'binary') execOpt.encoding = 'binary';

  logger.debug('execOpt: ', execOpt);

  var doIt = function(b, next) {
    logger.debug('time_begin: %d', new Date().getTime());
    var child = exec(execStr, execOpt,
      function (error, stdout, stderr) {
        if (error) {
          logger.error('error: %s (%d / %d)', error, stderr.length, stdout.length);
          logger.error('exitCode:', error.code);
          js.exitCode = error.code;
          response.prepareError(pRef, js, error.toString());
        } else {
          logger.debug('time_success: %d', new Date().getTime());
          var res;

          if (js.OutputEncoding == 'binary') {
            res = new Buffer(stdout, 'binary');
          } else {
            res = stdout;
          }
          logger.debug('exitCode:', 0);
          js.exitCode = 0;
          logger.debug('res: %s (%d Bytes)', typeof res, res.length);
          logger.debug('OutputType: %s, OutputEncoding: %s', js.OutputType,
            js.OutputEncoding);
          b.push(res);
        }
        next();
      }
    );
  };

  logger.debug('js: ', js);

  var wait = (js.Wait < cfg.MIN_EXEC_WAIT) ? cfg.MIN_EXEC_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(result) {
    if (postFunc) {
      logger.debug('call postFunc');
      postFunc(pRef, js, result);
    } else response.prepareResult(pRef, js, result);
  }, pRef, js);

}

exports.call = call;
