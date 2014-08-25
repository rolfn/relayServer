/**
 * @author Rolf Niepraschk (Rolf.Niepraschk@ptb.de)
 * version: 2014-05-28
 */

var cfg = require('./config.js');
var tools = require('./tools.js');
var response = require('./response.js');
var mailer = require('nodemailer');
// npm install nodemailer

var logger = cfg.logger;

/**
 * Konfiguration der für nodemailer nötigen Datenstrukturen und Vesenden einer E-Mail.
 * @param {object} pRef interne Serverdaten (req, res, ...)
 * @param {object} js empfangene JSON-Struktur um weitere Daten ergänzt
 */
function call(pRef, js) {
  mailer.SMTP = {
    host: (js.Host) ? js.Host : cfg.DEFAULT_SMTP_HOST,
    port: tools.getInt(js.Port, cfg.DEFAULT_SMTP_PORT),
    ssl:  (js.Ssl) ? js.Ssl : false,
    use_authentication: (js.UseAuthentication) ? js.UseAuthentication : false,
    user: (js.User) ? js.User : '',
    pass: (js.Password) ? js.Password : ''
  };
  logger.debug('mailer', mailer.SMTP);
  // Nur "From" und "To" sind zwingend.
  var message = {sender:js.From,to:js.To,subject:js.Subject};
  message.body = (js.Body) ? js.Body : '';
  ///message.debug = tools.isDebug(99);
  if (js.Cc) message.cc = js.Cc;
  if (js.Bcc) message.bcc = js.Bcc;
  if (js.ReplyTo) message.reply_to = js.ReplyTo;
  if (js.Html) message.html = js.Html;
  if ((js.Attachments) && Array.isArray(js.Attachments)) {
    for (var i=0; i<js.Attachments.length; i++) {
      var cont = js.Attachments[i].Contents;
      if ((cont) && (js.Attachments[i].Filename)) {
        if (!message.attachments) message.attachments = [];
        message.attachments[i] = {};
        message.attachments[i].filename = js.Attachments[i].Filename;
        // Einfache Strings und String-Arrays unterstützen.
        var buf = (Array.isArray(cont)) ? cont.join('') : cont;
        message.attachments[i].contents = new Buffer(buf, "base64");
      }
    }
  }
  logger.debug('message', message);
  var saveConsoleLog = console.log;
  console.log = function (d) {
    process.stderr.write(d + '\n');
  };
  utils.addStartTime(js);
  // TODO: Array von smtp-Server gestatten, falls einer nicht funktioniert.
  mailer.send_mail(message, function(error, success){
    console.log = saveConsoleLog;
    if (success) {
      utils.addStopTime(js);
      response.prepareResult(pRef, js, 'OK');
    } else {
      response.prepareError(pRef, js, error);
    }
  });
}

exports.call = call;
