# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.12.1  
**Letzte Aktualisierung:** 03.08.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt wird schrittweise als mehrseitige Kochbuch-Website aufgebaut.

- `index.html` – Apple-inspirierte Startseite
- `fleisch.html` – Übersichtsseite für Rind, Hähnchen, Schwein und Fisch
- `honig-senf-lachs.html` – Rezeptseite für Honig-Senf-Lachs vom Grill
- `assets/honig-senf-lachs.jpg` – weboptimiertes JPEG-Rezeptbild für den Honig-Senf-Lachs
- `assets/grillgemuese.jpg` – weboptimiertes JPEG-Rezeptbild für Grillgemüse
- `assets/gemuesefinish-fresh.jpg` – weboptimiertes JPEG-Rezeptbild für Gemüsefinish-Fresh
- `assets/gemuesefinish-mild.jpg` – weboptimiertes JPEG-Rezeptbild für Gemüsefinish-Mild
- `gemuese-salat.html` – Übersichtsseite **Salate & Beilagen**
- `vegan.html` – vorbereitete Übersichtsseite für vegane Rezepte
- `grundlagen.html` – eigene Seite für Kerntemperaturen, Garpunkte, Salzlake und Dry Brine
- `grillgemuese.html` – eigene Rezeptseite für Grillgemüse
- `finishing-sauce.html` – eigene Rezeptseite für Gemüsefinish-Fresh
- `gemuesefinish-mild.html` – eigene Rezeptseite für Gemüsefinish-Mild
- `einkaufsliste.html` – mengenberechnete Einkaufsliste für alle Einzelrezepte
- `einkaufsliste-gesamt.html` – gemeinsame Einkaufsliste für mehrere ausgewählte Rezepte
- `kochbuch.html` – Übergangsseite für die frühere Gesamtansicht
- `00_Meta-Kim.md` – stabile Regeln und Architektur
- `00_Projektstatus.md` – dynamischer Zustand und Änderungshistorie
- GitHub Pages – Veröffentlichung der Website

## Aktueller Bestand

- 4 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 3 Arbeitsfassungen
- 4 geplante Fleischrezepte
- noch keine veganen Rezepte
- 1 vollständige Grundlagen-Seite
- 1 Startseite
- 3 Kategorie-Übersichtsseiten
- 4 eigenständige Rezeptseiten
- 4 Rezeptseiten mit eingebautem Hero-Bild
- 2 Übersichtsseiten mit insgesamt 4 anklickbaren Rezept-Thumbnails
- 1 Einzelrezept-Einkaufsliste für alle 4 Rezepte mit Mengenberechnung und Druckansicht
- 1 gemeinsame Einkaufsliste mit Rezeptauswahl und Zutatenkumulierung
- 1 Übergangsseite für die frühere Gesamtansicht

## Startseite

Die Startseite verwendet eine reduzierte, Apple-inspirierte Gestaltung mit:

- sehr großer Hauptüberschrift
- lokaler Apple-/Systemtypografie
- Hamburger-Menü
- direkter Navigation zu Fleisch, Salate & Beilagen, Vegan und Grundlagen
- drei großen Kategoriekarten
- drei zusätzlichen Schnellzugriffen
- responsiver Darstellung für Desktop, Tablet und Smartphone

Alle vier Hauptbereiche verweisen auf eigene Seiten. Die gemeinsame Einkaufsliste ist zusätzlich direkt von der Startseite erreichbar.

## Navigation

Die aktuellen Unter- und Rezeptseiten besitzen im Kopfbereich:

- links das Hamburger-Menü
- direkt daneben einen runden Home-Button mit Haus-Symbol
- mittig den Titel „Haralds Grillkochbuch“

Der Home-Button führt unmittelbar zu `index.html`.

## Gestaltungsregeln

### Rezeptkarten

Rezeptkarten auf Übersichtsseiten zeigen keine farbigen Status- oder Informations-Pills. Arbeitsstand, Portionen und Rezeptstatus bleiben auf den Rezeptseiten beziehungsweise in den internen Projektdateien dokumentiert.

