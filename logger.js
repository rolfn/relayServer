/**
 *   @author Rolf Niepraschk (Rolf.Niepraschk@gmx.de)
 *   2019-01-28
 */

const { createLogger, format, transports } = require('winston');
const SocketIOserver = require('./socketio-server-transport');
const stackTrace = require('stack-trace');
const path = require('path');
const inspect = require('util').inspect;

const inspectOpts = {
  depth:null, colors:true, maxArrayLength:255, breakLength:60, compact:true   
}

function formatParams(info) {
  const { timestamp, level, message, message2 } = info, trace = stackTrace.get();
  var logCaller;
  for (var i=0; i<trace.length; i++) {
    if (trace[i].getFileName().indexOf('winston/create-logger.js') > -1) {
      logCaller = trace[i+1];
      break;
    }
  }
  function fmt(_o) {
    if (typeof _o === 'undefined') return '';
    var o = Array.isArray(_o) ? _o : [_o], ret = '';
    for (var i=0; i<o.length; i++) {
      ret =  ret + (o[i] === Object(o[i]) ? inspect(o[i], inspectOpts) : o[i]);
    }
    return ret;
  }
  //console.log(inspect(info));
  const filename = path.basename(logCaller.getFileName()),
    linenumber = logCaller.getLineNumber(),
    functionname =  logCaller.getFunctionName() || '<anonymous>';
  var ret = `${info.timestamp} [${filename}:${linenumber}:${functionname} `;
  ret = ret + `${level}]\n`;
  ret = ret + fmt(info.message) + fmt(info.meta);
  return ret;
}

const logger = createLogger({
  level: 'debug',
  handleExceptions: true,
  format: format.combine(
    format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
  ),
  transports: [
    new SocketIOserver({
      reconnect: true,
      format: format.combine(
        format.colorize(),
        format.splat(),
        format.printf(formatParams)
      )
    })
  ]
});

module.exports = logger;
