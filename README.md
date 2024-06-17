# Digitale Nachlässe

Ein paar Skripte, mit denen sich die Inhalte von Verzeichnisse kartieren und Metadaten gewinnen lassen. `dn.py` erstellt pro Datei eine Zeile in einer Excel-Datei. Jede Zeile gibt Auskunft über Dateiname, Pfad, Datum der letzten Änderung und Erstellung, die Dateigröße und den Dateityp. Die anderen Skripte lassen sich wahlweise einbinden, um Word-Dateien in Text-Dateien umzuwandeln (`word2txt.py`), eine PDF-, Word- oder Text-Datei zusammenzufassen (`summarize.py`) oder eine Bild-Datei zu beschreiben (`summarize_image.py`).

Um explorativ die Daten zu erschließen, kann auch das Jupyter Notebook `Digitale Nachlässe.ipynb` genutzt werden.

## Voraussetzung

Folgende Python-Bibliotheken müssen installiert sein:

```shell
pip3 install pandas openpyxl requests beautifulsoup4 lxml docx2txt ollama
```

## Aufruf

Mit `python dn.py <Verzeichnis> <Dateiname.xlsx>` lässt sich das Skript aufrufen.

## Dateien zusammenfassen

Voraussetzung ist eine lokal laufenden Ollama-Instanz. Ob eine läuft, kann mit `ollama serve` kontrolliert werden.

Wenn auf eine externe Ollama-Instanz zurückgegriffen werden soll, kann mit `export OLLAMA_HOST=<IP-Adresse:Port>` die externe Adresse angegeben werden.

Das Skrippt lässt sich auch über das Terminal mit `python summarize.py <Text-Datei>` aufrufen.