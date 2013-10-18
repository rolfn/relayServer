/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-10-18
 */

const MODULE = 'internal';

var fs = require('fs');
var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var _tcp = require('./tcp.js');
var _http = require('./http.js');
var _email = require('./email.js');
//var _ldap = require('./ldap.js');
//    derzeit (2013-01-14) Probleme (buffertools)!
//    npm install buffertools -g ; npm install ldapjs -g
//var _latex = require('./latex.js'); // TODO: Überarbeiten!

var logger = cfg.logger;

/**
 * Liefert Angaben zum Betriebssystem
 * (siehe: http://www.freedesktop.org/software/systemd/man/os-release.html)
 * @param {string|[string]} fname release-Dateien (kompletter Dateiname)
 * @param {function} success Aufruf bei Erfolg
 * @param {function} error Aufruf im Fehlerfall
*/
function getOSrelease(_file, success, error) {
  var files = Array.isArray(_file) ? _file : [_file];
  var ret = null, i = 0;
  function _getOSrelease(idx) {
    if (idx == files.length && !ret) {
      error('can\'t read os informations');
    } else {
      fs.readFile(files[idx], function (err, data) {
        if (err) {
          _getOSrelease(++idx);
        } else {
          ret = {};
          var lines = data.toString().split(/\r\n|\r|\n/);
          var isSUSE = false;
          for (var i=0; i<lines.length; i++) {
            var x = lines[i].split('=');
            var key = '', val = '';
            if (x.length == 1) {
              if (i==0) {// 'SuSE-release'
                isSUSE = true;
                key = 'NAME';
                if (lines[i].indexOf('SUSE Linux Enterprise') > -1) {
                  val = 'SLE';
                } else {
                  val = lines[i].split(/\s/g)[0];
                }
              }
            } else if (x.length > 1) {
              key = x[0].trim();
              val = x[1].trim();
            }
            if (isSUSE && key == 'VERSION') {
              key = 'VERSION_ID';
            }
            val = val.replace(/"/g, '');
            if (key != '' &&
              ((isSUSE && (key == 'NAME' || key == 'VERSION_ID') || !isSUSE))) {
              ret[key] = val;
            }
          }
          success(ret);
        }
      });
    }
  }
  _getOSrelease(i);
}

/**
 * Verzweigung bzw. Ausführung je nach internem Action-Typ. Ist es sinnvoll,
 * dass Wait/Repeat wirksam werden sollen, so ist die Funktion "doIt" zu
 * definieren.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
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
        var s = tools.pad2(d.getHours()) + ':' +
          tools.pad2(d.getMinutes()) + ':' + tools.pad2(d.getSeconds());
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
      // "/usr/local/bin/texcaller" benutzen. (???)
      ///processLATEX_1(pRef, js);
      response.prepareError(pRef, js, 'not working!');
      break;
    // Administration
    case '_version':
      response.prepareResult(pRef, js, cfg.VERSION + ', ' + cfg.DATE);
      break;
    case '_nodesVersion':
      response.prepareResult(pRef, js, process.version);
      break;
    case '_environment':
      response.prepareResult(pRef, js, process.env);
      break;
    case '_os_release':
      getOSrelease(cfg.RELEASE_FILES,
        function (d) {
          response.prepareResult(pRef, js, d);
        },
        function (e) {
          response.prepareError(pRef, js, e);
        }
      );
      break;
    case '_killRepeats':
      for (var key in cfg.theRepeats) {
        delete cfg.theRepeats[key];
      }
      response.prepareResult(pRef, js, 'OK');
      break;
    // TODO: Evtl. Ausgabe von "process.memoryUsage()" !?
    //                         "process.uptime()" !?
    default: response.prepareError(pRef, js, 'unknown internal action');
  }
  if (doIt) {
    utils.repeat(js.Repeat, js.Wait, doIt, function(repeatResult) {
      response.prepareResult(pRef, js, repeatResult);
    }, pRef, js);
  }
}

exports.call = call;
