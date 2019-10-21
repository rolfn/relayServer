/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 */

var fs = require('fs'), pkg = require('./package.json');

/**
 * Datenstruktur mit Default-Werten
 */
 
var cfg = {
  VERSION: pkg.version, 
  DATE: '2019-10-21',
  RELAY_PORT: 55555,
  WEBSOCKET_PORT: 9001,
  GRAYLOG_URL: 'i75422.berlin.ptb.de',
  GRAYLOG_PORT: 12201,
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
  theRepeats: {},
  vxi11_last_time: 0
};

module.exports = cfg;
