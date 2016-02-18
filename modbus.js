/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2016-02-18
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var net = require('net');
var os = require('os');
var modbus = require('h5.modbus');  // https://github.com/morkai/h5.modbus

var logger = cfg.logger;

/**
 * Liefert aus einem 16Bit-Integer-Wert ein Array mit 16 Werten, die
 * je nach Bit "0" oder "1" betragen. Ist "onlyLowByte" true, besteht das Array
 * nur aus 8 Werten, die den niederwertigen 8 Bits entsprechen.
 * @param {number} x
 * @param {boolean} onlyLowByte
 * @return {array}
 */
function Uint16toBitArray(x, onlyLowByte) {
  var ret = [], y = 0x0001, sh = onlyLowByte ? 8 : 16;
  function _Uint16toBitArray(_x) {
    for (var i=0; i<sh; i++) {
      ret.push(_x & (y<<i) ? 1 : 0);
    }
  }
  if (typeof x.length === 'undefined') {// single value
    _Uint16toBitArray(x);
  } else {// Array
    for (var i=0; i<x.length; i++) _Uint16toBitArray(x[i]);
  }
  return ret;
}

/**
 * Liefert aus einem Array mit maximal 0/1-Werten einen 16Bit-Integer-Wert.
 * @param {array} x
 * @return {number}
 */
function bitArrayToUint16(x) {
  var y = 0x0001, ret = 0;
  for(var i=0; i<x.length; i++) {
    if (x[i]) ret += y;
    y<<=1;
  }
  return ret;
}

/**
 * Vertauscht das zweite mit dem ersten Byte usw.
 */
if (os.endianness() === 'LE') {
  var correctEndian = function(b) {
    for(var i=0, tmp; i<b.length; i+=2) {
      tmp = b[i];
      b[i] =  b[i+1];
      b[i+1] = tmp;
    }
    return b;
  }
} else {
  var correctEndian = function(b) {
    return b;
  }
}

/**
 * Liefert neues Array, bei dem jeweils skip 16-Werte ignoriert werden.
 * @param {Uint8Array} b
 * @param {number} skip
 */
function reduceElements(b, skip) {
  // TODO: skip > 1 unterstützen
  // if (skip < 0 || skip >= b.length) return b;
  if (skip != 1) return b;
  var len = 2 * Math.round(b.length / 4);
  // byte length of the later Uint16Array must be multiple of 2
  var bb = new Uint8Array(len), j=0;
  for(var i=0; i<b.length; i+=4) {
    bb[j++] = b[i];
    bb[j++] = b[i+1];
  }
  return bb;
}

