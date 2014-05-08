/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2014-05-08
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var xlsx = require('node-xlsx');

var logger = cfg.logger;

/**
 * Konfiguration der nötigen Datenstrukturen.
 * Wait/Repeat wird nicht unterstützt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function toXLSX(pRef, js) {
  var params = {};
  params.worksheets = js.Value;
  logger.debug('params: ', params);
  try {
    var buf = xlsx.build(params);
    var filename = js.Filename ? js.Filename : cfg.DEFAULT_XLSX_NAME;
    js.OutputType = 'stream';
    js.OutputEncoding = 'binary';// TODO: Kann das weg?
    js.Head = {};
    js.Head['Content-Type'] =
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';
    // application/ms-excel ???
    js.Head['Content-Disposition'] = 'attachment; filename=' + filename;
    response.prepareResult(pRef, js, buf);
  } catch(e) {
    logger.error(e.toString());
    response.prepareError(pRef, js, 'xlsx creation error');
  }
}

function fromXLSX(pRef, js) {
  try {
    var data = xlsx.parse(new Buffer(js.Value, 'base64'));
    response.prepareResult(pRef, js, data);
  } catch(e) {
    logger.error(e.toString());
    response.prepareError(pRef, js, 'xlsx convert error');
  }
}

exports.toXLSX = toXLSX;
exports.fromXLSX = fromXLSX;

