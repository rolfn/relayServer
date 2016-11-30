
var cfg = require('../config.js');
// var inspect = require('util').inspect;
var request = require('request');

/**
 * Eingangs-JSON-Daten:
 *   {"Host":"172.30.56.46","PreProcessing":"_.getValveState(this);"}
 * und ggf. '"VNb":(1..32)' 
 * Alle anderen MODBUS-Parameter einschließlich "PostProcessing" setzt
 * diese Funktion.
 * 
 * @author Rolf Niepraschk
 */ 
function getValveState(ctx) {// für PreProcessing
  ctx.Action = 'MODBUS';
  ctx.FunctionCode = 'ReadHoldingRegisters';
  ctx.Address = 45407; // ???
  ctx.Quantity = 2; // ???
  ctx.OutMode = '16Bits*';
  ctx.PostProcessing = 'Result=_.getValveState2(this);';
}

/**
 * Ist in der JSON-Struktur VNb angegeben, wird eine einzelner boolean-Wert
 * zurückgeliefert, sonst ein Array von 32 boolean-Werten.
 *
 * @author Rolf Niepraschk
 * @return boolean-Wert oder Array von boolean-Werten
 */ 
function getValveState2(ctx) {// für PostProcessing
  var x = ctx._x, VNb = ctx._$.VNb;
  var a = [];
  for (var i=0; i<x.length; i++) {// 32?
    a.push(x & (1<<i) ? true : false);
  } // auf zwei 16Bit-Werte ausweiten.
  if (typeof VNb == 'number') {
    return a[VNb]
  } else {
    return a
  }
}

/**
 * Eingangs-JSON-Daten (Beispiel)
 *   {"Host":"172.30.56.46","PreProcessing":"_.setValveState(this);",
 *    "VNb": 9, Open":true}
 * Alle anderen MODBUS-Parameter einschließlich "PostProcessing" setzt
 * diese Funktion. Dazu wird vorher der bisherige Status des zugehörigen
 * Registers erfragt und der neu zu schreibende Wert errechnet.
 * 
 * @author Rolf Niepraschk
 */ 
function setValveState(ctx) {// für PreProcessing
  if (!ctx.Host || !ctx.VNb || typeof ctx.Open == 'undfined') return;
  var jdata = {
    Host:ctx.Host, VNb:ctx.VNb, Open:ctx.Open, 
    Address: ctx.VNb < 17 ? 45407 : 45415,
    Quantity:1, FunctionCode:'ReadHoldingRegisters', OutMode:'Uint16' 
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
      var d = typeof _d === 'string' ? JSON.parse(_d) : _d, v_data, v_old; 
      if (dtx.VNb < 17) {
        v_data = dtx.VNb;
        dtx.Address = 40003;
      } else {
        v_data = dtx.VNb - 16;
        dtx.Address = 40007;  
      }
      v_old = d.Result
      dtx.Action = 'MODBUS';
      dtx.FunctionCode = 'writeSingleRegister';
      dtx.Value = dtx.Open ? v_old | (1<<v_data-1) : v_old & ~(1<<v_data-1);
    }
    ctx._removeCallback(stateResponse);   
  }
  ctx._addCallback(stateResponse);     

  request(opts, stateResponse);// Abfrage des vorherigen Status
}

/**
 * Eingangs-JSON-Daten (Beispiel)
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
  ctx.Address = 45395; // ???
  ctx.Quantity = 11; // ???
  ctx.Skip = 1; // ???
  ctx.OutMode = '8Bits*';
  ctx.PostProcessing = 'Result=_.getDigitalInput2(this);';
}

/**
 * Ist in der JSON-Struktur PinNb angegeben, wird eine einzelner boolean-Wert
 * zurückgeliefert, sonst ein Array von 40 boolean-Werten.
 *
 * @author Rolf Niepraschk
 * @return boolean-Wert oder Array von boolean-Werten
 */ 
function getDigitalInput2(ctx) {// für PostProcessing
  var x = ctx._x, PinNb = ctx._$.PinNb;
  var a = [];
  for (var i=0; i<x.length; i++) {// 32?
    a.push(x & (1<<i) ? true : false);
  } // auf zwei 16Bit-Werte ausweiten.
  if (typeof PinNb == 'number') {
    return a[PinNb]
  } else {
    return a
  }
}

exports.getValveState = getValveState;
exports.getValveState2 = getValveState2;
exports.setValveState = setValveState;
exports.getDigitalInput = getDigitalInput;
exports.getDigitalInput2 = getDigitalInput2;