### Rezeptbilder

Für Rezeptseiten ist folgender Bildstil festgelegt:

- großes Hero-Bild direkt unter Titel und Kurzbeschreibung
- Seitenverhältnis 16:9
- großzügig abgerundete Ecken
- dezente Schattenwirkung
- ruhiger, heller und hochwertiger Food-Fotografie-Stil
- aussagekräftiger Alternativtext
- zurückhaltende Bildunterschrift
- responsive Darstellung auf Desktop, Tablet und Smartphone

Die Seite `honig-senf-lachs.html` ist die erste verbindliche Vorlage für dieses Bildlayout. Food-Fotos werden als weboptimierte JPEG-Dateien gespeichert. Übersichtsseiten verwenden sie als lazy-geladene 16:9-Thumbnails. PNG bleibt Logos, Transparenzen und Grafiken vorbehalten.

## Einkaufsliste

Für die Einkaufsplanung stehen zwei Wege zur Verfügung.

### Einzelrezept

- Button und Personenauswahl direkt auf jeder Rezeptseite
- der Block **Einkaufsliste erstellen** steht auf jeder Rezeptseite am Ende des Rezeptinhalts direkt vor dem Zurück-Link
- automatische Umrechnung ausgehend von jeweils 4 Personen
- optionale Zutaten und Varianten werden berücksichtigt
- eigene Ergebnisdarstellung auf `einkaufsliste.html`
- Zutaten lassen sich abhaken; Häkchen werden lokal im Browser gespeichert
- Druckansicht blendet Bedienelemente und bereits abgehakte Zutaten aus

### Mehrere Rezepte gemeinsam

- eigene Seite `einkaufsliste-gesamt.html`
- alle vorhandenen Rezepte können einzeln angehakt werden
- eine gemeinsame Personenzahl gilt für alle ausgewählten Rezepte
- gleiche Zutaten werden über dauerhafte interne Zutaten-IDs erkannt
- kompatible Volumeneinheiten werden intern vereinheitlicht und anschließend als EL beziehungsweise TL ausgegeben
- Mengenbereiche, optionale Zutaten und die Knoblauchvariante des Gemüsefinish-Mild werden berücksichtigt
- Salz oder Pfeffer ohne feste Menge bleiben als Bedarfshinweis erhalten
- bei jeder zusammengeführten Zutat werden die zugehörigen Rezepte angezeigt
- Grillgemüse fügt ein Finish nicht automatisch hinzu; das gewünschte Finish wird separat ausgewählt, damit keine Doppelzählung entsteht
- Zutaten lassen sich abhaken und die Liste kann gedruckt werden

## Kategorien und Hauptbereiche

### Fleisch

Eigene Übersichtsseite: `fleisch.html`

Unterkategorien:

- Rind
- Hähnchen
- Schwein
- Fisch

Vorhandenes Fischrezept:

- Honig-Senf-Lachs vom Grill – Arbeitsfassung, Version 0.1.8, Seite `honig-senf-lachs.html`

Geplante Rezepte:

- Entrecôte Steakhouse
- Beer Can Chicken
- Chicken Asado
- Schweinenackensteak mariniert

### Salate & Beilagen

Eigene Übersichtsseite: `gemuese-salat.html`

Der Dateiname bleibt vorerst bestehen, damit vorhandene Links stabil bleiben.

Rubriken:

- **Salate & Gemüse**
- **Soßen & Finishes**

Vorhandene Rezepte:

- Grillgemüse – Rubrik Salate & Gemüse, Arbeitsfassung, Version 0.9.5, Seite `grillgemuese.html`
- Gemüsefinish-Fresh – Rubrik Soßen & Finishes, bestätigt, Version 1.0.5, Seite `finishing-sauce.html`
- Gemüsefinish-Mild – Rubrik Soßen & Finishes, Arbeitsfassung, Version 0.1.4, Seite `gemuesefinish-mild.html`

Spätere Nudel-, Kartoffel- und weitere Beilagensalate werden unter **Salate & Gemüse** eingeordnet.

### Vegan

Eigene Übersichtsseite: `vegan.html`

