#!/usr/bin/env node

/**
 *   @author Rolf Niepraschk (Rolf.Niepraschk@gmx.de)
 *   2019-01-24
 */

var io = require('socket.io-client');
var host = process.argv[2] ? process.argv[2] : 'localhost';
var port = 9001;
var socket = io.connect('ws://' + host + ':' + port);

function onReconnect() {
  console.log('»' + socket.id + '« reconnected to »' + host + '«');
}
function onConnect() {
  console.log('»' + socket.id + '« connected to »' + host + '«');
}
function onDisconnect() {
  console.log('disconnected');
  id = undefined;
}
function onError(e) {
  // ...
  console.log('----------------------------------');
  console.log(e);
  console.log('----------------------------------');
}
function serverLog(data) {
  console.log(data);
}

socket.on('connect', onConnect);
socket.on('reconnect', onReconnect);
socket.on('disconnect', onDisconnect);
socket.on('logging', serverLog);
socket.on('connect_failed', onError);
socket.on('reconnect_failed', onError);
socket.on('error', onError);

