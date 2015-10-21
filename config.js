/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 */

/**
 * Datenstruktur mit Default-Werten
 */
var cfg = {
  VERSION: '12.0.1',
  DATE: '2015-10-20',
  RELAY_PORT: 55555,
  WEBSOCKET_PORT: 9001,
  DEFAULT_EXEC_TIMEOUT: 30000, // msec
  DEFAULT_EXEC_MAXBUFFER: 50 * 1024 * 1024,
  MIN_EXEC_WAIT: 50, // msec // ???
  MIN_VXI11_WAIT: 50, // msec
  MIN_TCP_WAIT: 250, // msec // ???
  MIN_UDP_WAIT: 250, // msec
  MIN_MODBUS_WAIT: 250, // msec
  DEFAULT_TCP_TIMEOUT: 30000, // msec
  DEFAULT_UDP_TIMEOUT: 30000, // msec
  DEFAULT_SMTP_HOST: 'smtp-hub',
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
  R_FILE: 'cmd.R',
  // Reihenfolge bestimmt Wichtigkeit
  RELEASE_FILES: ['/etc/os-release','/etc/SuSE-release','/etc/redhat-release',
    '/etc/mandrake-release','/etc/gentoo-release','/etc/slackware-release',
    '/etc/release'],
  bin: {
    RSCRIPT: '/usr/bin/Rscript',
    DATE: '/bin/date',
    SLEEP: '/bin/sleep',
    ECHO: '/bin/echo',
    WHICH: '/usr/bin/which'
  },
  theRepeats: {}
};

var winston = require('winston');
require('vwebsocket');
cfg.logger = require('vlogger')({
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

module.exports = cfg;
