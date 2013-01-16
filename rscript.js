/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-01-16
 */

const MODULE = 'rscript';

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var fs = require('fs');

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
 * Schreibt Inhalt von js.Body in temporäre Datei und ergänzt js.Body 
 * (R-Parameter) durch Namen und Pfad der temporären Datei: Zum Schluss wird
 * js.Body beseitigt und per external.call das Programm Rscript aufgerufen.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var cleanUp = function(pRef, js) {
    if (!js.KeepFiles) {
      tools.rmdirRecursive(js.WorkingDir, function (error) {
        fdebug('remove working directory', (error) ? error : js.WorkingDir);
      });
    }
  };
  if ((js.KeepFiles == undefined) || (js.KeepFiles != true))
    js.KeepFiles = false;
  var params = [];
  var Rfile = 'cmd.R';
  js.WorkingDir = tools.getTempDir() + '/' + pRef.jobId;
  params.push(Rfile);
  if (js.Value != undefined) {
    if (Array.isArray(js.Value)) {
      params = params.concat(js.Value); 
    } else {
      params = params.concat(js.Value.split(' ')); 
    }
  }
  // Alte Parameter zuvorderst ergänzt durch `Rfile'.
  js.Value = params;
  // Für `js.Body' String oder String-Array unterstützen.
  var content = (Array.isArray(js.Body)) ? new Buffer(js.Body.join('\n')) :
    new Buffer(js.Body);
  // `js.WorkingDir' anlegen und `js.Body' in Datei `Rfile' schreiben.
  // TODO: Allgemeingültig nach "tools" auslagern.
  //  tools.createTempFile(tempDir, tempFile, content)
  fs.mkdir(js.WorkingDir, '700', function (error) {
    if (error) {
      fdebug('create working directory', error);
      prepareError(pRef, js, error);
    } else {
      fdebug('create working directory', js.WorkingDir);
      fs.open(js.WorkingDir + '/' + Rfile, 'w', '600', function(e, fd) {
        if (e) {
          fdebug('file open', e);
          prepareError(pRef, js, e);
        } else {
          fdebug('file open', Rfile);
          fs.write(fd, content, 0, content.length, null, function(e, nb, buf){
            if (e) {
              fdebug('write', e);
              prepareError(pRef, js, e);
            } else {
              fdebug('write', nb + ' Bytes');
              fs.close(fd, function(e){
                if (e) {
                  fdebug('file close', e);
                  prepareError(pRef, js, e);
                } else {
                  fdebug('file close', Rfile);
                  delete js.Body;
                  // Zweiter Aufruf mit Dateinamen-Parameter statt 'Body';
                  fdebug('2nd "external.call"', e);
                  external.call(pRef, js, cleanUp);                      
                }
              });
            }
          });
        }
      });         
    }
  });
}

exports.call = call;