/**
 * Konfiguration der nötigen Datenstrukturen und Aufnahme der MODBUS-Kommunikation.
 * Wait/Repeat wird unterstützt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {

  var necessaryKeys = ['Host','Address','FunctionCode'], key, isMissing = false;

  for (var i=0; i<necessaryKeys.length; i++) {
    key = necessaryKeys[i];
    if (isMissing = !js.hasOwnProperty(key)) break;
  }

  if (isMissing) {
    response.prepareError(pRef, js, 'Some necessary options are missing');
    return;
  }

  var result = [], host = js.Host, address = tools.getInt(js.Address),
  quantity = tools.getInt(js.Quantity, 1),
  outmode = js.OutMode ? js.OutMode.trim() : cfg.DEFAULT_MODBUS_OUTMODE,
  port = tools.getInt(js.Port, cfg.DEFAULT_MODBUS_PORT),
  skip = tools.getInt(js.Skip, 0),
  value, fc = js.FunctionCode.trim();
  
  if (js.Value) {
    value = js.Value.length ? bitArrayToUint16(js.Value) : tools.getInt(js.Value);
  }

  fc = fc ? (fc[0].toLowerCase() + fc.slice(1)) : false;
  // "fc" entspricht nun dem Namen der relevanten Funktion

  function doIt(b, next) {
    logger.debug('modbus function: ' + fc);
    function destroyMaster() {
      setTimeout(function() {
        master.destroy();
      }, 1);
    }
    var master = modbus.createMaster({
      transport: {
        type: 'ip',
        connection: {
          type: 'tcp',
          host: host,
          port: port
        }
      },
      retryOnException: false // default: true
    });

    if (!(fc && master[fc])) {
      destroyMaster();
      response.prepareError(pRef, js, 'wrong function code');
    }

    master.on('connected', function() {
      logger.debug('connected');
    });
    master.on('disconnected', function() {
      logger.debug('disconnected');
    });
    master.on('error', function(err) {
      destroyMaster();
      logger.error(err.message);
      response.prepareError(pRef, js, err.message);
    });

    function onCompleteCommon(err, resp, func) {
      var msg = false;
      destroyMaster();
      if (err) {
        msg = err.message;
      } else if (resp.isException()) {
        msg = resp.toString();
      }
      if (msg) {// error
        logger.error(msg);
        response.prepareError(pRef, js, msg);
      } else {// gültige Antwort
        //logger.debug(require('util').inspect(resp));
        logger.debug(resp.toString());
        var x = func(); // Funktion muss aufbereitete Antwort zurückliefern
        b.push(x.length == 1 ? x[0] : x); // 1-Element-Array zu Element
        next();
      }
    }
    function onCompleteBuffer(err, resp) {
      onCompleteCommon(err, resp, function() {
        var values = resp.getValues();// Big-Endian (most significant byte first)
        var view8 = reduceElements(correctEndian(new Uint8Array(values)), skip);
        var arrBuf = view8.buffer, result;
        var view16 = new Uint16Array(arrBuf);
        logger.debug('outmode: ' + outmode);
        switch (outmode) {
          case '8Bits':  // Array of Bit-Arrays (8 Bits)
            result = [];
            for (var i=0; i<view16.length; i++) {
              result.push(Uint16toBitArray(view16[i], true));
            }
            break;
          case '16Bits': // Array of Bit-Arrays (16 Bits)
            result = [];
            for (var i=0; i<view16.length; i++) {
              result.push(Uint16toBitArray(view16[i]));
            }
            break;
          case '8Bits*': // Bit-Array (Quantity * 8 Bits)
            result = Uint16toBitArray(view16, true);
            break;
          case '16Bits*': // Bit-Array (Quantity * 16 Bits)
            result = Uint16toBitArray(view16);
            break;
          default: // 'Uint16'; Array of 16-Bit-Integers
            result = Array.from(view16);
        }
        return result;
      });
    }
    function onCompleteStates(err, resp) {
      onCompleteCommon(err, resp, function() {
        return resp.getStates().map(Number);
      });
    }
    function onCompleteDefault(err, resp) {
      onCompleteCommon(err, resp, function() {
        return resp.toString();
      });
    }
    var options = {
      interval: -1,
      onComplete: onCompleteDefault,
      onError: function(err) {// TODO: nötig?
        logger.error('onError: ' + err);
        response.prepareError(pRef, js, err);// err.message ???
      }
    };

    function checkQuantity(n, min, max) {
      var ret = quantity >= min && quantity <= max;
      if (!ret) {
        response.prepareError(pRef, js,
          'Quantity must be a number between ' + min + ' and ' + max);
      }
      return ret;
    }

    master.once('connected', function() {
      logger.debug('fc: ' + fc);
      switch (fc) {
        case 'readInputRegisters':
        case 'readHoldingRegisters':
          if (checkQuantity(quantity, 1, 125)) {
            options.onComplete = onCompleteBuffer;
            master[fc](address, quantity, options);
          }
          break;
        case 'readCoils':
        case 'readDiscreteInputs':
          if (checkQuantity(quantity, 1, 2000)) {
            options.onComplete = onCompleteStates;
            master[fc](address, quantity, options);
          }
          break;
        case 'writeSingleRegister':
          master[fc](address, value, options);
          break;
        case 'writeSingleCoil':
          master[fc](address, !!value, options);
          break;
        default:
          destroyMaster();
          response.prepareError(pRef, js, 'not implemented');
      }
    });
  }

  var wait = js.Wait < cfg.MIN_MODBUS_WAIT ? cfg.MIN_MODBUS_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);
}

exports.call = call;

