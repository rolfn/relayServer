
/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2016-12-01
 */

var cfg = require('../config.js');
//var inspect = require('util').inspect;
var request = require('request');

/**
 * Eingangs-JSON-Daten:
 *   {"Host":"172.30.56.46","PreProcessing":"_.getValveState(this);"}
 * und ggf. '"VNb":(1..32)' 
 * Alle anderen Parameter einschließlich "PostProcessing" setzt
 * diese Funktion.
 */ 
function getValveState(ctx) {// für PreProcessing
  ctx.Action = 'MODBUS';
  ctx.FunctionCode = 'ReadHoldingRegisters';
  ctx.OutMode = '16Bits*';
  ctx.PostProcessing = 'Result=_.getValveState2(this);';
  ctx.Address = 45407;
  ctx.Quantity = 9;
}

/**
 * Ist in der JSON-Struktur VNb angegeben, wird eine einzelner boolean-Wert
 * zurückgeliefert, sonst ein Array von 32 boolean-Werten (20 reale).
 *
 * @return boolean-Wert oder Array von boolean-Werten
 */ 
function getValveState2(ctx) {// für PostProcessing
  var x = ctx._x, VNb = ctx._$.VNb;
  var a = [];
  if (!x.length || x.length < 136) return null;
  for (var j=0; j<136; j+=32) {
    for (var i=0; i<8; i+=2) {
      a.push(!!x[j+i]);
    }
  }
  if (typeof VNb == 'number' && VNb > 0 && VNb < 21) {
    return a[VNb-1]
  } else {
    return a
  }
}

/**
 * Eingangs-JSON-Daten (Beispiel):
 *   {"Host":"172.30.56.46","PreProcessing":"_.setValveState(this);",
 *    "VNb": 9, Open":true}
 * Alle anderen Parameter einschließlich "PostProcessing" setzt
 * diese Funktion. Dazu wird vorher der bisherige Status des zugehörigen
 * Registers erfragt und der neu zu schreibende Wert errechnet.
 */ 
function setValveState(ctx) {// für PreProcessing
  var o = ctx._x;
  if (!o.Host || typeof o.VNb != 'number' || o.VNb < 1 || o.VNb > 20 ||
    typeof o.Open == 'undfined') return;
  var adr = 45407;
  
  if (o.VNb > 16) adr+=2;
  if (o.VNb > 12) adr+=2;
  if (o.VNb >  8) adr+=2;
  if (o.VNb >  4) adr+=2;
  
  var jdata = {
    Host:o.Host, VNb:o.VNb, Open:o.Open, Address:adr, Quantity:1,
    Action:'MODBUS', FunctionCode:'ReadHoldingRegisters', OutMode:'Uint16' 
  };  
  var opts = {
    url: 'http://localhost:' + cfg.RELAY_PORT,
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jdata)
  };  
  function stateResponse(err, res, _d) {
    if (!err) {    
      var d = typeof _d === 'string' ? JSON.parse(_d) : _d, 
        v_old = d.Result, adr = 40003, v_data = o.VNb;
      if (o.VNb > 16) {
        adr++;
        v_data-=4;
      }
      if (o.VNb > 12) {
        adr++;
        v_data-=4;
      }
      if (o.VNb >  8) {
        adr++;
        v_data-=4;
      }
      if (o.VNb >  4) {
        adr++;
        v_data-=4;
      }
      if (o.VNb > 16) {
        // TODO: Sonderbehandlung Ventile 17..20
        v_data = 1 << 2*(v_data-1); // <-- anpassen!
      } else {
        v_data = 1 << 2*(v_data-1);
      }
      o.Address = adr;
      o.Action = 'MODBUS';
      o.FunctionCode = 'writeSingleRegister';
      o.Value = o.Open ? v_old | v_data : v_old & ~v_data;
    }
    ///console.log('stateResponse 1:' + inspect(opts));
    ctx._busy--;   
  }
  ctx._busy++;     
  request(opts, stateResponse);// Abfrage des vorherigen Status
}

/**
 * Eingangs-JSON-Daten (Beispiel):
 *   {"Host":"172.30.56.46","PreProcessing":"_.getDigitalInput(this);"}
 * und ggf. '"PinNb":(1..32)' 
 * Alle anderen MODBUS-Parameter einschließlich "PostProcessing" setzt
 * diese Funktion.
 * 
 * @author Rolf Niepraschk
 */ 
function getDigitalInput(ctx) {// für PreProcessing
  ctx.Action = 'MODBUS';
  ctx.FunctionCode = 'ReadHoldingRegisters';
  ctx.Address = 45395; 
  ctx.Quantity = 11; 
  ctx.Skip = 1; 
  ctx.OutMode = '8Bits*';
  ctx.PostProcessing = 'Result=_.getDigitalInput2(this);';
}

/**
 * Ist in der JSON-Struktur PinNb angegeben, wird eine einzelner boolean-Wert
 * zurückgeliefert, sonst ein Array von 48 boolean-Werten.
 *
 * @author Rolf Niepraschk
 * @return boolean-Wert oder Array von boolean-Werten
 */ 
function getDigitalInput2(ctx) {// für PostProcessing
  var x = ctx._x, PinNb = ctx._$.PinNb;
  var a = [];
  for (var i=0; i<x.length; i++) {
    a.push(!!x[i]);
  } 
  if (typeof PinNb == 'number' && PinNb > 0 && PinNb <= x.length) {             
    return a[PinNb-1]
  } else {
    return a
  }
}

exports.getValveState = getValveState;
exports.getValveState2 = getValveState2;
exports.setValveState = setValveState;
exports.getDigitalInput = getDigitalInput;
exports.getDigitalInput2 = getDigitalInput2;
