#!/usr/bin/env node

const MODUL = 'nodejsServers';

var cfg = require('./config.js'); 
var tools = require('./tools.js');
var relay = require('./relay.js');

console.log(cfg);

console.log(cfg.VERSION);
console.log('------------------------------');
for (var i in cfg.bin) {
  console.log(i + ':' + cfg.bin[i]);
}
console.log('------------------------------');

function analyzeActions_1(body, pRef) {

  console.log('body: ' + body);
  console.log('pRef: ' + pRef);

}

tools.getEnv(cfg.env, analyzeActions_1, 'HUGO', 'GUSTAV');

  console.log('MODUL: ' + MODUL);
  console.log(cfg.env); // zu früh!
  console.log('------------------------------');

/*
var server1 = http.createServer(relay.start);
server1.listen(exports.RELAY_PORT);
*/
/*
var server2 = http.createServer(dispatcher.start);
server2.listen(exports.DISPATCHER_PORT);
*/
