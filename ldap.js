/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: version: 2019-01-25
 */

// noch ungetestet in der modularen Variante!

var cfg = require('./config.js');
var tools = require('./tools.js');
var response = require('./response.js');
var ldap = require('/usr/lib/node_modules/ldapjs');
var zlib = require('zlib');

var logger = cfg.logger;

/**
 * Description
 * @method end
 * @param {object} pRef
 * @param {object} js
 */
function end(pRef, js) {
  prepareResult(pRef, js, {Success:js.Success,Data:js.Data});
}

/**
 * Description
 * @method unbind
 * @param {object} pRef
 * @param {object} js
 */
function unbind(pRef, js) {
  js.client.unbind(function(e) {
    if (e) {
      logger.error('error', e);
    } else {
      logger.debug('success');
    }
    end(pRef, js);
  });
}

/**
 * Description
 * @method search2
 * @param {object} pRef
 * @param {object} js
 * @param {function} last
 */
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
        logger.error('search: ', e);
        js.Data = e.message;
        unbind(pRef, js);
      } else {
        logger.debug('search: ', 'SUCCESS');
        res.on('searchEntry', function(entry) {
          js.Data = JSON.stringify(entry.object);
          js.DN = entry.dn;
          logger.debug('searchEntry: ', js.Data);
        });
        res.on('error', function(e) {
          js.Data = e.message;
          logger.error('error: ', js.Data);
        });
        res.on('end', function(result) {
           logger.debug('status: ', result.status);
          if (last === undefined) {
            js.Success = true;
            unbind(pRef, js);
          } else {
            logger.debug('last: ', last);
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

/**
 * Description
 * @method search1
 * @param {object} pRef
 * @param {object} js
 * @param {function} last
 */
function search1(pRef, js, last) {
  js.client = ldap.createClient({url: 'ldap://' + js.Host + ':' + js.Port});
  js.Success = false;
  js.client.bind('', '', function(err, res) {// Connection-Test
    if (err) {
      js.Data = err;
      logger.error('error', err);
      end(pRef, js); // kein "unbind"!
    } else {
      logger.debug('SUCCESS');
      search2(pRef, js, last);
    }
  });
}

/**
 * Description
 * @method auth3
 * @param {object} pRef
 * @param {object} js
 */
function auth3(pRef, js) {
  if (js.DN === undefined) {
    js.Data = ('Search failure or wrong username');
    unbind(pRef, js);
  } else {
    if (!js.Passwd) {
      js.Passwd = (js.Action == 'LDAP_AUTH') ? js.Passwd = '?' : js.Passwd = '';
    }
    if (!js.Name) js.Name = '';
    js.client.bind(js.DN, js.Passwd, function(err, res) {
      if (err) {
        logger.error('wrong password', err);
      } else {
        logger.debug('SUCCESS');
        js.Success = true;
      }
      unbind(pRef, js);
    });
  }
}

/**
 * Description
 * @method auth2
 * @param {object} pRef
 * @param {object} js
 */
function auth2(pRef, js) {
  zlib.inflate(js.Passwd, function(err, buf) {
    if (err) {
      prepareError(pRef, js, 'internal error');
    } else {
      js.Passwd = buf.toString();
      auth3(pRef, js);
    }
  });
}

/**
 * http://ldapjs.org/client.html
 * @method auth1
 * @param {object} pRef
 * @param {object} js
 */
function auth1(pRef, js) {
  // Später nach vollständigem DN für "CN=username" suchen.
  js.Filter = 'cn=' + js.Name;
  js.Attributes = '';
  search1(pRef, js, auth2);
}

exports.auth = auth1;
exports.search = search1;