- derzeit noch ohne Rezept
- als Platzhalter im gleichen Apple-inspirierten Stil wie die anderen Kategorien angelegt
- für spätere vegane Rezepte vorbereitet

### Grundlagen

Eigene Seite: `grundlagen.html`

Vorhanden – in dieser Reihenfolge:

1. Kerntemperaturen und Garpunkte
2. Salzlake & Dry Brine

Das Kapitel **Salzlake & Dry Brine** beschreibt bewusst ein Vorbereitungsverfahren und ist kein eigenständiges Rezept. Die früheren Kapitel zu direkter Hitze, indirekter Hitze, Deckelregel und Zwei-Zonen-Aufbau wurden entfernt.

## Rezepte

### Honig-Senf-Lachs vom Grill

- ID: `honig-senf-lachs-grill`
- Seite: `honig-senf-lachs.html`
- Bild: `assets/honig-senf-lachs.jpg`
- Version: 0.1.8
- Status: Arbeitsfassung
- Rubrik: Fleisch → Fisch
- Menge: 4 Personen
- Grillmethode: indirekte Hitze bei 180–200 °C
- Grillzeit: etwa 12–15 Minuten
- Ziehzeit: 10 Minuten

Aktueller Zutatenstand:

- 4 Lachsfilets mit Haut
- 1 EL grober Senf
- 1 EL mittelscharfer Senf
- 1 EL Honig
- 1 EL Olivenöl
- 1 TL Zitronensaft
- Salz und Pfeffer
- optional Dill, sehr empfehlenswert

Verbindlicher Ablauf:

1. Senf, Honig, Olivenöl und Zitronensaft zu einer cremigen Glasur verrühren.
2. Lachs nur leicht salzen.
3. Glasur ausschließlich auf die Oberseite streichen, nicht auf die Haut.
4. 10 Minuten ziehen lassen, nicht länger.
5. Mit der Hautseite nach unten indirekt bei 180–200 °C grillen.
6. Nicht wenden und den Deckel geschlossen halten.
7. Nach etwa 8 Minuten bei Bedarf noch einmal dünn glasieren.
8. Gesamtgrillzeit etwa 12–15 Minuten.

Wichtiger Hinweis: Wegen des Honigs ausschließlich indirekt und ohne direkte Flamme grillen.

Dazu passend:

- Grillgemüse
- Gemüsefinish-Mild ohne Honig

Das Bild zeigt einen glasierten Lachs mit Dill und Grillgemüse. Das weboptimierte JPEG ist direkt unter der Einleitung eingebaut und wird auf der Fleischseite zusätzlich als anklickbares Thumbnail verwendet.

### Gemüsefinish-Fresh

- ID: `finishing-sauce-grillgemuese-haehnchen`
- Seite: `finishing-sauce.html`
- Version: 1.0.5
- Status: bestätigt
- Bild: `assets/gemuesefinish-fresh.jpg`
- Das Bild ist als Hero-Bild auf der Rezeptseite und als anklickbares Thumbnail unter Soßen & Finishes eingebunden.
- Rubrik: Soßen & Finishes

### Gemüsefinish-Mild

- ID: `gemuesefinish-mild`
- Seite: `gemuesefinish-mild.html`
- Version: 0.1.4
- Status: Arbeitsfassung
- Bild: `assets/gemuesefinish-mild.jpg`
- Das Bild ist als Hero-Bild auf der Rezeptseite und als anklickbares Thumbnail unter Soßen & Finishes eingebunden.
- Rubrik: Soßen & Finishes

Die Zubereitung folgt derselben Abfolge wie bei Gemüsefinish-Fresh. Das Finish wird nicht mitgegrillt.

### Grillgemüse

- ID: `grillgemuese-gasgrill`
- Seite: `grillgemuese.html`
- Version: 0.9.5
- Status: Arbeitsfassung
- Rubrik: Salate & Gemüse
- Bild: `assets/grillgemuese.jpg`
- Das Bild ist als Hero-Bild auf der Rezeptseite und als anklickbares Thumbnail unter Salate & Beilagen eingebunden.
- Noch zu prüfen: Mengen, Schnittgrößen, Brennereinstellung und genaue Zeitabstände

