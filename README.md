# Digitale Nachlässe

Ein Skript, mit dem sich die Inhalte von Verzeichnisse kartieren lassen. Es erstellt pro Datei eine Zeile in einer Excel-Datei. Jede Zeile gibt Auskunft über Dateiname, Pfad, Datum der letzten Änderung und Erstellung, die Dateigröße und den Dateityp.

## Voraussetzung

Folgende Python-Bibliotheken müssen installiert sein:

```shell
pip3 install pandas openpyxl requests beautifulsoup4 lxml
```

## Aufruf

Mit `python dn.py <Verzeichnis> <Dateiname.xlsx>` lässt sich das Skript aufrufen.
