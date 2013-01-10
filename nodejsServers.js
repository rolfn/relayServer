#!/usr/bin/env node

// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'nodejsServers';

var http = require('http');
var cfg = require('./config.js'); 
var relay = require('./relay.js');
// var dispatcher = require('./dispatcher.js');

var server1 = http.createServer(relay.start);
server1.listen(cfg.RELAY_PORT);

/*
var server2 = http.createServer(dispatcher.start);
server2.listen(exports.DISPATCHER_PORT);
*/
