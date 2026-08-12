# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.15.3  
**Letzte Aktualisierung:** 12.08.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt ist eine mehrseitige, statische Kochbuch-Website auf GitHub Pages.

- `index.html` – Startseite und eingebetteter maschinenlesbarer Projektstatus
- `fleisch.html` – Übersicht für Rind, Geflügel, Schwein und Fisch
- `gemuese-salat.html` – Übersicht Salate & Beilagen
- `vegan.html` – vorbereiteter Bereich für vegane Rezepte
- `grundlagen.html` – Kerntemperaturen, Garpunkte, Salzlake und Dry Brine
- `einkaufsliste.html` – Einkaufsliste für ein Rezept
- `einkaufsliste-gesamt.html` – gemeinsame Einkaufsliste für mehrere Rezepte
- `kochbuch.html` – Übergangsseite der früheren Gesamtansicht
- `00_Meta-Kim.md` – stabile Regeln
- `00_Projektstatus.md` – dynamischer Zustand und Änderungshistorie

## Startseite

Die Hauptnavigation enthält Fleisch, Salate & Beilagen, Vegan, Grundlagen und Einkaufsliste. Unterhalb bleiben die drei großen Kategorie-Karten Fleisch, Salate & Beilagen und Vegan.

Darunter befindet sich der bildstarke Bereich **Neu hinzugefügt** mit vier direkt anklickbaren Rezeptkarten:

1. Beer Can Chicken – Geflügel
2. Chicken Asado – Geflügel
3. Entrecôte Steakhouse – Rind
4. Keto-Pudding – Salate & Beilagen

Die Karten zeigen jeweils ein 16:9-Rezeptbild, die Rubrik, den Rezeptnamen und einen dezenten Öffnen-Link. Auf großen Bildschirmen stehen vier Karten nebeneinander, auf Tablets zwei pro Reihe und auf Smartphones untereinander.

## Aktueller Bestand

- 9 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 8 Arbeitsfassungen
- 9 eigenständige Rezeptseiten
- 9 Rezeptseiten mit Hero-Bild
- beide Einkaufslisten unterstützen alle 9 Rezepte
- sichtbare Versions- und Statushinweise bleiben ausgeblendet

## Rezeptübersicht

### Fleisch

#### Rind

- Entrecôte Steakhouse – Version 0.1.1 – `entrecote-steakhouse.html`

#### Geflügel

- Chicken Asado – Version 0.1.1 – `chicken-asado.html`
- Beer Can Chicken – Version 0.1.0 – `beer-can-chicken.html`

#### Schwein

- Schweinenackensteak mit Senf-Kräuter-Sauce – Version 0.1.1 – `schweinenackensteak-senf-kraeuter.html`

#### Fisch

- Honig-Senf-Lachs vom Grill – Version 0.1.9 – `honig-senf-lachs.html`

### Salate & Beilagen

- Grillgemüse – Version 0.9.7 – `grillgemuese.html`
- Gemüsefinish-Fresh – Version 1.0.6 – bestätigt – `finishing-sauce.html`
- Gemüsefinish-Mild – Version 0.1.5 – `gemuesefinish-mild.html`
- Keto-Pudding – Version 0.1.1 – `keto-pudding.html`

## Rezeptbilder Geflügel

- Chicken Asado: `assets/Chicken_asado.jpg`
- Beer Can Chicken: `assets/beer_can_chicken.jpg`
- Beide JPEGs sind als 16:9-Hero-Bilder auf den Rezeptseiten eingebunden.
- In der Geflügel-Kategorie der Fleischübersicht werden beide Bilder als anklickbare, lazy-geladene Thumbnails angezeigt.
- Die unveränderten Rezeptinhalte liegen zusätzlich in `chicken-asado-basis.html` und `beer-can-chicken-basis.html`; `fleisch-basis.html` bewahrt die unveränderte Fleischübersicht. Die sichtbaren Seiten ergänzen daraus ausschließlich die Bilder.

## Einkaufslisten

### Einzelrezept

`einkaufsliste.html` unterstützt neun Rezepte einschließlich Chicken Asado und Beer Can Chicken.

Die Fehlerursache vom 12.08.2026 lag nicht in den Rezeptformularen: Die korrekte `recipe`-ID wurde über den Query-Parameter übergeben. Der bisherige Wrapper lud jedoch `einkaufsliste-basis.html` in ein iframe und schrieb den gepatchten Inhalt anschließend mit `document.write()` erneut hinein. Dabei wurde das JavaScript der Basisdatei im betroffenen Browser nicht ausgeführt. Dadurch blieben statischer Lachs-Titel, leere Zutatenliste und funktionslose Bedienelemente sichtbar.

Die Basisdatei wird jetzt als vollständiges `srcdoc`-Dokument geladen. Der Query-String der äußeren Seite wird ausdrücklich an die Basislogik übergeben. `Neu berechnen` lädt die äußere Einkaufsliste mit den neuen GET-Parametern; Häkchen, Reset und Senden arbeiten wieder innerhalb des ausgeführten Dokuments.

