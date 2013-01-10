
// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'utils';

var cfg = require('./config.js');
var tools = require('./tools.js');

eval(tools.getFunctionCode('debug'));
eval(tools.getFunctionCode('fdebug'));
var inspect = tools.inspect;

/**
 * Wiederholtes Aufrufen der Funktion ``exec''.
 * @param number Anzahl der Aufrufe.
 * @param wait Wartezeit zwischen zwei Aufrufen in ms.
 * @param exec Aufzurufende Funktion. Ihr Rückgabe-String wird
 * aufgesammelt. Ihr Parameter ist eine Array-Variable im Falle 
 * von echten Wiederholung. Es sollte aber auch der Fall, dass null
 * übergeben wird, behandelt werden ("number==1").
 * @param ready Funktion, die nach dem letzten Aufruf von ``exec''
 *  aufgerufen wird. Ihr Parameter ist ein Array aller Rückgabe-Strings
 *  der einzelnen exec-Aufrufe.
 * @param pRef Object, speziell wegen "jobId" zum Kennzeichnen des
 *  Repeat-Prozesses und zum vorzeitigen Beenden.
 * @param _buf String-Array; darf beim ersten Aufruf nicht angegeben
 *  werden (nur interne Verwendung).
 */
function repeat(number, wait, exec, ready, pRef, _buf) {
  if (!_buf) {// Erster Aufruf
    var _buf = [];
    cfg.theRepeats[pRef.jobId] = { running:true };
    var nb;
  }
  nb = number;
  fdebug('cfg.theRepeats 1', inspect(cfg.theRepeats));
  // Solange nb > 0 und kein "killRepeats" passiert ist: Ergebnis in
  // Array _buf speichern und nach Wartezeit sich selbst erneut aufrufen.
  fdebug('time', '' + new Date().getTime(), 1);
  var running = cfg.theRepeats[pRef.jobId] && cfg.theRepeats[pRef.jobId].running;
  if ((nb--) && running) {
    //_buf.push(exec());
    exec(_buf);
    fdebug('_buf', ' (nb:' + nb + ') ' + inspect(_buf));
    if (nb) {
      setTimeout(function() {
        repeat(nb, wait, exec, ready, pRef, _buf);
      }, wait);
    } else {// Nach letztem Durchgang nicht mehr warten
      repeat(nb, wait, exec, ready, pRef, _buf);
    }
  } else {
    delete cfg.theRepeats[pRef.jobId];
    fdebug('cfg.theRepeats 2', inspect(cfg.theRepeats));
    ready((_buf.length == 1) ? _buf[0] : _buf);// Ergebnis weiterleiten
  }
}

exports.repeat = repeat;

