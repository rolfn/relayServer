
// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-09

const MODULE = 'config';

var cfg = {
  VERSION: '7.0a, 2013-01-09',
  //RELAY_PORT: 55555,
  RELAY_PORT: 61111,
  DISPATCHER_PORT: 55565,
  DEFAULT_EXEC_TIMEOUT: 10000, // msec
  DEFAULT_EXEC_MAXBUFFER: 50 * 1024 * 1024,
  MIN_EXEC_WAIT: 50, // msec // ???
  MIN_TCP_WAIT: 250, // msec // ???
  DEFAULT_SMTP_HOST: 'smtp-hub',
  DEFAULT_SMTP_PORT: 25,
  DEFAULT_TEX_MAXRUNS: 5,
  DEFAULT_TEX_SRCFMT: 'LaTeX',
  DEFAULT_TEX_DESTFMT: 'PDF',
  bin: {
    VXITRANSCEIVER: '/usr/local/bin/vxiTransceiver',
    RSCRIPT: '/usr/bin/Rscript',
    DATE: '/bin/date',
    SLEEP: '/bin/sleep',
    ECHO: '/bin/echo',
    TEXCALLER: '/usr/local/bin/texcaller',
    WHICH: '/usr/bin/which'
  },
  env: {}
}

for (var i in cfg) exports[i] = cfg[i];

delete cfg;

