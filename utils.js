
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
 * @param exec Aufzurufende Funktion, die die Daten beschafft. Ihr erster
 * Parameter muss eine Array-Variable sein. In ihr werden die Daten pro
 * Durchgang abgelegt. Der zweite Parameter ist eine Funktion, die aufgerufen
 * werden muss, nachdem Daten gespeichert wurden (oft innerhalb von
 * callback-Funktion).
 *
 * |#######|<----- Wait ----->|#######|<----- Wait ----->|
 * start1                     stop1
 *                            start2                     stop2/Response
 * 
 * @param ready Funktion, die nach dem letzten Aufruf von ``exec''
 *  aufgerufen wird. Ihr Parameter ist ein Array aller Rückgabe-Strings
 *  der einzelnen exec-Aufrufe.
 * @param pRef Object, speziell wegen "jobId" zum Kennzeichnen des
 *  Repeat-Prozesses und zum vorzeitigen Beenden.
 * @param js Object, das allgemeine Datenobjekt.
 * @param _buf String-Array; darf beim ersten Aufruf nicht angegeben
 *  werden (nur interne Verwendung).
 */
function repeat_A(number, wait, exec, ready, pRef, js, _buf) {
  function repeat_A1() {
    fdebug('buf', ' (nb:' + nb + ') ' + inspect(_buf));
    setTimeout(function() {
      js.t_stop.push(new Date().getTime()); 
      repeat_A(nb, wait, exec, ready, pRef, js, _buf);
    }, wait);
  }
  if (!_buf) {// Erster Aufruf
    var _buf = [], nb;
    theRepeats[pRef.jobId] = { running:true }; 
  }
  nb = number;
  fdebug('theRepeats 1', inspect(theRepeats));
  fdebug('time', '' + new Date().getTime(), 1);
  var running = theRepeats[pRef.jobId] && theRepeats[pRef.jobId].running;
  // Solange nb > 0 und kein "killRepeats" passiert ist: Ergebnis in
  // Array _buf speichern und nach Wartezeit sich selbst erneut aufrufen.
  if (nb-- && running) {
    fdebug('exec', inspect(exec));
    js.t_start.push(new Date().getTime()); 
    exec(_buf, repeat_A1);
  } else {
    delete theRepeats[pRef.jobId];
    fdebug('theRepeats 2', inspect(theRepeats));
    ready(_buf.length == 1 ? _buf[0] : _buf);// Ergebnis weiterleiten
  }
}

exports.repeat = repeat_A;

