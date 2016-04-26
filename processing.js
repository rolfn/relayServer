/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2016-04-22
 */

var vm = require('vm');
var cfg = require('./config.js');
var tools = require('./tools.js');
var logger = cfg.logger;
var addon = null;

/* 
 TODO: Logger-Ausgaben funktionieren hier nicht. Klären, warum das so ist. 
*/

/**
 * Wenn vorhanden, Datei "relay-add.js" laden.
 */

try {
  addon = require('./relay-add.js');
  logger.info('"relay-add.js" loaded');
} catch(e) {
  logger.info('"relay-add.js" not found');
}

var process = function(target, data, code, a1, a2) {    
  // Einfache Strings und String-Arrays unterstützen.
  var evalStr = (Array.isArray(code)) ? code.join('\n') : code;
  logger.debug('evalStr: %s', evalStr);
  var script, ret = "";
  var sandbox = {};
  sandbox._x = data;
  if (typeof a1 != 'undefined') sandbox._$ = a1;
  if (typeof a2 != 'undefined') {
    if (a2.t_start !== undefined) {
      sandbox._t_start = a2.t_start;
      delete a2.t_start; //???
    }
    if (a2.t_stop !== undefined) {
      sandbox._t_stop = a2.t_stop;
      delete a2.t_stop; //???
    }    
  }
  if (addon) sandbox._ = addon; 
  try {
    script = vm.createScript(evalStr);
    script.runInNewContext(sandbox);
    for (var key in sandbox) {
      if (key != 'gc' && key[0] != '_') {// temporäre Variablen ignorieren
        logger.debug('sandbox[%s]', key, sandbox[key]);
        target[key] = sandbox[key];
      }
    }
  } catch(err) {
    ret = err.toString();
  }
  return ret;
}

module.exports = process;
