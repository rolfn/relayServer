/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2015-10-20
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var net = require('net');
var os = require('os');
var modbus = require('h5.modbus');

var logger = cfg.logger;

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

function reduceElements(b) {
  var len = 2 * Math.round(b.length / 4);
  // byte length of the later Uint16Array must be a multiple of 2
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
  functioncode = js.FunctionCode.trim();

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

  master.on('connected', function() {
    logger.debug('connected');
  });
  master.on('disconnected', function() {
    logger.debug('disconnected');
  });
  master.on('error', function(err) {//
    logger.error(err.message);
    master.destroy();
  });

  function atEnd() {
    setTimeout(function() {// ???
      logger.debug('master destroy');
      console.log('master destroy');
      master.destroy();
    }, 200);
  }

  function error(msg) {
    atEnd();
    response.prepareError(pRef, js, msg);
  }

  function doIt(b, next) {
    var modbusCall = false;
    console.log('FunctionCode: ' + functioncode);
    switch (functioncode) {
      case 'ReadCoils':
        modbusCall = 'readCoils';
        error('not implemented!');
      break;
      case 'ReadHoldingRegisters':
        modbusCall = 'readHoldingRegisters';
      break;
      case 'WriteSingleRegister':
        modbusCall = 'writeSingleRegister';
        error('coming soon');
      break;
      default: error('unknown function code');
    }
    if (modbusCall) {
      var options = {
        interval: -1,
        onComplete: function(err, resp) {
          //error('coming soon');
        },
        onError: function(err) {
          console.log('onError: ' + err);
          error(err);  // err.message
        }
      };
      master.once('connected', function() {
        var t1 = master[modbusCall](address, quantity, {
          interval: -1,
          onComplete: function(err, resp) {
            if (err) {
              console.error(err.message);
            } else if (resp.isException()) {
              console.error(resp.toString());
            } else {
              var values = resp.getValues();
              console.log('onComplete: ');
              logger.debug(resp.toString());
              // values = Big-Endian (most significant byte first)
              var view8 = correctEndian(new Uint8Array(values));
              var reduce = false; // TODO: Anders machen!
              if (reduce) view8 = reduceElements(view8);
              var arrBuf = view8.buffer;
              var view16 = new Uint16Array(arrBuf);
              // console.log(util.inspect(view8));
              // console.log(util.inspect(view16));
              if (false) {
                console.log('OutMod: "Uint8"');
                console.log(JSON.stringify(Array.from(view8)));
                console.log('OutMod: "Uint16"');
                console.log(JSON.stringify(Array.from(view16)));
                console.log('OutMod: "16Bits"');
                var bitArr1a = [];
                for (var i=0; i<view16.length; i++) {
                  bitArr1a.push(Uint16toBitArray(view16[i]));
                }
                console.log(JSON.stringify(bitArr1a));
                console.log('OutMod: "8Bits"');
                var bitArr1b = [];
                for (var i=0; i<view16.length; i++) {
                  bitArr1b.push(Uint16toBitArray(view16[i], true));
                }
                console.log(JSON.stringify(bitArr1b));
                console.log('OutMod: "16Bits*"');
                var bitArr2a = [];
                bitArr2a = Uint16toBitArray(view16);
                console.log(JSON.stringify(bitArr2a));
                console.log('OutMod: "8Bits*"');
                var bitArr2b = [];
                bitArr2b = Uint16toBitArray(view16, true);
                console.log(JSON.stringify(bitArr2b));
              } else {
                var bitArr1b = [];
                for (var i=0; i<view16.length; i++) {
                  bitArr1b.push(Uint16toBitArray(view16[i]));
                }
                for (var i=0; i<view16.length; i++) {
                  console.log((i + address) + ':\t' + bitArr1b[i]);
                }
                response.prepareResult(pRef, js, bitArr1b);
              }
            }
            //master.destroy();
          },
          onResponse: function(resp) {// ???
            //console.log('onResponse: ' + util.inspect(resp));
          },
          onError: function(err) {
            console.log('onError: ' + util.inspect(err));
          },

        });

        setTimeout(function() {
          master.destroy();
        }, 100);
      });
    }
  }

  var wait = js.Wait < cfg.MIN_TCP_WAIT ? cfg.MIN_TCP_WAIT : js.Wait;
  utils.repeat(js.Repeat, wait, doIt, function(repeatResult) {
    response.prepareResult(pRef, js, repeatResult);
  }, pRef, js);

}

exports.call = call;

