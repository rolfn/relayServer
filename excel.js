/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2014-05-12
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var xlsx = require('node-xlsx');

var logger = cfg.logger;

function simplify(d) {
  for (var i=0; i<d.worksheets.length; i++) {
    for (var j=0; j<d.worksheets[i].data.length; j++) {
      for (var k=0; k<d.worksheets[i].data[j].length; k++) {
        var v = d.worksheets[i].data[j][k].value;
        d.worksheets[i].data[j][k] = v;
      }
    }
  }
  return d;
}

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
    js.Head = {};
    js.Head['Content-Type'] =
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';
    // 'application/ms-excel' ???
    js.Head['Content-Disposition'] = 'attachment; filename=' + filename;
    response.prepareResult(pRef, js, buf);
  } catch(e) {
    logger.error(e.toString());
    response.prepareError(pRef, js, 'xlsx creation error');
  }
}

function fromXLSX(pRef, js) {
  try {
    logger.debug('Value.length: %d', js.Value.length);
    utils.addStartTime(js);
    var data = xlsx.parse(new Buffer(js.Value, 'base64'));
    utils.addStopTime(js);
    var short = (typeof js.ShortFormat == 'boolean') ? js.ShortFormat : true;
    response.prepareResult(pRef, js, short ? simplify(data) : data);
  } catch(e) {
    logger.error(e.toString());
    response.prepareError(pRef, js, 'xlsx convertion error');
  }
}

exports.toXLSX = toXLSX;
exports.fromXLSX = fromXLSX;

