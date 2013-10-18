# nodejsServers2

Nodejs-basierte http-Server für Messaufgaben

Dies ist eine Neuimplementierung von "nodejsServers". Im Gegensatz zur alten
Version soll hier in größerem Maße auf Modularität Wert gelegt werden.

##  Relay-Server

Durch Zusenden von JSON-Daten per http-POST (Port 55555) kann dieser Server veranlasst werden, bestimmte Aktionen auszuführen und deren Ergebnis an die aufrufende Applikation zurückzusenden.

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

echo '{"Action":"/usr/local/bin/vxiTransceiver","Host":"e75481",
  "Device":"gpib0,5","Value":"*IDN?"}' | curl -T - -X PUT http://localhost:55555

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
##  GitLab-Webhook-Server

Dieser Server ist über http auf dem Port 3240 erreichbar (Beispiel: `http://a73434.berlin.ptb.de:3420`). Die URL kann in GitLab einem bestimmten Repositorium als Webhook-Adresse zugeordnet werden. Nach erfolgter Git-Push-Operation, d.h. bei einer Erneuerung der versionierten Dateien des betreffenden Repositoriums auf dem GitLab-Server, wird dem Webhook-Server Daten zu diesem Ereignis übermittelt. Daraufhin werden Shell-Kommandos, die in der  Konfigurationsdatei `gitlabhook.conf` angegeben sind, ausgeführt. Enthält diese Datei keine gültige tasks-Definition, so unterbleibt das Starten des GitLab-Webhook-Server. Näheres siehe: [node-gitlab-hook](../../../../rolf.niepraschk/node-gitlab-hook/blob/master/README.md).

### Beispiel des Inhaltes der Konfigurationsdatei

Die Datei `gitlabhook.conf` wird geladen, wenn sie sich im Hauptverzeichnis dieses Projektes befindet (alternativ in `/etc/gitlabhook/` oder `/usr/local/etc/gitlabhook/`). Der folgende Inhalt einer solchen Datei zeigt als Beispiel, wie die zur home-page des Vakuumlabors gehörenden Dateien automatisch nach einem erfolgten `git push` an ihren Bestimmungsort kopiert werden:

```javascript
{
  "tasks": {
    "vaclabpage": [
      "exec 1>/dev/null",
      "exec 2>/dev/null",
      "git clone %h",
      "cd %r",
      "cp -p --parents `git ls-files` /srv/www/htdocs/vaclabpage/"
    ]
  }
}
```

Anmerkung: Da der als Dämon gestartete NodejsServers-Prozess unter dem Nutzer "wwwrun" und der Gruppe "www" läuft, muss das zu beschreibene Zielverzeichnis der Gruppe "www" gehören und zumindest für diese Gruppe Schreibrechte besitzen (`chmod g+w /srv/www/htdocs/vaclabpage`).





