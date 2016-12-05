/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2016-12-05
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');
var mailer = require('nodemailer');
// npm install nodemailer

var logger = cfg.logger;

/**
 * Lifert String von String-Array ("\\n" als Verbinder) oder String selbst. 
 * @method getString
 * @param x String oder String-Array
 * @return {string} String
 */
function getString(x) {
  if (Array.isArray(x)) return x.join('\n'); else return x;
}

/**
 * Konfiguration der für nodemailer nötigen Datenstrukturen und Vesenden einer E-Mail.
 * @method call
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  var options = {
   host: js.Host || cfg.DEFAULT_SMTP_HOST,
   port: js.Port || cfg.DEFAULT_SMTP_PORT,
   logger: logger, // ???
   debug:false 
  }
  // Nur "From" und "To" sind zwingend.
  var mail = {
    from: js.From || false,
    to: js.To || false,
    cc: js.Cs || null,
    bcc: js.Bcc || null, 
    replyTo: js.ReplyTo || null,
    subject: js.Subject || '',
    text: js.Text ? getString(js.Text) : '',
    html: js.Text ? null : js.Html ? getString(js.Html) : null,
    secure: typeof js.Secure == 'boolean' ? js.Secure : false
  }
  if (js.User) {
    mail.auth = {};
    mail.auth.user = js.User;
    mail.auth.pass = js.Password || '';
  }

  if (!mail.from || !mail.to) response.prepareError(pRef, js, 'missing parameter');

  var transporter = mailer.createTransport(options);
  logger.debug('transporter', transporter);
  logger.debug('message', mail.text || mail.html);

  utils.addStartTime(js);
  
  transporter.sendMail(mail, function(err, res) {
    if (err) {
      response.prepareError(pRef, js, err.response);
    } else {    
      response.prepareResult(pRef, js, res.response);
      utils.addStopTime(js);
    }  
    transporter.close();
  });
  
}

exports.call = call;
