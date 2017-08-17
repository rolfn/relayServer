# Beispiele zur Gerätekommunikation per »relayServer«

## VXI-11

### GPIB/RS232-LAN-Adapter E5810A

#### RS232
```
cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"VXI11","Host":"169.254.58.10","Device":"COM1,488","Value":"*IDN?"}
EOF
```

#### GPIB
```
cat <<EOF | curl -T - -X PUT http://localhost:55555
{"Action":"VXI11","Host":"e75481","Device":"gpib0,5","Value":"*IDN?"}
EOF
```

... Weiteres soll folgen ...


