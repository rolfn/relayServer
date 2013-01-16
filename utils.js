/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-01-14
 */

const MODULE = 'utils';

var cfg = require('./config.js');
var tools = require('./tools.js');

/**
 * Erzeugt String-Repräsentation der inneren Struktur einer JS-Variable
 * (Rekursion bis Ebene 2, coloriert)
 * @param {object} o Zu untersuchende JS-Variable.
 * @return {string}  String-Repräsentation
 */
function inspect(o) {};
inspect = tools.inspect;

/**
 * In Abhängigkeit von "level" Ausgabe von Informationen. Der aktuelle 
 * Modulname wird ebenfalls ausgegeben.
 * @param item meist Funktionsname
 * @param subitem spezifische Aktion innerhalb der Funktion.
 * @param info Daten
 * @param level
 */
function debug(item, subitem, info, level) {};
debug = tools.createFunction('debug', MODULE);

/**
 * Wie "debug", aber "item" (Funktionsname) wird selbst ermittelt.
 * @param subitem
 * @param info
 * @param level
 */
function fdebug(subitem, info, level) {};
fdebug = tools.createFunction('fdebug', debug);

/**
 * Wiederholtes Aufrufen der Funktion exec.
 * Im Parameter _buf werden durch exec die Daten pro Durchgang abgelegt. Er darf
 * beim ersten Aufruf nicht angegeben werden. Der Parameter ready ist eine
 * Funktion, die aufgerufen wird, nachdem exec letztmalig aufgerufen wurde. Ihr
 * wird _buf als Parameter mitgegeben. Bei jedem Durchgang werden das t_start-
 * und das t_stop-Array ergänzt.
 * <pre>
 * |#######|<----- Wait ----->|#######|<----- Wait ----->|
 * start1                     stop1
 *                            start2                     stop2/Response
 * </pre>
 * @param {number} number Anzahl der Aufrufe.
 * @param {number} wait Wartezeit zwischen zwei Aufrufen in ms.
 * @param {function} exec zu wiederholende Funktion
 * @param {function} ready Aufruf nach Ende von ``exec''
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {String[]} _buf aufgesammelte Daten.
 */
function repeat(nb, wait, exec, ready, pRef, js, _buf) {
  function repeat1() {
    fdebug('buf', ' (_nb:' + _nb + ') ' + inspect(_buf));
    setTimeout(function() {
      js.t_stop.push(new Date().getTime());
      fdebug('t_stop.push', '' + js.t_stop[js.t_stop.length-1]);
      //fdebug('js', inspect(js));
      repeat(_nb, wait, exec, ready, pRef, js, _buf);
    }, wait);
  }
  if (!_buf) {// Erster Aufruf
    var _buf = [], _nb;
    cfg.theRepeats[pRef.jobId] = { running:true }; 
  }
  _nb = nb;
  fdebug('cfg.theRepeats 1', inspect(cfg.theRepeats));
  var running = cfg.theRepeats[pRef.jobId] && cfg.theRepeats[pRef.jobId].running;
  // Solange _nb > 0 und kein "killRepeats" passiert ist: Ergebnis in
  // Array _buf speichern und nach Wartezeit sich selbst erneut aufrufen.
  if (_nb-- && running) {
    js.t_start.push(new Date().getTime());
    fdebug('t_start.push', '' + js.t_start[js.t_start.length-1]); 
    exec(_buf, repeat1);
  } else {
    delete cfg.theRepeats[pRef.jobId];
    fdebug('cfg.theRepeats 2', inspect(cfg.theRepeats));
    ready(_buf.length == 1 ? _buf[0] : _buf);// Ergebnis weiterleiten
  }
}

exports.repeat = repeat;

