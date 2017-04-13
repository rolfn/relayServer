/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2017-04-10
 */

var fs = require('fs');

/**
 * Datenstruktur mit Default-Werten
 */
var cfg = {
  // Nur wenn sie mit '?' beginnt, wird Eintrag aus "package.json" verwendet
  VERSION: '12.9.0-pre2', 
  DATE: '2017-04-12',
  RELAY_PORT: 55555,
  WEBSOCKET_PORT: 9001,
  DEFAULT_EXEC_TIMEOUT: 60000, // msec
  DEFAULT_EXEC_MAXBUFFER: 50 * 1024 * 1024,
  MIN_EXEC_WAIT: 50, // msec // ???
  MIN_VXI11_WAIT: 50, // msec
  MIN_TCP_WAIT: 250, // msec // ???
  MIN_UDP_WAIT: 250, // msec
  MIN_MODBUS_WAIT: 250, // msec
  DEFAULT_TCP_TIMEOUT: 30000, // msec
  DEFAULT_UDP_TIMEOUT: 30000, // msec
  DEFAULT_SMTP_PORT: 25,
  DEFAULT_MODBUS_PORT: 502,
  DEFAULT_MODBUS_OUTMODE: 'Uint16',
  DEFAULT_XLSX_NAME: 'data.xlsx',
  DEFAULT_TEX_RUNS: 2,
  DEFAULT_TEX_CMD: 'pdflatex',
  DEFAULT_TEX_DESTFMT: 'pdf',
  DEFAULT_TEX_OUTNAME: 'output',
  TEX_CMDS: ['pdftex', 'pdflatex', 'xetex', 'xelatex', 'luatex', 'lualatex'],
  TEX_FILE: 'texput.tex',
  TEX_ERROR_FILE: 'texerror.tex',
  PRG_FILE: 'prg.dat',
  // Reihenfolge bestimmt Wichtigkeit
  RELEASE_FILES: ['/etc/os-release','/etc/SuSE-release','/etc/redhat-release',
    '/etc/mandrake-release','/etc/gentoo-release','/etc/slackware-release',
    '/etc/release'],
  bin: {
    RSCRIPT: '/usr/bin/Rscript',
    PYTHON: '/usr/bin/python',
    DATE: '/bin/date',
    SLEEP: '/bin/sleep',
    ECHO: '/bin/echo',
    WHICH: '/usr/bin/which'
  },
  theRepeats: {}
};

try {
  var fname = __dirname + '/package.json';
  if (cfg.VERSION[0] == '?') {// nur, wenn nicht Test-Version
    fs.stat(fname, function(err, stats) {
      if (!err) {
        var t = stats.mtime;
        cfg.DATE = t.getFullYear() + '-' +
          ("0" + (t.getMonth() + 1)).slice(-2) + '-' +
          ("0" + (t.getDate())).slice(-2);
        var data = JSON.parse(fs.readFileSync(fname, 'utf-8'));
        if (data.version) cfg.VERSION = data.version;
      }
    });
  }
} catch(err) {
}

var winston = require('winston');
require('vwebsocket');
cfg.logger = require('vlogger')({
  transports: [
    new winston.transports.vWebsocket({
      level: 'silly',
      port: cfg.WEBSOCKET_PORT,
      handleExceptions: true,
      colorize: true,
      prettyPrint: true
    })
  ]
});
winston.remove(winston.transports.Console);

module.exports = cfg;