### Gemeinsame Einkaufsliste

`einkaufsliste-gesamt.html` enthält alle neun Rezepte als auswählbare Rezepte. Gleiche Zutaten werden über dauerhafte Zutaten-IDs zusammengeführt.

Da die gemeinsame Liste dieselbe problematische `document.write()`-Technik nutzte, wurde sie im gleichen Zug ebenfalls auf die zuverlässige `srcdoc`-Ausführung umgestellt.

## Offene Aufgaben

1. Beer Can Chicken gemeinsam testen und Garzeit sowie Gewürzmenge präzisieren.
2. Chicken Asado gemeinsam testen und anschließend Mengen, Grillhitze und Gesamtgrillzeit präzisieren.
3. Grillgemüse gemeinsam testen und später auf Version 1.0.0 setzen.
4. Honig-Senf-Lachs und Gemüsefinish-Mild gemeinsam prüfen.
5. Weitere Salate, Beilagen und vegane Rezepte ergänzen.
6. Übergangsseite `kochbuch.html` später reduzieren oder auflösen.

## Verbindliche Hinweise

- Neue Rezeptseiten zeigen keine sichtbaren Versions- oder Arbeitsstatusangaben.
- Interne Rezeptversionen bleiben als HTML-Meta-Daten erhalten.
- Der Einkaufslistenblock steht am Ende des Rezeptinhalts.
- Die Fleisch-Unterkategorie heißt `Geflügel`.
- Food-Fotos werden als weboptimierte JPEG-Dateien eingebunden.
- Frühere Detailstände bleiben über die Git-Commit-Historie nachvollziehbar.

## Änderungshistorie

### Version 2.15.3 – 12.08.2026

- Fehleranalyse der Einzel-Einkaufsliste durchgeführt: Rezeptparameter war korrekt, Basis-JavaScript wurde nach `document.write()` jedoch nicht ausgeführt
- `einkaufsliste.html` auf zuverlässige `srcdoc`-Ausführung umgestellt
- Rezept-ID und Personenzahl werden wieder korrekt aus der URL übernommen
- `Neu berechnen`, `Senden`, gespeicherte Häkchen und `Häkchen zurücksetzen` wieder mit ausgeführter Basislogik verbunden
- gemeinsame Einkaufsliste wegen identischer Fehlerquelle ebenfalls umgestellt
- Buchversion auf 2.15.3 erhöht

### Version 2.15.2 – 04.08.2026

- Startseite um den Bereich **Neu hinzugefügt** erweitert
- Beer Can Chicken, Chicken Asado, Entrecôte Steakhouse und Keto-Pudding als bildstarke Rezeptkarten ergänzt
- Karten mit Rubrik, Rezeptname und direkter Verlinkung ausgestattet
- responsives Raster mit vier, zwei beziehungsweise einer Karte pro Reihe umgesetzt

### Korrektur zu Version 2.15.1 – 04.08.2026

- die bereits hochgeladenen Dateien `assets/Chicken_asado.jpg` und `assets/beer_can_chicken.jpg` tatsächlich eingebunden
- Chicken Asado und Beer Can Chicken mit 16:9-Hero-Bild, Alt-Text und Bildunterschrift ergänzt
- Geflügel-Übersicht mit zwei anklickbaren Thumbnails erweitert

### Version 2.15.1 – 04.08.2026

- Startseite vereinfacht
- Einkaufsliste in die Hauptnavigation verschoben
- drei untere Schnellzugriffe entfernt

### Version 2.15.0 – 04.08.2026

- Fleisch-Unterkategorie Hähnchen in Geflügel umbenannt
- Chicken Asado der Rubrik Geflügel zugeordnet
- Beer Can Chicken als zweites Geflügelrezept ergänzt
- Einzel- und gemeinsame Einkaufsliste auf neun Rezepte erweitert

### Version 2.14.0 – 03.08.2026

- Chicken Asado als neues Geflügelrezept ergänzt

### Version 2.13.2 – 03.08.2026

- Grillgemüse mit neuen Zutaten und neuem Plancha-Ablauf überarbeitet

### Version 2.13.1 – 03.08.2026

- Bilder für Entrecôte Steakhouse, Schweinenackensteak und Keto-Pudding eingebunden

### Version 2.13.0 – 03.08.2026

- Entrecôte Steakhouse, Schweinenackensteak mit Senf-Kräuter-Sauce und Keto-Pudding ergänzt

### Version 2.12.2 – 03.08.2026

- sichtbare Versions- und Statushinweise entfernt

### Version 2.12.1 – 03.08.2026

- Einkaufslistenblock auf Rezeptseiten an das Seitenende verschoben

### Version 2.12.0 – 03.08.2026

- Grundlagen auf Kerntemperaturen und Salzlake & Dry Brine konzentriert
