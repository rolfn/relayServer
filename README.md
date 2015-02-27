# relayServer

Nodejs-basierter http-Server für Messaufgaben

Dies ist eine Neuimplementierung von "nodejsServers". Im Gegensatz zur alten
Version soll hier in größerem Maße auf Modularität Wert gelegt werden.

## Relay-Server

Durch Zusenden von JSON-Daten per http-POST (Port 55555) kann dieser Server veranlasst werden, bestimmte Aktionen auszuführen und deren Ergebnis an die aufrufende Applikation zurückzusenden.

### Vorbereitung zur Installation

Die make-Aufrufe ```make``` bzw. ```make install``` erzeugen ein rpm-Paket mit allen Dateien, die notwendig sind, damit der Relay-Server als Dämon unter openSUSE (>12.2) laufen kann. Vorher muss einmalig ```npm install``` aufgerufen werden, damit die nötigen nodejs-Bibliotheken installiert werden. ```make install``` kopiert das fertige rpm-Paket in eine Dateistruktur, die geeignet ist, an unser openSUSE-rpm-Repositorium geschickt zu werden. Alternativ kann das rpm-Paket auch von Hand installiert werden.

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

Einem neuen Rechner sollte das vaclab-Repositorium bekannt gemacht werden, damit das Paket »relayServer« einfach installiert werden kann (einschließlich zukünftiger updates):
```bash
zypper ar http://a73434.berlin.ptb.de:5984/sys/repos/openSUSE_13.1/vaclab.repo
zypper ref vaclab ; zypper in relayServer
```

### Beispiele zur Kommunikation mit dem Relay-Server (Port 55555)

```bash
echo '{"Action":"/bin/echo","Value":"FRIDOLIN"}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"/usr/bin/which","Value":"pdftex"}' | \
  curl -T - -X PUT http://`hostname --fqdn`:55555

echo '{"Action":"_version"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"RANDOM"}' | \
  curl -T - -X PUT http://i75434.berlin.ptb.de:55555

echo '{"Action":"TIME","Repeat":3,"Wait":2000}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"VXI11","Host":"e75465","Device":"gpib0,2","Value":"T\n",
  "readTimeout":0}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"/usr/bin/Rscript", "Value":["foo","bar"],"Body":"print(17+4)"}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"TCP","Repeat":3,"Wait":2000,"Host":"e75493","Port":"23",
  "Value":"exit\r"}' | curl -T - -X PUT http://localhost:55555

echo '{"Action":"HTTP","Url":"http://a73434.berlin.ptb.de"}' | \
  curl -T - -X PUT http://localhost:55555

echo '{"Action":"EMAIL", "Host": "smtp-hub", "Subject": "Grüße von NodeJS",
  "From": "Homunculus <homunculus@ptb.de>","To": "Thomas.Bock@ptb.de",
  "Body": "Hallo, wie geht es Dir?\nHeute scheint die Sonne."}' | \
   curl -T - -X PUT http://localhost:55555

echo '{"Action":"LaTeX","Source":"\\documentclass{article}\\begin{document}
  Hello world!!!\\end{document}","OutputType":"stream"}' | \
    curl -T - -X PUT http://localhost:55556 > zz.pdf

echo '{"Action":"_version","PostProcessing":"Result=\"Hugo\""}' | \
  curl -T - -X PUT http://localhost:55555
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

gestartet werden. Es entsteht zusätzlich ein coverage-Report
unter ./coverage/lcov-report/index.html

* nur VXI11 Funktionalität: ```bash npm run test-vxi11```
* nur TCP Funktionalität: ```bash npm run test-tcp```
* nur postprocessing-Zusatzfunktionen: ```bash npm run test-relay-add```
* nur Rscript Funktionalität: ```bash npm run test-rscript```

Zum Testen eines bereits laufenden relayServers sind folgende scripte
vorbereitet:

* ```bash npm run test-ce3-inst```
* ```bash npm run test-rolf-inst```
* ```bash npm run test-thomas-inst```

