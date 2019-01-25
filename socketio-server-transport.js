/*
 * socketio-server-transport.js: 
 * A winston transport for emitting logs to a socket.io clients
 *
 * Author: Rolf Niepraschk, <Rolf.Niepraschk@ptb.de>
 * 2019-01-24
 */
const Transport = require('winston-transport');
const { MESSAGE } = require('triple-beam');
const inspect = require('util').inspect;
const io = require('socket.io');
const os = require('os');

//
// Inherit from `winston-transport` so you can take advantage
// of the base functionality and `.exceptions.handle()`.
//
module.exports = class SocketIOserver extends Transport {
  
  constructor(opts) {
    super(opts);
    opts = opts || {};

    this.default_format = function(level, message) {
      return {
        level : level,
        message : message
      };
    };
    
    this.name = 'socketioserver';
    this.port = opts.port || 9001;
    this.reconnect = opts.reconnect || false;
    this.namespace = opts.namespace || null;
    this.log_topic = opts.log_topic || 'log';
    this.log_format = opts.log_format || this.default_format;
    this.eol = opts.eol || os.EOL;
    
    this.socket = io.listen(this.port, {log:false});
    
    const self = this;
    
    this.socket.sockets.on('connection', function (client) {
      //console.log('client ' + '»' + client.id + '« connected');
      client.emit('logging', `... to »${client.request.headers.host}«`);
      client.on('disconnect', function () {
        //console.log('client ' + '»' + client.id + '« disconnected');
      });
    });    
    
  }    
  
  log(info, callback) {
    setImmediate(() => this.emit('logged', info));
    
    if (this.silent) {
      callback();
      return true;
    }
    
    if (this.socket && this.socket.sockets) {
      this.socket.sockets.emit('logging', `${info[MESSAGE]}${this.eol}`);
      //console.log(`${info[MESSAGE]}${this.eol}`);
    }
    
    if (callback) {
      callback(); 
    }
    
    return;
  }
};