## Erledigt

- GitHub-Repository `henkhar/Kim` als dauerhafte Ablage eingerichtet
- GitHub Pages aktiviert
- Meta-Kim und dynamischen Projektstatus eingerichtet
- Übergang von einer Dokumentansicht zu einer Website beschlossen
- Apple-inspirierte Startseite als `index.html` umgesetzt
- Hamburger-Menü und responsive Navigation umgesetzt
- eigene Fleisch-, Vegan-, Grundlagen- und Salate-&-Beilagen-Seiten angelegt
- Grillgemüse als eigene Rezeptseite angelegt
- Gemüsefinish-Fresh als eigene Rezeptseite angelegt
- Gemüsefinish-Mild als zweite Finish-Rezeptseite angelegt
- Honig-Senf-Lachs vom Grill als erstes ausgearbeitetes Fischrezept angelegt
- Fischkarte auf `fleisch.html` mit dem neuen Rezept verknüpft
- passende Beilagen Grillgemüse und Gemüsefinish-Mild auf der Rezeptseite verlinkt
- erstes Rezeptbild für Honig-Senf-Lachs erstellt
- Bild als großes 16:9-Hero-Bild auf der Rezeptseite eingebaut
- fehlerhafte SVG-, Daten-URL- und JPEG-Einbindungen verworfen
- weboptimiertes JPEG `assets/honig-senf-lachs.jpg` eingebunden
- weboptimiertes JPEG `assets/grillgemuese.jpg` eingebunden
- Lachs-, Grillgemüse- und Finish-Bilder als Thumbnails auf den jeweiligen Übersichtsseiten ergänzt
- Bildlayout als Standard für weitere Rezeptseiten dokumentiert
- Rezeptversion Honig-Senf-Lachs auf 0.1.6 erhöht
- Rezeptversion Grillgemüse auf 0.9.3 erhöht
- Rezeptversion Gemüsefinish-Fresh auf 1.0.3 erhöht
- Rezeptversion Gemüsefinish-Mild auf 0.1.2 erhöht
- Buchversion auf 2.8.1 erhöht

- Einkaufsliste-Pilot für den Honig-Senf-Lachs umgesetzt
- Personenzahl, optionale Zutaten, Mengenberechnung, Abhaken, lokale Speicherung und Druckansicht ergänzt
- Rezeptversion Honig-Senf-Lachs auf 0.1.7 erhöht
- Buchversion auf 2.9.0 erhöht
- Einkaufsliste auf Grillgemüse, Gemüsefinish-Fresh und Gemüsefinish-Mild erweitert
- Mengenbereiche, optionale Zutaten und die Knoblauchalternative von Gemüsefinish-Mild unterstützt
- Rezeptversion Grillgemüse auf 0.9.4 erhöht
- Rezeptversion Gemüsefinish-Fresh auf 1.0.4 erhöht
- Rezeptversion Gemüsefinish-Mild auf 0.1.3 erhöht
- Buchversion auf 2.10.0 erhöht
- gemeinsame Einkaufsliste mit Auswahl mehrerer Rezepte ergänzt
- gleiche Zutaten über interne Zutaten-IDs und normierte Einheiten kumuliert
- Startseite und Hauptmenü mit der neuen Einkaufsliste verknüpft
- Buchversion auf 2.11.0 erhöht

- Grundlagen-Seite auf die Kapitel Kerntemperaturen und Garpunkte sowie Salzlake & Dry Brine reduziert
- Kapitel Salzlake & Dry Brine als Verfahren ergänzt
- Kapitel direkte Hitze, indirekte Hitze, Deckelregel und Zwei-Zonen-Aufbau entfernt
- Buchversion auf 2.12.0 erhöht
- Einkaufslisten-Block auf allen vier Rezeptseiten an das Seitenende verschoben
- Rezeptversionen auf 0.1.8, 0.9.5, 1.0.5 und 0.1.4 erhöht
- Buchversion auf 2.12.1 erhöht

