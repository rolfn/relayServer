/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2013-10-10
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
 * @param {number} nb Anzahl der Aufrufe.
 * @param {number} wait Wartezeit zwischen zwei Aufrufen in ms.
 * @param {function} exec zu wiederholende Funktion
 * @param {function} ready Aufruf am Ende von ``repeat''
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 * @param {String[]} _buf aufgesammelte Daten.
 */
function repeat(nb, wait, exec, ready, pRef, js, _buf) {
  if (!_buf) {// Erster Aufruf
    var _buf = [];
    cfg.theRepeats[pRef.jobId] = { running:true };
  }
  var running = cfg.theRepeats[pRef.jobId] && cfg.theRepeats[pRef.jobId].running;
  // Solange kein "killRepeats" passiert ist bzw. nicht letzter Durchgang:
  // "exec" ausführen und Ergebnis in Array _buf speichern und ggf. nach
  // Wartezeit sich selbst erneut aufrufen.
  if (running) {
    js.t_start.push(new Date().getTime());
    fdebug('t_start.push', '' + js.t_start[js.t_start.length-1]);
    exec(_buf, function() {
      js.t_stop.push(new Date().getTime());
      fdebug('t_stop.push', '' + js.t_stop[js.t_stop.length-1]);
      fdebug('buf', ' (nb:' + nb + ') ' + inspect(_buf));
      if (--nb) {
        setTimeout(function() {
          repeat(nb, wait, exec, ready, pRef, js, _buf);
        }, wait);
      } else {
        delete cfg.theRepeats[pRef.jobId];
        // Gleich Ende
        repeat(nb, wait, exec, ready, pRef, js, _buf);
      }
    });
  } else {
    // Ende
    ready(_buf.length == 1 ? _buf[0] : _buf);// Ergebnis weiterleiten
  }
}

exports.repeat = repeat;

