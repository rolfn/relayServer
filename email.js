// Rolf Niepraschk, Rolf.Niepraschk@ptb.de, 2013-01-10

const MODULE = 'email';

var cfg = require('./config.js');
var tools = require('./tools.js');
var utils = require('./utils.js');
var response = require('./response.js');

eval(tools.getFunctionCode('debug'));
eval(tools.getFunctionCode('fdebug'));
var inspect = tools.inspect;
