/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2020-04-27
 */

const cfg = require('./config.js');
const tools = require('./tools.js');
const utils = require('./utils.js');
const axios = require('axios');
const response = require('./response.js');

const logger = cfg.logger;

/**
 * Konfiguration der nötigen Datenstrukturen und Aufnahme der HTTP-Kommunikation.
 * Wait/Repeat wird derzeit nicht unterstützt. Die Umgebungsvariablen proxy und
 * no_proxy werden berücksichtigt.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var config = {}, isJson = typeof js.Json == 'boolean' ? js.Json : false,
    isNoProxy = typeof js.NoProxy == 'boolean' ? js.NoProxy : false;
  
  config.url =  js.Url;
  config.method = (js.Method || 'get').toLowerCase(); 
  config.timeout = js.Timeout || 0;
  if (js.Body) config.data = js.Body;
  config.responseType = js.ResponseType || isJson ? 'json' : 'text';
  if (isNoProxy) config.proxy = false;
  config.headers = js.Headers || {};
  
  if (!js.Method) {
    if (js.Body) {
      if (typeof js.Body != 'string' && typeof js.Body != 'Buffer' && !json) {
        response.prepareError(pRef, js, 
          "Wrong type of Body. (Missing 'Json:true'?)");
        return;
      }
      config.method = 'post';
    } 
  }

  logger.debug(`method: ${config.method}, responseType: ${config.responseType}, 
  timeout: ${config.timeout}, proxy: ${config.proxy}`);
  
  utils.addStartTime(js);
  
  axios(config).then(function (res) {
    if (res.status > 199 && res.status < 500) {
      utils.addStopTime(js);
      logger.debug('response body: ', res.data);
      response.prepareResult(pRef, js, res.data);
    } else {
      const x = res.statusText || res.status ? res.status : 'unknown error';
      logger.error(x);
      response.prepareError(pRef, js, x);      
    }
  }).catch(function (error) {
    var x;
    if (error.response) {
      const e = error.response;
      x = e.statusText || e.status ? e.status : 'unknown error';
    } else if (error.request) {
      x = error.request; 
    } else {
      x = error.message;
    }
    logger.error(x);
    response.prepareError(pRef, js, x);   
  });
  
}

exports.call = call;


