/**
 *   @author Rolf Niepraschk (Rolf.Niepraschk@gmx.de)
 *   2019-01-25
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
  const filename = path.basename(logCaller.getFileName()),
    linenumber = logCaller.getLineNumber(),
    functionname =  logCaller.getFunctionName() || '<anonymous>';
  var ret = `${info.timestamp} [${filename}:${linenumber}:${functionname}]\n`;  
  ret = ret + `${info.message === Object(info.message) ? 
    inspect(info.message, inspectOpts) : info.message}`;
  if (typeof info.meta !== 'undefined') {
    ret = ret + `${info.meta === Object(info.meta) ? 
      inspect(info.meta, inspectOpts) : info.meta}`;
  }  
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
