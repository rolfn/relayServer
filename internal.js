// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'internal';

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');

eval(tools.getFunctionCode('debug'));
eval(tools.getFunctionCode('fdebug'));
var inspect = tools.inspect;

// Wenn "Repeat" wirksam werden soll, muss die Funktion "doIt" definiert werden.
exports.call = function(pRef, js) {
  fdebug('js', inspect(js));
  var doIt = null;
  var wait = js.Wait;
  switch (js.Action) {
    case 'RANDOM':
      doIt = function(b) {
        b.push(Math.random());
      };
      break;
    case 'TIME':
      doIt = function(b) {
        var d = new Date();
        var s = tools.pad2(d.getHours()) + ':' + tools.pad2(d.getMinutes()) +
          ':' + tools.pad2(d.getSeconds());
        b.push(s);
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
      // eigentl. external, aber wegen Komplexität intern verwaltet.
      // http://www.profv.de/texcaller/index.html
      processLATEX_1(pRef, js);
      break;
    // Administration
    case '_version':
      response.prepareResult(pRef, js, cfg.VERSION);
      break;
    case '_environment':
      response.prepareResult(pRef, js, cfg.env);
      break;
    case '_killRepeats':
      for (key in theRepeats) {
        theRepeats[key].running = false; // oder besser "delete"?
      }
      response.prepareResult(pRef, js, 'OK');
      break;
    default: response.prepareError(pRef, js, 'unknown internal action');
  }
  // Wiederholte Funtionsaufrufe, falls gewünscht.
  if (doIt) {
    utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
      response.prepareResult(pRef, js, repeatResult);
    }, pRef);
  } 
}
