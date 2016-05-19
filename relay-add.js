
/**
 * Dedizierte Funktionen zur Vereinfachung des
 * Postprocessing einer Task.
 *
 * Eine in einem der Submodule definierte Funktion
 * z.B. helloSandbox() kann über:
 *
 *  _.helloSandbox()
 *
 * im Postprocessing ausgeführt werden.
 *
 * version: 2016-05-17
 */

submodules = [
'./add/relay-add-MISC.js',
'./add/relay-add-SRG3.js',
'./add/relay-add-PPC.js',
'./add/relay-add-MKT50.js',
'./add/relay-add-SE1FM3.js',
'./add/relay-add-CORVUS.js',
'./add/relay-add-VM212.js',
'./add/relay-add-FRS.js',
'./add/relay-add-PM2535.js',
'./add/relay-add-MKSCDG.js',
'./add/relay-add-F250.js',
'./add/relay-add-ATMION.js',
'./add/relay-add-IM540.js',
'./add/relay-add-AxTRAN.js',
'./add/relay-add-COMBIVAC.js',
'./add/relay-add-DCF77.js',
'./add/relay-add-KEITHLEY.js',
'./add/relay-add-VACOM.js',
'./add/relay-add-CDG.js',
'./add/relay-add-STATISTICS.js'
]

for (var i=0; i<submodules.length; i++) {
  var sm = require(submodules[i]);
  for (exp in sm) {
    exports[exp] = sm[exp];
  }
}



