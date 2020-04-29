/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2020-04-29
 */

var exec = require('child_process').exec;
var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var prepare = require('./prepareScriptCall.js');
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
  logger.debug('Action: ', js.Action);
  if (js._execStr === undefined) {
    
    if (js.Body) {// Erster Aufruf; 
      // kehrt später noch mal hier her zurück (dann "js.Body == false").
      prepare.call(pRef, js); // js.Body --> js._paramFile usw.
      return;
    } else {
      if (!js.Cmd) {
        response.prepareError(pRef, js, '"Cmd" missing');
        return;
      } 
      execStr = js.Cmd;
      if (js.Args0) {
        execStr = execStr + ' ' + (Array.isArray(js.Args0) ? js.Args0.join(' ') 
          : js.Args0);
      } 
      if (js._paramFile) execStr = execStr + ' ' + js._paramFile;
      if (js.Args) {
        execStr = execStr + ' ' + (Array.isArray(js.Args) ? js.Args.join(' ') 
          : js.Args);
      } 
    }
                                      
  } else {// Sonderfall (js._execStr bereits anderweitig definiert; z.B. "TEX")
    execStr = js._execStr; 
  }

  logger.info('execStr: ', execStr);

  var execOpt = {};
  execOpt.timeout = tools.getInt(js.Timeout, cfg.DEFAULT_EXEC_TIMEOUT);
  execOpt.maxBuffer = tools.getInt(js.MaxBuffer, cfg.DEFAULT_EXEC_MAXBUFFER);
  if (js.WorkingDir !== undefined) execOpt.cwd = js.WorkingDir;
  //execOpt.env = (js.ENV != undefined) ? js.ENV : process.env;
  if (js.OutputEncoding == 'binary') execOpt.encoding = 'binary';

  logger.debug('execOpt: ', execOpt);

  var doIt = function(b, next) {
    logger.debug('time_begin: ', new Date().getTime());
    var child = exec(execStr, execOpt,
      function (error, stdout, stderr) {
        if (error) {
          logger.error(`error: ${error} (${stderr.length} / ${stdout.length})`);
          logger.error('exitCode: ', error.code);
          js.exitCode = error.code;
          response.prepareError(pRef, js, error.toString());
        } else {
          logger.debug('time_success: ', new Date().getTime());
          var res;

          if (js.OutputEncoding == 'binary') {
            //res = new Buffer(stdout, 'binary');
            res = Buffer.from(stdout, 'binary');
          } else {
            res = stdout;
          }
          logger.debug('exitCode: ', 0);
          js.exitCode = 0;
          logger.debug(`res: ${typeof res} (${res.length} Bytes)`);
          logger.debug(`OutputType: ${js.OutputType}, OutputEncoding: ${js.OutputEncoding}`); 
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
