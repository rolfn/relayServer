
/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2017-01-13
 */

var cfg = require('../config.js');
//var inspect = require('util').inspect;
var request = require('request');

const V_WRITE_ADR = 40003;
const V_READ_ADR  = 45407;
const D_READ_ADR  = 45395;
const V_QUANTITY  = 20;

/**
 * Eingangs-JSON-Daten:
 *   {"Host":"172.30.56.46","PreProcessing":"_.getValveState(this);"}
 * und ggf. '"VNb":(1..20)'
 * Alle anderen Parameter setzt diese Funktion.
 */
function getValveState(ctx) {// für PreProcessing
  ctx.Action = 'MODBUS';
  ctx.FunctionCode = 'ReadHoldingRegisters';
  ctx.OutMode = '8Bits*';
  ctx.Address = V_READ_ADR;
  ctx.Skip = 1;
  ctx.Quantity = V_QUANTITY / 4 * 2 - 1;
  // 4 Ventil-Bits pro 16-Bit-Register und jeweils nächstes 16-Bit-Register
  // ist ungenutzt und wird übersprungen; die 8 höherwertigen Bits ignorieren.
}

/**
 * Eingangs-JSON-Daten (Beispiel):
 *   {"Host":"172.30.56.46","PreProcessing":"_.setValveState(this);",
 *    "VNb":9, Open":true}
 * Alle anderen Parameter setzt diese Funktion. Dazu wird vorher der bisherige
 * Status des zugehörigen Registers erfragt und der neu zu schreibende Wert
 * errechnet.
 */
function setValveState(ctx) {// für PreProcessing
  var o = ctx._x;
  var VNb = parseInt(o.VNb);
  if (!o.Host || VNb < 1 || VNb > 20 || typeof o.Open == 'undfined') return;
  var adr = V_READ_ADR;

  if (VNb > 16) adr+=2;
  if (VNb > 12) adr+=2;
  if (VNb >  8) adr+=2;
  if (VNb >  4) adr+=2;

  var jdata = {
    Host:o.Host, Address:adr, Quantity:1,
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
        v_old = d.Result, adr = V_WRITE_ADR, v_data = VNb;
      if (VNb > 16) {
        adr++;
        v_data-=4;
      }
      if (VNb > 12) {
        adr++;
        v_data-=4;
      }
      if (VNb >  8) {
        adr++;
        v_data-=4;
      }
      if (VNb >  4) {
        adr++;
        v_data-=4;
      }
      if (VNb > 16) {
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
 * und ggf. '"PinNb":(1..48)'
 * Alle anderen MODBUS-Parameter setzt diese Funktion.
 */
function getDigitalInput(ctx) {// für PreProcessing
  ctx.Action = 'MODBUS';
  ctx.FunctionCode = 'ReadHoldingRegisters';
  ctx.Address = D_READ_ADR;
  ctx.Quantity = 11;
  ctx.Skip = 1;
  ctx.OutMode = '8Bits*';
}

exports.getValveState = getValveState;
exports.setValveState = setValveState;
exports.getDigitalInput = getDigitalInput;

/*

Schreibregister für Ventile 1..20
=================================
40003:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  |  | x|  | x|  | x|  | x|
                             4     3     2     1   <-- Ventilnummer
40004:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  |  | x|  | x|  | x|  | x|
                             8     7     6     5   <-- Ventilnummer
...
40007:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  | x| x| x| x| x| x| x| x|
                          ^20^  ^19^  ^18^  ^17^   <-- Ventilnummer

Leseregister für Ventile 1..20
==============================
45407:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  |  | x|  | x|  | x|  | x|
                             4     3     2     1   <-- Ventilnummer
45409:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  |  | x|  | x|  | x|  | x|
                             8     7     6     5   <-- Ventilnummer
...
45415:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  | x| x| x| x| x| x| x| x|
                          ^20^  ^19^  ^18^  ^17^   <-- Ventilnummer

Für die Ventile 17..20 werden 2 Bitpositionen verwendet (2-Wege).


Leseregister für Digitaleingänge 1..48
======================================
45395:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  | x| x| x| x| x| x| x| x|
                          8  7  6  5  4  3  2  1   <-- Nr. des Digitaleingangs
45397:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  | x| x| x| x| x| x| x| x|
                         16 15 14 13 12 11 10  9   <-- Nr. des Digitaleingangs
...
45405:
 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0   <-- Bitnummer
|  |  |  |  |  |  |  |  | x| x| x| x| x| x| x| x|
                         48 47 46 45 44 43 42 41   <-- Nr. des Digitaleingangs

*/
