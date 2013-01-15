// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-14

const MODULE = 'internal';

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var _tcp = require('./tcp.js');
var _http = require('./http.js');
var _email = require('./email.js');
//var _ldap = require('./ldap.js'); // derzeit (2013-01-14) Probleme (buffertools)!
// npm install buffertools -g ; npm install ldapjs -g
// var _latex = require('./latex.js');

function inspect() {};
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

function call(pRef, js) {
  fdebug('js', inspect(js));
  var doIt = null;
  switch (js.Action) {
    case 'RANDOM':
      doIt = function(b, next) {
        b.push(Math.random());
        next();
      };
      break;
    case 'TIME':
      doIt = function(b, next) {
        var d = new Date();
        var s = tools.pad2(d.getHours()) + ':' + tools.pad2(d.getMinutes()) + ':' +
          tools.pad2(d.getSeconds());
        b.push(s);
        next();
      };
      break;
    case 'TCP':
      _tcp.call(pRef, js);
      break;
    case 'HTTP':
      _http.call(pRef, js);
      break;  
    case 'EMAIL':
      _email.call(pRef, js);
      break;
    case 'LDAP_AUTH':
      //_ldap.auth(pRef, js);
      response.prepareError(pRef, js, 'not working!');
      break;
    case 'LDAP_SEARCH':
      //_ldap.search(pRef, js);
      response.prepareError(pRef, js, 'not working!');
      break;
    case 'LaTeX':
      // eigentl. external, aber wegen Komplexität intern verwaltet.
      // http://www.profv.de/texcaller/index.html
      // https://github.com/vog/texcaller
      // TODO: Auslagern nach "dispatcher.js" und external action
      // "/usr/local/bin/texcaller" benutzen.
      ///processLATEX_1(pRef, js);
      response.prepareError(pRef, js, 'not working!');
      break;
    // Administration
    case '_version':
      response.prepareResult(pRef, js, cfg.VERSION + ', ' + cfg.DATE);
      break;
    case '_environment':
      response.prepareResult(pRef, js, cfg.env);
      break;
    case '_killRepeats':
      for (var key in cfg.theRepeats) {
        delete cfg.theRepeats[key];
      }
      response.prepareResult(pRef, js, 'OK');
      break;
    default: response.prepareError(pRef, js, 'unknown internal action');
  }
  // Wiederholte Funtionsaufrufe, falls gewünscht.
  if (doIt) {
    utils.repeat(js.Repeat, js.Wait, doIt, function(repeatResult) {
      response.prepareResult(pRef, js, repeatResult);
    }, pRef, js);
  } 
}

exports.call = call;
