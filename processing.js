/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2016-04-21
 */

var vm = require('vm');
var cfg = require('./config.js');
var logger = cfg.logger;
var addon = null;

/**
 * Wenn vorhanden, Datei "relay-add.js" laden.
 */
try {
  addon = require('./relay-add.js');
  logger.info('"relay-add.js" loaded');
} catch(e) {
  logger.info('"relay-add.js" not found');
}
 
var sandbox = {}; 

var process = function(id, data, code) {    
  // Einfache Strings und String-Arrays unterstützen.
  var evalStr = (Array.isArray(code)) ? code.join('') : code;
  logger.debug('evalStr: %s', evalStr);
  var script, ret = {};
  sandbox[id] = {};
  sandbox[id]._x = data;
  if (addon) sandbox[id]._ = addon; 
  try {
    script = vm.createScript(evalStr);
    script.runInNewContext(sandbox[id]);
    for (var key in sandbox[id]) {
      if (key != 'gc' && key[0] != '_') {// temporäre Variablen ignorieren
        logger.debug('sandbox[%s][%s]', id, key, sandbox[id][key]);
        ret[key] = sandbox[id][key];
      }
    }
  } catch(err) {
    ret.error = err;
  }


  delete sandbox[id];
  return ret;
}

module.exports = process;
