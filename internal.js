/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2017-04-18
 */

var fs = require('fs');
var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var _tcp = require('./tcp.js');
var _udp = require('./udp.js');
var _http = require('./http.js');
var _email = require('./email.js');
//var _ldap = require('./ldap.js');
//    derzeit (2013-01-14) Probleme (buffertools)!
//    npm install buffertools -g ; npm install ldapjs -g
var _latex = require('./latex.js'); // TODO: Überarbeiten!
var _vxi11 = require('./vxi.js');
var _excel = require('./excel.js');
var _modbus = require('./modbus.js');

var logger = cfg.logger;

/**
 * Liefert Angaben zum Betriebssystem
 * (siehe: http://www.freedesktop.org/software/systemd/man/os-release.html)
 * @param {string} fname release-Dateien (kompletter Dateiname)
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
              if (i === 0) {// 'SuSE-release'
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
            if (key !== '' &&
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
    case 'UDP':
      _udp.call(pRef, js);
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
    case 'TEX':
      _latex.call(pRef, js);
      break;
    case 'VXI11':
      _vxi11.call(pRef, js);
      break;
    case 'MODBUS':
      logger.log('MODBUS');
      _modbus.call(pRef, js);
      break;
    case 'XLSX-OUT':
      _excel.toXLSX(pRef, js);
      break;
    case 'XLSX-IN':
      _excel.fromXLSX(pRef, js);
      break;
    case 'TTY':
      response.prepareError(pRef, js, 'not yet implemented!');
      // TODO: Zugriff auf /dev/*tty* (ggf. auch auf "/dev/char/x:y" o.ä.)
      break;
    // Administration
    case '_version':
      response.prepareResult(pRef, js, cfg.VERSION + 
        ' (node: ' + process.versions.node + ')');
      break;
    case '_nodejsVersion':
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
    case '_exit':
      process.on('exit', function () {
        response.prepareResult(pRef, js, 'OK');
      });
      process.exit(0);
      break;
    default: response.prepareError(pRef, js, 'unknown action');
  }
  if (doIt) {
    utils.repeat(js.Repeat, js.Wait, doIt, function(repeatResult) {
      response.prepareResult(pRef, js, repeatResult);
    }, pRef, js);
  }
}

exports.call = call;
