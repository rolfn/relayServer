# relayServer

Nodejs-basierter http-Server für Messaufgaben

Dies ist eine Neuimplementierung von "nodejsServers". Im Gegensatz zur alten
Version soll hier in größerem Maße auf Modularität Wert gelegt werden.

## Relay-Server

Durch Zusenden von JSON-Daten per http-POST (Port 55555) kann dieser Server veranlasst werden, bestimmte Aktionen auszuführen und deren Ergebnis an die aufrufende Applikation zurückzusenden.

### Vorbereitung zur Installation

### Installation
Funktionierende Dateien von einem anderen Rechner beschaffen, z.B.:
```bash
rsync -avzL --delete --keep-dirlinks --exclude '.git'  \
  i75454:/usr/local/share/relayServer /usr/local/share/
scp i75454:/usr/lib/systemd/system/relayServer.service \
  /usr/lib/systemd/system/relayServer.service
chown -R nobody.nobody /usr/local/share/relayServer/
ln -sf /usr/local/share/relayServer/vlLogging /usr/local/bin/vlLogging
```

### Nach erfolgter Installation

Um den Relay-Server als Linux-Dämon zu betreiben, sind folgende Schritte auszuführen (systemd-basiertes Betriebssystem):
```bash
systemctl enable relayServer.service
systemctl start relayServer.service
```
und ggf.
```bash
systemctl status -l relayServer.service
```

### Beispiele zur Kommunikation mit dem Relay-Server (Port 55555)

```bash
cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"EXECUTE","Cmd":"/usr/bin/date","Args":"+%Y-%m-%d"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"_version"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"TIME","Repeat":3,"Wait":2000}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"RANDOM"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"VXI11","Host":"e75465","Device":"gpib0,2","Value":"T\n",
  "readTimeout":0}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"EXECUTE","Cmd":"/usr/bin/Rscript",
"Body":["a <- 1:10","b <- which(a > 2 & a < 8)","b"],
"Args0":"--vanilla","Args":["foo","bar"]}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"EXECUTE","Cmd":"/usr/bin/python","Body":"print 12+5"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"TCP","Repeat":3,"Wait":2000,"Host":"e75493","Port":"23",
  "Value":"exit\r"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"UDP","Host":"172.30.56.30","Port":"2362","Value":"*IDN?"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"HTTP","Url":"https://google.de"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"EMAIL", "Host": "smtp-hub", "Subject": "Grüße von NodeJS",
  "From": "Homunculus <homunculus@ptb.de>","To": "Thomas.Bock@ptb.de",
  "Body": "Hallo, wie geht es Dir?\nHeute scheint die Sonne."}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555 > foo.pdf
{"Action":"TEX","Body":"\\\documentclass{article} \
\\\begin{document}Hello world!!!\\\end{document}",
"OutputType":"stream","KeepFiles":true}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"_version","PostProcessing":"Result=\"Hugo\""}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"XLSX-IN","Value":"$(base64 -w 0 foo.xlsx)"}
EOF

cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"MODBUS","Host":"10.0.0.31","Address":45395,"Quantity":11,
 "FunctionCode":"ReadHoldingRegisters", "OutMode":"Uint16"}
```

## Test

Nach einem Auffrischen der vxi11-Bibliothek:

```bash
npm update vxi11
```

können die unter ```./test``` befindlichen unit-Tests werden im
»relayServer«-Stammverzeichnis mittels:

```bash
npm test
```

gestartet werden. Für die erstellung eines coverage-Report
unter ./coverage/lcov-report/index.html gibt es  ```bash npm run coverage```.

Folgene Einzeltests stehen zur Verfügung:
* nur VXI11 Funktionalität: ```bash npm run test-vxi11```
* nur TCP Funktionalität: ```bash npm run test-tcp```
* nur UDP Funktionalität: ```bash npm run test-udp```
* nur postprocessing-Zusatzfunktionen: ```bash npm run test-relay-add```
* nur Rscript Funktionalität: ```bash npm run test-rscript```

Zum Testen eines bereits laufenden relayServers sind folgende scripte
vorbereitet:

* ```bash npm run test-ce3-inst```
* ```bash npm run test-rolf-inst```
* ```bash npm run test-thomas-inst```

