// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-14

// noch ungetestet in der modularen Variante!

const MODULE = 'ldap';

var cfg = require('./config.js');
var tools = require('./tools.js');
var response = require('./response.js');
var ldap = require('/usr/lib/node_modules/ldapjs');
var zlib = require('zlib');

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

function end(pRef, js) {
  fdebug();
  prepareResult(pRef, js, {Success:js.Success,Data:js.Data});
}

function unbind(pRef, js) {
  js.client.unbind(function(e) {
    if (e) {
      fdebug('error', e);
    } else {
      fdebug('success');
    }
    end(pRef, js);
  });
}

function search2(pRef, js, last) {
  var opts = {
    filter:js.Filter, 
    attributes:js.Attributes,
    scope: 'sub'
  }; // base=???

  try{
    js.client.search('', opts, function(e, res) {
      js.Data = '???';
      if (e) {
        fdebug('search', e);
        js.Data = e.message;
        unbind(pRef, js);
      } else {
        fdebug('search', 'SUCCESS');
        res.on('searchEntry', function(entry) {
          js.Data = JSON.stringify(entry.object);
          js.DN = entry.dn;
          fdebug('entry', js.Data);
        });
        res.on('error', function(e) {
          js.Data = e.message;
          fdebug('error', js.Data);
        });
        res.on('end', function(result) {
          fdebug('status', result.status);
          if (last == undefined) {
            js.Success = true;
            unbind(pRef, js);
          } else {
            fdebug('last', last);
            last(pRef, js);
          }
        });
      }  
    });  
  } catch(e) {
    js.Data = e.toString();
    unbind(pRef, js);
  }
  
}

function search1(pRef, js, last) {
  js.client = ldap.createClient({url: 'ldap://' + js.Host + ':' + js.Port});
  js.Success = false;
  js.client.bind('', '', function(err, res) {// Connection-Test
    if (err) {
      js.Data = err;
      fdebug(err);
      end(pRef, js); // kein "unbind"!
    } else {
      fdebug('SUCCESS');
      search2(pRef, js, last);
    }
  });   
}

function auth3(pRef, js) {
  if (js.DN == undefined) {
    js.Data = ('Search failure or wrong username');
    unbind(pRef, js);
  } else {
    if (!js.Passwd) {
      js.Passwd = (js.Action == 'LDAP_AUTH') ? js.Passwd = '?' : js.Passwd = '';
    }
    if (!js.Name) js.Name = '';
    js.client.bind(js.DN, js.Passwd, function(err, res) {
      if (err) {
        fdebug('error', err);
        js.Data = ('Wrong password');
      } else {
        fdebug('success');
        js.Success = true;
      }
      unbind(pRef, js);
    });
  }
}

function auth2(pRef, js) {
  fdebug();
  zlib.inflate(js.Passwd, function(err, buf) {
    if (err) {
      prepareError(pRef, js, 'internal error');
    } else {
      js.Passwd = buf.toString();
      auth3(pRef, js);
    }
  });
}

/* http://ldapjs.org/client.html */
function auth1(pRef, js) {
  // Später nach vollständigem DN für "CN=username" suchen.
  js.Filter = 'cn=' + js.Name;
  js.Attributes = '';
  debug();
  search1(pRef, js, auth2);
}

exports.auth = auth1;
exports.search = search1;
