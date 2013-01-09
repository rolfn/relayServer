// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-09

const MODULE = 'external';

var cfg = require('./config.js');
var tools = require('./tools.js');

/**
 * In Abhängigkeit von "level" Ausgabe von Informationen.
 * @param item meist Funktionsname
 * @param subitem spezifische Aktion innerhalb der Funktion.
 * @param info Daten
 * @param level
 */
function debug(item, subitem, info, level) {
  tools.debug(MODULE, item, subitem, info, level);
}

/**
 * Wie "debug", aber "item" (Funktionsname) wird selbst ermittelt.
 * @param subitem
 * @param info
 * @param level
 */
function fdebug (subitem, info, level) {
  var item = arguments.callee.caller.name ? arguments.callee.caller.name : '::';
  debug(item, subitem, info, level);
}