## Offene Aufgaben

1. Honig-Senf-Lachs vom Grill gemeinsam testen und bestätigen.
2. Weitere Rezeptbilder im festgelegten 16:9-Hero-Stil ergänzen.
3. Weitere Fleischrezepte schrittweise ausarbeiten und verlinken.
4. Vegane Rezepte schrittweise ergänzen.
5. Weitere Salate und Beilagen wie Nudelsalate ergänzen.
6. Gemüsefinish-Mild gemeinsam testen und bestätigen.
7. Arbeitsfassung Grillgemüse gemeinsam prüfen und auf Version 1.0.0 setzen.
8. Übergangsseite `kochbuch.html` später reduzieren oder auflösen.
9. Später Suche, Filter, PWA und Favoriten prüfen.
10. Gemeinsame Einkaufsliste später um unterschiedliche Personenzahlen pro Rezept erweitern.
11. Eigene Fotos später bei Bedarf ergänzen oder bestehende Bilder ersetzen.

## Verbindliche Hinweise für die nächste Sitzung

- `index.html`, `00_Meta-Kim.md` und `00_Projektstatus.md` zuerst vollständig lesen.
- Bei Arbeiten an Fleisch zusätzlich `fleisch.html` lesen.
- Bei Arbeiten am Honig-Senf-Lachs zusätzlich `honig-senf-lachs.html` lesen.
- Bei Arbeiten an Salaten, Gemüse, Soßen oder Finishes zusätzlich `gemuese-salat.html` lesen.
- Bei Arbeiten an Gemüsefinish-Fresh zusätzlich `finishing-sauce.html` lesen.
- Bei Arbeiten an Gemüsefinish-Mild zusätzlich `gemuesefinish-mild.html` lesen.
- Bei Arbeiten an veganen Inhalten zusätzlich `vegan.html` lesen.
- Bei Arbeiten an Grillwissen oder Temperaturen zusätzlich `grundlagen.html` lesen.
- Bei Änderungen an der gemeinsamen Einkaufsliste zusätzlich `einkaufsliste-gesamt.html` lesen.
- Bei Rezeptänderungen immer die zuständige Rezeptseite laden.
- Rezeptkarten auf Übersichtsseiten enthalten keine farbigen Status- oder Informations-Pills.
- Neue Rezeptbilder orientieren sich am bestätigten 16:9-Hero-Stil des Honig-Senf-Lachses.
- Food-Fotos werden als weboptimierte JPEG-Dateien gespeichert und auf Übersichtsseiten lazy geladen.
- Gemüsefinish-Fresh gilt als bestätigt.
- Honig-Senf-Lachs, Gemüsefinish-Mild und Grillgemüse bleiben bis zur gemeinsamen Kontrolle Arbeitsfassungen.
- Änderungen an Website, Meta und Status müssen synchron gehalten werden.

## Änderungshistorie
### Version 2.12.1 – 03.08.2026

- Block „Einkaufsliste erstellen“ auf Honig-Senf-Lachs, Grillgemüse, Gemüsefinish-Fresh und Gemüsefinish-Mild an das Ende des Rezeptinhalts verschoben
- Einkaufslisten-Block steht nun direkt vor dem Zurück-Link
- neue Position als Standard für künftige Rezeptseiten dokumentiert
- Rezeptversionen und Buchversion synchron erhöht

### Version 2.12.0 – 03.08.2026

- Reihenfolge der Grundlagen neu festgelegt: zuerst Kerntemperaturen und Garpunkte, danach Salzlake & Dry Brine
- Salzlake und Dry Brine als kompaktes Verfahrenskapitel ergänzt
- Kapitel direkte Hitze, indirekte Hitze, Deckelregel und Zwei-Zonen-Aufbau entfernt
- Buchversion auf 2.12.0 erhöht

### Version 2.11.0 – 02.08.2026

