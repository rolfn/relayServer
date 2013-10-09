/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-10-08
 */

const MODULE = 'config';

/**
 * Datenstruktur mit Default-Werten
 */
var cfg = {
  VERSION: '8.0b',
  DATE: '2013-10-08',
  RELAY_PORT: 55555,
  DISPATCHER_PORT: 55565,
  GITLABHOOK_PORT: 3420,
  GITLABHOOK_HOST: '0.0.0.0',
  DEFAULT_EXEC_TIMEOUT: 10000, // msec
  DEFAULT_EXEC_MAXBUFFER: 50 * 1024 * 1024,
  MIN_EXEC_WAIT: 50, // msec // ???
  MIN_TCP_WAIT: 250, // msec // ???
  DEFAULT_TCP_TIMEOUT: 2000, // msec
  DEFAULT_SMTP_HOST: 'smtp-hub',
  DEFAULT_SMTP_PORT: 25,
  DEFAULT_TEX_MAXRUNS: 5,
  DEFAULT_TEX_SRCFMT: 'LaTeX',
  DEFAULT_TEX_DESTFMT: 'PDF',
  R_FILE: 'cmd.R',
  // Reihenfolge bestimmt Wichtigkeit
  RELEASE_FILES: ['/etc/os-release','/etc/SuSE-release','/etc/redhat-release',
    '/etc/mandrake-release','/etc/gentoo-release','/etc/slackware-release',
    '/etc/release'],
  bin: {
    VXITRANSCEIVER: '/usr/local/bin/vxiTransceiver',
    RSCRIPT: '/usr/bin/Rscript',
    DATE: '/bin/date',
    SLEEP: '/bin/sleep',
    ECHO: '/bin/echo',
    TEXCALLER: '/usr/local/bin/texcaller',
    WHICH: '/usr/bin/which'
  },
  theRepeats: {}
}

for (var i in cfg) exports[i] = cfg[i];

delete cfg;
