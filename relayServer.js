#!/usr/bin/env node

/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2019-01-25
 */

var cfg = require('./config.js');
var logger = cfg.logger;
var http = require('http');
var relay = require('./relay.js');

var server = http.createServer(relay.start);
server.listen(cfg.RELAY_PORT);
logger.info('relay server listen: ', cfg.RELAY_PORT);

// https://github.com/smartcomments/smartcomments