- neue Seite `einkaufsliste-gesamt.html` ergänzt
- Auswahl mehrerer Rezepte mit einer gemeinsamen Personenzahl umgesetzt
- gleiche Zutaten über dauerhafte interne Zutaten-IDs kumuliert
- kompatible Volumeneinheiten intern vereinheitlicht und als EL beziehungsweise TL ausgegeben
- optionale Zutaten, Mengenbereiche und die Knoblauchvariante von Gemüsefinish-Mild berücksichtigt
- Startseite und Hauptmenü mit der gemeinsamen Einkaufsliste verknüpft
- Buchversion auf 2.11.0 erhöht

### Version 2.10.0 – 02.08.2026

- Einkaufsliste auf Grillgemüse, Gemüsefinish-Fresh und Gemüsefinish-Mild erweitert
- alle vier Einzelrezepte verwenden dieselbe Einkaufsliste
- optionale Zutaten und Mengenbereiche werden berücksichtigt
- bei Gemüsefinish-Mild kann zwischen Knoblauchpulver und frischen Knoblauchzehen gewählt werden
- Rezeptversion Grillgemüse auf 0.9.4 erhöht
- Rezeptversion Gemüsefinish-Fresh auf 1.0.4 erhöht
- Rezeptversion Gemüsefinish-Mild auf 0.1.3 erhöht
- Buchversion auf 2.10.0 erhöht

### Version 2.9.0 – 02.08.2026

- Einkaufsliste-Pilot für den Honig-Senf-Lachs ergänzt
- Personenzahl direkt auf der Rezeptseite auswählbar
- Zutatenmengen automatisch von der Grundmenge für 4 Personen umgerechnet
- optionale Zutaten ein- und ausschaltbar
- neue Seite `einkaufsliste.html` mit Abhakfunktion, lokaler Speicherung, Zurücksetzen und Druckansicht
- Rezeptversion Honig-Senf-Lachs auf 0.1.7 erhöht
- Buchversion auf 2.9.0 erhöht
- Einkaufsliste auf Grillgemüse, Gemüsefinish-Fresh und Gemüsefinish-Mild erweitert
- Mengenbereiche, optionale Zutaten und die Knoblauchalternative von Gemüsefinish-Mild unterstützt
- Rezeptversion Grillgemüse auf 0.9.4 erhöht
- Rezeptversion Gemüsefinish-Fresh auf 1.0.4 erhöht
- Rezeptversion Gemüsefinish-Mild auf 0.1.3 erhöht
- Buchversion auf 2.10.0 erhöht

### Version 2.8.1 – 02.08.2026

- Gemüsefinish-Fresh mit dem Hero-Bild `assets/gemuesefinish-fresh.jpg` ergänzt
- Gemüsefinish-Mild mit dem Hero-Bild `assets/gemuesefinish-mild.jpg` ergänzt
- beide Bilder als anklickbare, lazy-geladene Thumbnails unter Soßen & Finishes eingebaut
- stabile ASCII-Dateinamen für die beiden hochgeladenen Bilder angelegt
- Rezeptversion Gemüsefinish-Fresh auf 1.0.3 erhöht
- Rezeptversion Gemüsefinish-Mild auf 0.1.2 erhöht
- Buchversion auf 2.8.1 erhöht

### Version 2.8.0 – 02.08.2026

- Honig-Senf-Lachs auf das weboptimierte JPEG `assets/honig-senf-lachs.jpg` umgestellt
- Grillgemüse mit dem Hero-Bild `assets/grillgemuese.jpg` ergänzt
- Lachsbild als anklickbares Thumbnail auf der Fleischseite eingebaut
- Grillgemüsebild als anklickbares Thumbnail unter Salate & Beilagen eingebaut
- Thumbnails mit `loading="lazy"` und 16:9-Zuschnitt umgesetzt
- Rezeptversion Honig-Senf-Lachs auf 0.1.6 erhöht
- Rezeptversion Grillgemüse auf 0.9.3 erhöht
- Rezeptversion Gemüsefinish-Fresh auf 1.0.3 erhöht
- Rezeptversion Gemüsefinish-Mild auf 0.1.2 erhöht
- Buchversion auf 2.8.1 erhöht

### Version 2.7.4 – 02.08.2026

