// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-14

const MODULE = 'email';

var cfg = require('./config.js');
var tools = require('./tools.js');
var response = require('./response.js');
var mailer = require('/usr/lib/node_modules/nodemailer'); // npm install nodemailer

function inspect() {};
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

function call(pRef, js) {
  mailer.SMTP = {
    host: (js.Host) ? js.Host : cfg.DEFAULT_SMTP_HOST,
    port: tools.getInt(js.Port, cfg.DEFAULT_SMTP_PORT),
    ssl:  (js.Ssl) ? js.Ssl : false,
    use_authentication: (js.UseAuthentication) ? js.UseAuthentication : false,
    user: (js.User) ? js.User : '',
    pass: (js.Password) ? js.Password : ''
  };
  fdebug('mailer', inspect(mailer));
  // Nur "From" und "To" sind zwingend.
  var message = {sender:js.From,to:js.To,subject:js.Subject};
  message.body = (js.Body) ? js.Body : '';
  message.debug = tools.isDebug(99);
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
  fdebug('message', inspect(message));
  var saveConsoleLog = console.log;
  console.log = function (d) {
    process.stderr.write(d + '\n');
  };
  mailer.send_mail(message, function(error, success){
    console.log = saveConsoleLog;
    if (success) {
      response.prepareResult(pRef, js, 'OK');
    } else {
      response.prepareError(pRef, js, error);
    }
  });
}

exports.call = call;
