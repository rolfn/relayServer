## nodejsServers2

Nodejs-basierte http-Server für Messaufgaben

Dies ist eine Neuimplementierung von "nodejsServers". Im Gegensatz zur alten
Version soll hier in größerem Maße auf Modularität Wert gelegt werden.

### Beispiele zur Kommunikation mit dem Relay-Server (Port 55555)

```javascript
echo '{"Action":"HTTP","Url":"http://a73434.berlin.ptb.de"}' | \
  curl -T - -X PUT http://localhost:55555
```
    echo '{"Action":"HTTP","Url":"http://a73434.berlin.ptb.de"}' | \
      curl -T - -X PUT http://localhost:55555


R.N.