- vom Nutzer hochgeladenes Originalbild `assets/honi-senf-lachs.png` übernommen
- beschädigte JPEG-Einbindung auf der Rezeptseite durch das Original-PNG ersetzt
- korrekte Bildabmessungen 1672 × 941 Pixel hinterlegt
- Rezeptversion Honig-Senf-Lachs auf 0.1.5 erhöht
- Fleischseite und Startseite auf Buchversion 2.7.4 aktualisiert
- beschädigte alte JPEG-Datei entfernt

### Version 2.7.3 – 01.08.2026

- beschädigte direkte JPEG-Daten-URL aus `honig-senf-lachs.html` entfernt
- optimiertes Rezeptbild als Datei `assets/honig-senf-lachs.jpg` im Repository gespeichert
- Rezeptseite mit der relativen Bildadresse verknüpft
- Rezeptversion Honig-Senf-Lachs auf 0.1.3 erhöht
- Buchversion auf 2.7.3 erhöht

### Version 2.7.2 – 01.08.2026

- nicht zuverlässig dargestellte externe SVG-Datei entfernt
- Versuch einer direkten JPEG-Einbettung in `honig-senf-lachs.html`
- vorhandenes 16:9-Layout, abgerundete Ecken, Schatten, Alternativtext und Bildunterschrift beibehalten
- Rezeptversion Honig-Senf-Lachs auf 0.1.2 erhöht
- Buchversion auf 2.7.2 erhöht

### Version 2.7.1 – 01.08.2026

- erstes Rezeptbild beim Honig-Senf-Lachs ergänzt
- Bildlayout als Vorlage für weitere Rezeptseiten festgelegt

### Version 2.7.0 – 01.08.2026

- neue Datei `honig-senf-lachs.html` angelegt
- Honig-Senf-Lachs vom Grill als Arbeitsfassung Version 0.1.0 aufgenommen
- vollständige Zutaten, Glasur, Ziehzeit und Grillablauf dokumentiert
- indirekte Grillmethode bei 180–200 °C, Hautseite unten und ohne Wenden festgehalten
- optionales Nachstreichen nach etwa 8 Minuten ergänzt
- Warnhinweis zum schnellen Verbrennen von Honig aufgenommen
- Grillgemüse und Gemüsefinish-Mild als passende Beilagen verlinkt
- Fischbereich auf `fleisch.html` mit dem neuen Rezept verknüpft
- geplantes Lachsfilet aus der Planung entfernt
- Rezeptanzahl auf 4 erhöht
- Buchversion auf 2.7.0 erhöht

### Version 2.6.1 – 01.08.2026

- Zubereitung von Gemüsefinish-Mild an die Abfolge von Gemüsefinish-Fresh angeglichen
- Rezeptversion Gemüsefinish-Mild auf 0.1.1 erhöht

### Version 2.6.0 – 01.08.2026

- Gemüsefinish-Mild als zweite Finish-Rezeptseite angelegt

### Version 2.5.2 – 01.08.2026

- Zutatenverhältnis von Gemüsefinish-Fresh angepasst

### Version 2.5.1 – 01.08.2026

- farbige Status- und Informations-Pills aus den Rezeptkarten entfernt

### Version 2.5.0 – 01.08.2026

- Hauptbereich „Gemüse & Salat“ in „Salate & Beilagen“ umbenannt
- Rubriken „Salate & Gemüse“ und „Soßen & Finishes“ angelegt

### Version 2.4.1 – 01.08.2026

- runden Home-Button auf den Unter- und Rezeptseiten ergänzt

### Version 2.4.0 – 31.07.2026

- neue Grundlagen-Seite angelegt

### Version 2.3.0 – 31.07.2026

- neue vegane Platzhalterseite angelegt

### Version 2.2.0 – 27.07.2026

- Übersichtsseite für Gemüse & Salat sowie getrennte Rezeptseiten ergänzt

### Version 2.1.0 – 26.07.2026

- neue Fleisch-Übersichtsseite angelegt

### Version 2.0.0 – 26.07.2026

- Kochbuch auf eine mehrseitige Website-Architektur umgestellt