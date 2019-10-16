/**
 *   @author Rolf Niepraschk (Rolf.Niepraschk@gmx.de)
 *   2019-02-05
 */

const io = require('socket.io');
const inspect = require('util').inspect;
const bunyan = require('bunyan');
const bunyanDebugStream = require('bunyan-debug-stream');
const BunyanToGelfStream = require('bunyan-gelf');

function SocketStream(options) {
  this.writable = true;
  socket = io.listen(9001);
  socket.sockets.on('connection', function (client) {
    logger.info(`\n[${client.request.headers.host}]: »${client.id}« connected`);
    client.on('disconnect', function () {
      //console.log('client ' + '»' + client.id + '« disconnected');
    });
  }); 
}

SocketStream.prototype.write = function (record) {
  //console.log(record);
  socket.sockets.emit('logging', record);
  return true;
};

var socket, socketStream = new SocketStream();

function formateDate(d) {
  return d.getFullYear() + '-' + ('0'+(d.getMonth()+1)).slice(-2) + '-' + 
    ('0' + d.getDate()).slice(-2) + ' ' + ('0' + d.getHours()).slice(-2) + ':' + 
    ('0' + d.getMinutes()).slice(-2) + ':' + ('0' + d.getSeconds()).slice(-2);
}

var logger = bunyan.createLogger({
  name: 'vlLogging',
  src: true,
  serializers: bunyan.stdSerializers,
  streams: [{
    level: 'debug',
    type: 'raw',    // use 'raw' to get raw log record objects
    //type: 'stream', 
    stream: bunyanDebugStream({
      basepath: __dirname, // this should be the root folder of your project.
      useColor: true,
      forceColor: true,
      showLoggerName: false,
      showProcess: false,
      showPid: false,
      showLevel: true,
      showMetadata: true,
      showDate: formateDate,
      out: socketStream
    })
  },
  {
    type: 'raw',
    level: 'trace',
    stream: new BunyanToGelfStream({
      host: '172.30.56.22', 
      port: 12201,
    })
   }],
  //serializers: bunyanDebugStream.serializers
});

module.exports = logger;
