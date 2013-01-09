// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-09

const MODULE = 'internal';

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

function callInternal(pRef, js) {
  fdebug('js', inspect(js));
  var doIt = null;
  var wait = js.Wait;
  switch (js.Action) {
    case 'RANDOM':
      doIt = function(b) {
        if (b) b.push(Math.random());
        else prepareResult(pRef, js, Math.random());
      };
      break;
    case 'TIME':
      doIt = function(b) {
        var d = new Date();
        var s = tools.pad2(d.getHours()) + ':' + tools.pad2(d.getMinutes()) +
          ':' + tools.pad2(d.getSeconds());
        if (b) b.push(s); else prepareResult(pRef, js, s);
      };
      break;
    case 'TCP':
      processTCP(pRef, js);
      break;
    case 'HTTP':
      processHTTP(pRef, js);
      break;  
    case 'EMAIL':
      processEMAIL(pRef, js);
      break;
    case 'LDAP_AUTH':
      processLDAP_AUTH_1(pRef, js);
      break;
    case 'LDAP_SEARCH':
      processLDAP_SEARCH_1(pRef, js);
      break;
    case 'LaTeX':
      // eigentl. external, aber intern verwaltet.
      // http://www.profv.de/texcaller/index.html
      processLATEX_1(pRef, js);
      break;
    // Administration
    case '_version':
      prepareResult(pRef, js, cfg.VERSION);
      break;
    case '_environment':
      prepareResult(pRef, js, cfg.ENV);
      break;
    case '_killRepeats':
      for (key in theRepeats) {
        theRepeats[key].running = false;
      }
      prepareResult(pRef, js, 'OK');
      break;
    default: prepareError(pRef, js, 'unknown internal action');
  }
  // Wiederholte Funtionsaufrufe, falls gewünscht.
  if (doIt) {
    _repeat(js.Repeat, wait, doIt,
      function(repeatResult) {
        prepareResult(pRef, js, repeatResult);
      }, pRef);
  } 
}
