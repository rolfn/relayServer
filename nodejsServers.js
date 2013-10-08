#!/usr/bin/env node

/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-10-08
 */

const MODULE = 'nodejsServers';

var http = require('http');
var cfg = require('./config.js');
var relay = require('./relay.js');
// var dispatcher = require('./dispatcher.js');

var server1 = http.createServer(relay.start);
server1.listen(cfg.RELAY_PORT);

// TODO: Nachdenken, ob das Konzept eines zweiten vorgelagerten Servers
//       sinnvoll ist.
// var server2 = http.createServer(dispatcher.start);
// server2.listen(exports.DISPATCHER_PORT);


var tools = require('./tools.js');
debug = tools.createFunction('debug', 'GITLABHOOK');

var logger = {
  log:  function(s){debug('', '', s)},
  error:function(s){debug('', '', s)}
}

logger = undefined;

var glh = {
  port: cfg.GITLABHOOK_PORT,
  host: cfg.GITLABHOOK_HOST,
  logger: logger,
  configPathes: ['/etc/gitlabhook', '/usr/local/etc/gitlabhook/', __dirname]
};

var server3 = require('gitlabhook')(glh);
server3.listen();

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

echo '{"Action":"/usr/local/bin/vxiTransceiver","Host":"e75481",
  "Device":"gpib0,5","Value":"*IDN?"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"/usr/bin/Rscript", "Value":["foo","bar"],
  "Body":"print(17+4)"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"TCP","Repeat":3,"Wait":2000,"Host":"e75493","Port":"23",
  "Value":"exit\r"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"HTTP","Url":"http://a73434.berlin.ptb.de"}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"EMAIL", "Host": "smtp-hub", "Subject": "GrÃ¼Ãe von NodeJS",
  "From": "Homunculus ","To": "Thomas.Bock@ptb.de",
  "Body": "Hallo, wie geht es Dir?\nHeute scheint die Sonne."}' | \
   curl -T - -X PUT http://localhost:55555

echo '{"Action":"LaTeX","Source":"\\documentclass{article}\\begin{document}
  Hello world!!!\\end{document}","OutputType":"stream"}' | \
    curl -T - -X PUT http://localhost:55556 > zz.pdf
</pre>
*/
