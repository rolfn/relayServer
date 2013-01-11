
// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'relay';

var exec = require('child_process').exec;
var cfg = require('./config.js');
var tools = require('./tools.js');
var internal = require('./internal.js');
var response = require('./response.js');

/**
 * In Abhängigkeit von "level" Ausgabe von Informationen. Der aktuelle 
 * Modulname wird ebenfalls ausgegeben.
 *   function(item, subitem, info, level)
 * @param item meist Funktionsname
 * @param subitem spezifische Aktion innerhalb der Funktion.
 * @param info Daten
 * @param level
 */
eval(tools.getFunctionCode('debug'));

/**
 * Wie "debug", aber "item" (Funktionsname) wird selbst ermittelt.
 *   function fdebug (subitem, info, level)
 * @param subitem
 * @param info
 * @param level
 */
eval(tools.getFunctionCode('fdebug'));

var inspect = tools.inspect;

/**
 * Analysiert den Action-Typ.
 * @param str Action-String.
 * @returns -1 --> "internal action",
 *           0 --> "invalid external action",
 *           1 --> "valid external action"
 */
function getActionType(str) {
  var ret = str.indexOf('/');
  if (ret > -1) {
    ret = 0;
    for (i in cfg.bin) {
      if (cfg.bin[i] == str) {
        ret = 1; break;
      }
    }
  }
  return ret;
}

function analyzeActions_3(pRef, js) {
  fdebug('js', inspect(js));
  js.Repeat = tools.getInt(js.Repeat, 1);
  js.Wait = tools.getInt(js.Wait, 0);
  if (js.OutputType == undefined) js.OutputType = 'json';
  if (js.OutputEncoding == undefined) js.OutputEncoding = 'utf8';
  js.t_start = new Date().getTime(); 
  if (('DemoMode' in js) && (js.DemoMode) && ('DemoResponse' in js)) {
    prepareResult(pRef, js, js.DemoResponse); // Hier auch _repeat?
  } else if ('Action' in js) {
    var aType = getActionType(js.Action);
    fdebug('aType', '' + aType);
    if (aType == -1) {
      internal.call(pRef, js);
    } else if (aType == 1) {
      //callExternal(pRef, js);
      response.prepareError(pRef, js, 'external action not implementd');
    } else if (aType == 0) {
      response.prepareError(pRef, js, 'unknown external action');
    }
  } else response.prepareError(pRef, js, 'action not found');
}

function analyzeActions_2(pRef, js) {
  if (js.Passwd != undefined) {
    zlib.deflate(js.Passwd, function(err, buf) {
      if (err) {
        response.prepareError(pRef, js, 'internal error');
      } else {
        js.Passwd = buf;
        analyzeActions_3(pRef, js);
      }
    });      
  } else {
    analyzeActions_3(pRef, js);
  }
}

function analyzeActions_1(data, pRef) {
  var js = {};
  if (data) {
    try{
      js = JSON.parse(data);
    } catch(err) {
      response.prepareError(pRef, js, 'data error');
    }
    analyzeActions_2(pRef, js);
  } else {
    response.prepareError(pRef, js, 'no data');
  }
}

exports.start = function start(_req, _res) {
  fdebug('time', '' + new Date().getTime(), 1);
  var pRef = {req:_req, res:_res, jobId:'NJS'+new Date().getTime()};
  fdebug('_req', inspect(_req), 102);
  _req.setEncoding('utf8');
  _req.socket.setTimeout(0); 
  var body = '';
  _req.on('data', function (chunk) {
    body += chunk;
  }); 
  _req.on('end', function () {
    tools.getEnv(cfg.env, analyzeActions_1, body, pRef);
  });
  _res.connection.on('close', function () {
    debug('close connection', 'time', '' + new Date().getTime(), 1);
    debug('close connection');
  });
};
