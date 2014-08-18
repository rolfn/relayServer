/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 */


/**
 * Datenstruktur mit Default-Werten
 */
module.exports = {
  VERSION: '11.8.3',
  DATE: '2014-08-18',
  RELAY_PORT: 55555,
  DISPATCHER_PORT: 55565,
  GITLABHOOK_PORT: 3420,
  GITLABHOOK_HOST: '0.0.0.0',
  WEBSOCKET_PORT: 9001,
  DEFAULT_EXEC_TIMEOUT: 10000, // msec
  DEFAULT_EXEC_MAXBUFFER: 50 * 1024 * 1024,
  MIN_EXEC_WAIT: 50, // msec // ???
  MIN_VXI11_WAIT: 50, // msec
  MIN_TCP_WAIT: 250, // msec // ???
  DEFAULT_TCP_TIMEOUT: 2000, // msec
  DEFAULT_SMTP_HOST: 'smtp-hub',
  DEFAULT_SMTP_PORT: 25,
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

//for (var i in cfg) exports[i] = cfg[i];
//delete cfg;

