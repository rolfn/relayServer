
// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-14

const MODULE = 'rscript';

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var fs = require('fs');

eval(tools.getFunctionCode('debug'));
eval(tools.getFunctionCode('fdebug'));
var inspect = tools.inspect;

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
  js.WorkingDir = cfg.env.TMPDIR + '/' + pRef.jobId;
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


