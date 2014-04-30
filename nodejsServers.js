#!/usr/bin/env node

/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2014-04-30
 */

var cfg = require('./config.js');
var winston = require('winston');
require('vwebsocket');
var logger = cfg.logger = require('vlogger')({
  transports: [
    new winston.transports.vWebsocket({
      level: 'debug',
      port: cfg.WEBSOCKET_PORT,
      handleExceptions: true,
      colorize: true,
      prettyPrint: true
    })
  ]
});
winston.remove(winston.transports.Console);

var http = require('http');
var relay = require('./relay.js');
// var dispatcher = require('./dispatcher.js');

var server1 = http.createServer(relay.start);
server1.listen(cfg.RELAY_PORT);
///if (cfg.isDebug) logger.enable(); else logger.disable();
///logger.info('logging: %s', cfg.isDebug);
logger.info('relay server listen (%d)\n', cfg.RELAY_PORT);

// TODO: Nachdenken, ob das Konzept eines zweiten vorgelagerten Servers
//       sinnvoll ist.
// var server2 = http.createServer(dispatcher.start);
// server2.listen(exports.DISPATCHER_PORT);

var glh = {
  port: cfg.GITLABHOOK_PORT,
  host: cfg.GITLABHOOK_HOST,
  logger: logger,
  configPathes: [__dirname, '/etc/gitlabhook', '/usr/local/etc/gitlabhook/']
};

var server3 = require('gitlabhook')(glh);
server3.listen();
if (server3.server) logger.info('webhook server listen (%d)\n', cfg.GITLABHOOK_PORT);

/**
<h4> Beispiele zur Kommunikation mit dem Relay-Server</h4>
<pre>
echo '{"Action":"/bin/echo","Value":"FRIDOLIN"}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"/usr/bin/which","Value":"pdftex"}' | \
  curl -T - -X PUT http://`hostname --fqdn`:55555

echo '{"Action":"_version"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"RANDOM"}' | \
  curl -T - -X PUT http://i75434.berlin.ptb.de:55555

echo '{"Action":"TIME","Repeat":3,"Wait":2000}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"VXI11","Host":"e75481",
  "Device":"gpib0,5","Value":"*IDN?"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"/usr/bin/Rscript", "Value":["foo","bar"],
  "Body":"print(17+4)"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"TCP","Repeat":3,"Wait":2000,"Host":"e75493","Port":"23",
  "Value":"exit\r"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"HTTP","Url":"http://a73434.berlin.ptb.de"}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"EMAIL", "Host": "smtp-hub", "Subject": "Grüße von NodeJS",
  "From": "Homunculus ","To": "Thomas.Bock@ptb.de",
  "Body": "Hallo, wie geht es Dir?\nHeute scheint die Sonne."}' | \
   curl -T - -X PUT http://localhost:55555

echo '{"Action":"TEX","Body":"\\documentclass{article}\\begin{document}
  Hello world!!!\\end{document}"}' | \
    curl -T - -X PUT http://localhost:55556 > zz.pdf

echo '{"Action":"UDP","Host":"192.168.98.15","Port":4165,"Value":"Sw_on2adminanel"}' | \
  curl -T - -X PUT http://localhost:55555

</pre>
*/
