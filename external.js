/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-01-14
 */

const MODULE = 'external';

var exec = require('child_process').exec;
var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var rscript = require('./rscript.js');
var response = require('./response.js');

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
 * Konfiguration je nach externem Action-Typ; Ausführung des externen Programmaufrufs
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {function} Aufruf nach Beendigung des externen Programmaufrufs 
 */
function call(pRef, js, postFunc) {
  var execStr = '';
  fdebug('Action', js.Action);
  if (js.execStr == undefined) {

    execStr = js.Action;
  
    switch (js.Action) {// Spezifische Ergänzungen der Aufrufe
      case cfg.bin.VXITRANSCEIVER:
        execStr = execStr + ' "' + js.Host + '" "' + js.Device + '"' +
          ((js.VxiTimeout) ? ' ' + js.VxiTimeout : '');
        break;
      case cfg.bin.DATE:
        execStr = execStr + ' "+%Y-%m-%d %H:%M:%S"';
        break;
      case cfg.bin.RSCRIPT:
        if (js.Body != undefined) {
          rscript.call(pRef, js);
          // Kehrt später noch mal zu dieser Funktion zurück.
          return;
        }
        // TODO: LaTeX ähnlich wie RSCRIPT handhaben. (???)
        break
      default:
        break;
    }

    if (js.Value != undefined) {
      if (Array.isArray(js.Value)) {
        for (var i=0; i < js.Value.length; i++) {
          execStr = execStr + ' "' + js.Value[i] + '"';
        }
      } else {
        execStr = execStr + ' "' + js.Value + '"';
      }
    }

  } else {// Sonderfall
    execStr = js.execStr;
  }

  fdebug('execStr', execStr);

  var execOpt = {};
  execOpt.timeout = (js.TimeOut) ? js.TimeOut : cfg.DEFAULT_EXEC_TIMEOUT;
  execOpt.maxBuffer = (js.MaxBuffer) ? js.MaxBuffer : cfg.DEFAULT_EXEC_MAXBUFFER;
  if (js.WorkingDir != undefined) execOpt.cwd = js.WorkingDir;
  //execOpt.env = (js.ENV != undefined) ? js.ENV : process.env;
  if (js.OutputEncoding == 'binary') execOpt.encoding = 'binary';

  fdebug('execOpt', inspect(execOpt), 102);

  var doIt = function(b, next) {
    fdebug('time_begin', '' + new Date().getTime(), 1);
    var child = exec(execStr, execOpt,
      function (error, stdout, stderr) {
        if (error) {
          fdebug('error', error + ' ' + stderr.length + ' ' + stdout.length);
          var s = 'error:' + error;
          b.push(s);
        } else {
          fdebug('time_success', '' + new Date().getTime(), 1);
          fdebug('success', stdout.length + ' Bytes');
          var res;

          if (js.OutputEncoding == 'binary') {
            res = new Buffer(stdout, 'binary');
          } else {
            res = stdout;
          }
          
          fdebug('res', typeof res + '//' + res.length + ' Bytes');
          fdebug('OutputType', js.OutputType);
          fdebug('OutputEncoding', js.OutputEncoding);
          b.push(res);
        }
        next();
      }
    );
  }

  var wait = (js.Wait < cfg.MIN_EXEC_WAIT) ? cfg.MIN_EXEC_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    if (postFunc) {
      fdebug('postFunc');
      postFunc(pRef, js);
    }
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;
