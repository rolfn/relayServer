#!/usr/bin/env node

/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2019-10-21
 */

var cfg = require('./config.js');
var logger = cfg.logger = require('./logger');
var http = require('http');
var relay = require('./relay.js');

var server = http.createServer(relay.start);
server.listen(cfg.RELAY_PORT);
logger.info('relay server listen: ', cfg.RELAY_PORT);

// https://github.com/smartcomments/smartcomments
