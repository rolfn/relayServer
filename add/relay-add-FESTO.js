
var cfg = require('../config.js');
var inspect = require('util').inspect;
var request = require('request');

function getDigitalInput() {// für PostProcessing
}

/**
 * Als Eingangs-JSON-Daten reichen die folgenden:
 *   {"Host":"172.30.56.46","PreProcessing":"_.getValveState(this);"}
 * und ggf. '"VNb":...'
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
/*
$ cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"TIME","PreProcessing":"_.foo(this);"}
EOF
*/

/**
 * 
 *
 * @author Rolf Niepraschk
 * @param 
 * @return 
 */ 
function setValveState(ctx) {// für PreProcessing
  var _x = ctx._x;
  var callbacks = ctx._callbacks
  //console.log('foo: ' + inspect(ctx));
  function bar() {
    _x.Action = 'RANDOM';
  }
  ctx._addCallback(bar);
  setTimeout(function() {
    bar();
    ctx._removeCallback(bar);
  }, 3000);
  /*
  var jdata = {
    Host:_x.Host, Quantity:2, // 4?
    VNb:5, Open:true,
    FunctionCode:'ReadHoldingRegisters', OutMode:'Uint16' 
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
    //if (err) throw err;
    if (!err) {    
      var d = typeof _d === 'string' ? JSON.parse(_d) : _d, v_data, v_old; 
      if (_x.VNb < 17) {
        v_data = _x.VNb;
        v_old = d.Result[0];
        _x.Address = 40003;
      } else {
        v_data = _x.VNb-16;
        v_old = d.Result[8]; // [?]
        _x.Address = 40003+4; // +1?       
      }
      _x.Action = 'MODBUS';
      _x.Value = _x.Open ? v_old | (1<<v_data-1) : v_old & ~(1<<v_data-1);
      _x.FunctionCode = 'writeSingleRegister';
    }
    ctx._removeCallback(stateResponse);   
  }
  ctx._addCallback(stateResponse);
   
  request(opts, stateResponse);
  
  */
}

exports.getValveState = getValveState;
exports.getValveState2 = getValveState2;
exports.setValveState = setValveState;

