// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'response';

var cfg = require('./config.js');
var tools = require('./tools.js');

var addon = null;
try {
  addon = require('./relay-add.js');
} catch(e) {
}

eval(tools.getFunctionCode('debug'));
eval(tools.getFunctionCode('fdebug'));
var inspect = tools.inspect;

function _sendResponse(pRef, js, _data) {
  fdebug('_data', _data);
  var ctype, data;
  if (js.OutputType == 'stream') {
    ctype = ((js.ContentType != undefined) ? js.ContentType :
      'application/octet-stream') + ';charset=ISO-8859-1';
    // 8-Bit-Charset nötig!
    data = _data;
  } else {
    ctype = 'application/json';
    data = JSON.stringify(_data) + '\n';
  }
  fdebug('ContentType', ctype);
  pRef.res.writeHead(200, {
    'Content-Type':ctype,
    'Access-Control-Allow-Origin':'*'});
  pRef.res.end(data);
  pRef.req.connection.end();
}

// Ergebnis an den Aufrufer zurücksenden.
function prepareResult(pRef, js, data) {
  var x = data;
  var jsonRes = {};

  fdebug('js', inspect(js));

  if (js.t_start != undefined) jsonRes.t_start = js.t_start;
  if (js.t_stop != undefined) jsonRes.t_stop = js.t_stop;    
  
  if (js.Action == cfg.bin.VXITRANSCEIVER) {
    /*
      Der oder die gelieferten Strings haben am Anfang und am Ende
      einen Zeitstempel (ms seit 1.1.1970). Diese müssen entfernt, aber
      gerettet werden.
      Beispiel: "1348578392026|MEASURING  -1.17E-3|1348578392032"
                 t_start       GPIB-Response       t_stop
    */
    var a;
    /// Zum Vergleich der Zeiten ///
    jsonRes.t__start = [];
    for (var i=0;i<js.t_start.length;i++) {
      jsonRes.t__start[i] = js.t_start[i];
    }
    jsonRes.t__stop = [];
    for (var i=0;i<js.t_stop.length;i++) {
      jsonRes.t__stop[i] = js.t_stop[i];
    }
    /// //////////////////////////////
    if (!Array.isArray(x)) x = [x];
    jsonRes.t_start = [], jsonRes.t_stop = [];
    for (var i=0;i<x.length;i++) {
      a = x[i].split('|');
      jsonRes.t_start.push(parseInt(a.shift())); // erstes Element ist Startzeit
      jsonRes.t_stop.push(parseInt(a.pop()));    // letztes Element ist Stoppzeit
      x[i] = a.join('|'); // Falls vorher mehr als zwei "|" enthalten waren.
    }
    ///
    if (!jsonRes.t__start.length || !jsonRes.t__stop.length) {
      delete jsonRes.t__start;
      delete jsonRes.t__stop;
    } else if (jsonRes.t__start.length == 1) {
      jsonRes.t__start = jsonRes.t__start[0];
      jsonRes.t__stop = jsonRes.t__stop[0];
    }
    ///
  }
fdebug('jsonRes A', inspect(jsonRes));
  if (!jsonRes.t_start.length || !jsonRes.t_stop.length) {
    delete jsonRes.t_start;
    delete jsonRes.t_stop;
  } else if (jsonRes.t_start.length == 1) {
    jsonRes.t_start = jsonRes.t_start[0];
    jsonRes.t_stop = jsonRes.t_stop[0];
  }
fdebug('jsonRes B', inspect(jsonRes));  
  if ((js) && (js.PostProcessing)) {
    // Einfache Strings und String-Arrays unterstützen.
    var evalStr = (Array.isArray(js.PostProcessing)) ?
      js.PostProcessing.join('') : js.PostProcessing;
    fdebug('evalStr', inspect(evalStr));
    var sandbox = {};
    sandbox._x = x;
    if (jsonRes.t_start != undefined) {
      sandbox._t_start = jsonRes.t_start;
      delete jsonRes.t_start; //???
    } 
    if (jsonRes.t_stop != undefined) {
      sandbox._t_stop = jsonRes.t_stop;
      delete jsonRes.t_stop;
    }
    if (addon != undefined) sandbox._ = addon;
    try{
      // Benutzer-JS-Anweisungen innerhalb der sandbox ausführen.
      vm.runInNewContext(evalStr, sandbox);
    } catch(err) {
      prepareError(pRef, js, 'Postprocessing failed: ' + err);
    }
    // sandbox-Variablen der Rückgabe-Struktur zuweisen.
    for (var key in sandbox) {
      // "runInNewContext" bringt ggf. Funktion "gc" mit. Schwer wegzubekommen!
      if (key != 'gc') {
        fdebug('sandbox[' + key + ']', inspect(sandbox[key]));
        // temporäre Variablen ignorieren
        if (key[0] != '_') jsonRes[key] = sandbox[key];
      }
    }
  } else {
    jsonRes.Result = x;
  }
  fdebug('jsonRes', inspect(jsonRes));
  if (js.OutputType == 'stream') {
    if (jsonRes.Result != undefined) {
      _sendResponse(pRef, js, jsonRes.Result);
    } else {
      _sendResponse(pRef, js, x);
    }
  } else {// 'json'
    _sendResponse(pRef, js, jsonRes);
  }
}

exports.prepareResult = prepareResult;

// Fehlermeldung an den Aufrufer zurücksenden.
function prepareError(pRef, js, data) {
  js.OutputType = 'json';
  var jsonRes = {error:data};
  _sendResponse(pRef, js, jsonRes);
}

exports.prepareError = prepareError;

