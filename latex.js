/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2014-05-08
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var external = require('./external.js');
var response = require('./response.js');
var fs = require('fs');
var os = require('os');
var path = require('path');
var tmp = require('temp'); tmp.track();

var logger = cfg.logger;

function call(pRef, js) {
  function post(pRef, js) {
    var texFile = js.execStr.split(' ').pop();
    var resultFile = path.join(js.WorkingDir,
      texFile.replace('.tex', '.' + cfg.DEFAULT_TEX_DESTFMT));
    logger.debug('texFile: ' + texFile);
    logger.debug('resultFile: ' + resultFile);
    fs.readFile(resultFile, function (err, data) {
      if (err) {
        if (js.execStr.indexOf(cfg.TEX_ERROR_FILE) == -1) {// keine Endlosschleife
          // Fehlermeldung als pdf-Code
          js.execStr = js.execStr.replace(cfg.TEX_FILE, cfg.TEX_ERROR_FILE);
          var fname = path.join(js.WorkingDir, cfg.TEX_ERROR_FILE);

          var content = [];
          content.push('\\documentclass{article}');
          content.push('\\usepackage[T1]{fontenc}');
          content.push('\\usepackage{lmodern}');
          content.push('\\usepackage{listings}');
          content.push('\\lstset{basicstyle=\\footnotesize\\ttfamily}');
          content.push('\\usepackage[margin={10mm,10mm}]{geometry}');
          content.push('\\begin{document}');
          content.push('\\lstinputlisting{texput.log}');
          content.push('\\end{document}');

          fs.writeFile(fname, content.join('\n'), function(err) {
            if (err) {
              var e = 'File creation error: ' + err;
              logger.error(e);
              response.prepareError(pRef, js, e);
            } else {
              logger.debug('2nd "external.call"');
              external.call(pRef, js, post);
            }
          });
        } else response.prepareError(pRef, js, err);
      } else {
        logger.debug('successful read: ' + resultFile);
        if (!js.KeepFiles) {
          logger.debug('remove working directory: %s: ', js.WorkingDir);
          tmp.cleanup();
        }
        response.prepareResult(pRef, js, data);
      }
    });
  }

  function getCmd() {
    if (!!!js.Command) return cfg.DEFAULT_TEX_CMD;
    if (cfg.TEX_CMDS.indexOf(js.Command) === -1) return null;
    else return js.Command;
  }

  var cmd = getCmd();
  if (!cmd) response.prepareError(pRef, js, 'invalid TeX command');
  if (!js.Body) response.prepareError(pRef, js, 'missing document data');
  var content = (Array.isArray(js.Body)) ? js.Body.join('\n') : js.Body;

  js.KeepFiles = typeof js.KeepFiles === 'undefined' ? false : !!js.KeepFiles;
  js.Repeat = tools.getInt(js.Repeat, cfg.DEFAULT_TEX_RUNS);
  var filename = js.Filename ? js.Filename :
    cfg.DEFAULT_TEX_OUTNAME + '.' + cfg.DEFAULT_TEX_DESTFMT;
  logger.debug('filename: %s', filename);
  js.Head = {};
  js.Head['Content-Type'] = 'application/pdf';
  js.Head['Content-Disposition'] = 'attachment; filename=' + filename;
  js.OutputType = 'stream';
  js.OutputEncoding = 'binary';// TODO: Kann das weg?
  js.execStr = cmd + ' -interaction=batchmode '  + cfg.TEX_FILE;
  logger.debug('Head: %s', js.Head);
  // "js.WorkingDir" anlegen und "js.Body" in Datei "cfg.TEX_FILE"
  //  schreiben, dann Aufruf von "external.call".
  tmp.mkdir({dir:os.tmpDir(), prefix:'latex.'}, function(err, p) {
    js.WorkingDir = p;
    var fname = path.join(p, cfg.TEX_FILE);
    fs.writeFile(fname, content, function(err) {
      if (err) {
        var e = 'File creation error: ' + err;
        logger.error(e);
        response.prepareError(pRef, js, e);
      } else {
        delete js.Body;
        // Aufruf mit Dateinamen-Parameter statt 'Body';
        logger.debug('1st "external.call"');
        external.call(pRef, js, post);
      }
    });
  });

}

exports.call = call;
