# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.19.0  
**Letzte Aktualisierung:** 10.10.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt ist eine mehrseitige, statische Kochbuch-Website auf GitHub Pages.

- `index.html` – Startseite und eingebetteter maschinenlesbarer Projektstatus
- `fleisch.html` – Übersicht für Rind, Geflügel, Schwein, Lamm und Fisch
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

1. Toskanisches Lammkarree – Lamm
2. Beer Can Chicken – Geflügel
3. Chicken Asado – Geflügel
4. Entrecôte Steakhouse – Rind

Die Karten zeigen jeweils ein 16:9-Rezeptbild, die Rubrik, den Rezeptnamen und einen dezenten Öffnen-Link. Auf großen Bildschirmen stehen vier Karten nebeneinander, auf Tablets zwei pro Reihe und auf Smartphones untereinander.

## Aktueller Bestand

- 13 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 12 Arbeitsfassungen
- 13 eigenständige Rezeptseiten
- 13 Rezeptseiten mit Hero-Bild
- beide Einkaufslisten unterstützen nun 13 Rezepte inklusive Ibérico und Salsa Verde
- sichtbare Versions- und Statushinweise bleiben ausgeblendet

## Rezeptübersicht

### Fleisch

#### Rind

- Entrecôte Steakhouse – Version 0.1.1 – `entrecote-steakhouse.html`

#### Geflügel

- Chicken Asado – Version 0.1.1 – `chicken-asado.html`
- Beer Can Chicken – Version 0.1.0 – `beer-can-chicken.html`

#### Schwein

- Ibérico Bellota Carré – Version 0.1.4 – `iberico-bellota-carre.html` – Arbeitsfassung; Einkaufslistenintegration vorhanden

- Schweinenackensteak mit Senf-Kräuter-Sauce – Version 0.1.1 – `schweinenackensteak-senf-kraeuter.html`

#### Lamm

- Lammlachse mit Rosmarin – Version 0.1.0 – `lammlachse-klassisch.html` – Arbeitsfassung, mit eigenem Rezeptfoto `assets/Lammlachse.jpeg`; direkt/indirekt gegrillt, beide Einkaufslisten integriert


- Toskanisches Lammkarree – Version 0.1.2 – `toskanisches-lammkarree.html`
  - Grundmenge 4 Portionen
  - direkter und indirekter Grillbereich
  - Kräuter-Rub aus Rosmarin, Thymian, Salbei, granuliertem Knoblauch und Zwiebel, Chili und Salz
  - Mop aus trockenem Weißwein, Wermut und Honig
  - 53 °C Kerntemperatur vor der Ruhephase und etwa 55 °C nach 10 Minuten Ruhezeit
  - Kartoffeln und Frühlingszwiebeln als Beilage
  - für die Kartoffeln wurden 2 EL Rapsöl als gemeinsame Rezeptfestlegung ergänzt
  - Quellenhinweis bleibt nur intern dokumentiert und wird nicht sichtbar auf der Rezeptseite gezeigt
  - Bild: `assets/toskanisches_lammkarree.jpg`
  - Bild als 16:9-Hero auf der Rezeptseite, als Thumbnail in der Lamm-Übersicht und als neueste Karte auf der Startseite eingebunden

#### Fisch

- Honig-Senf-Lachs vom Grill – Version 0.1.9 – `honig-senf-lachs.html`

### Salate & Beilagen

- Salsa Verde – Version 0.1.1 – `salsa-verde.html` – Arbeitsfassung; mit Einkaufslistenintegration und eigenem Foto

- Grillgemüse – Version 0.9.7 – `grillgemuese.html`
- Gemüsefinish-Fresh – Version 1.0.6 – bestätigt – `finishing-sauce.html`
- Gemüsefinish-Mild – Version 0.1.5 – `gemuesefinish-mild.html`
- Keto-Pudding – Version 0.1.1 – `keto-pudding.html`

## Rezeptbilder Geflügel

- Chicken Asado: `assets/Chicken_asado.jpg`
- Beer Can Chicken: `assets/beer_can_chicken.jpg`
- Beide JPEGs sind als 16:9-Hero-Bilder auf den Rezeptseiten eingebunden.
- In der Geflügel-Kategorie der Fleischübersicht werden beide Bilder als anklickbare, lazy-geladene Thumbnails angezeigt.
- Die unveränderten Rezeptinhalte liegen zusätzlich in `chicken-asado-basis.html` und `beer-can-chicken-basis.html`; `fleisch-basis.html` bewahrt die unveränderte Fleischübersicht. Die sichtbaren Seiten ergänzen daraus die aktuellen Erweiterungen.

## Einkaufslisten

### Einzelrezept

`einkaufsliste.html` unterstützt zehn Rezepte einschließlich Chicken Asado, Beer Can Chicken und Toskanischem Lammkarree.

Für das Toskanische Lammkarree werden Lammkarree, Weißwein, Wermut, Honig, Kartoffeln, Frühlingszwiebeln, 2 EL Rapsöl und sämtliche Rub-Zutaten auf die Personenzahl skaliert.

Die Fehlerursache vom 12.08.2026 lag nicht in den Rezeptformularen: Die korrekte `recipe`-ID wurde über den Query-Parameter übergeben. Der frühere Wrapper schrieb den gepatchten Inhalt nach dem Laden erneut mit `document.write()` in ein iframe, wodurch das JavaScript der Basisdatei im betroffenen Browser nicht ausgeführt wurde. Die Einzel-Einkaufsliste nutzt deshalb seit Version 2.15.3 die zuverlässige `srcdoc`-Ausführung und übergibt den Query-String ausdrücklich an die Basislogik.

### Gemeinsame Einkaufsliste

`einkaufsliste-gesamt.html` enthält alle zehn Rezepte als auswählbare Rezepte. Gleiche Zutaten werden über dauerhafte Zutaten-IDs zusammengeführt. Das Toskanische Lammkarree ist als eigene Auswahl mit Grundmenge für 4 Personen ergänzt; sein Rapsöl verwendet die bestehende gemeinsame Zutaten-ID `rapsoel` und wird dadurch mit Rapsöl aus anderen Rezepten korrekt zusammengeführt.

Die gemeinsame Liste verwendet ebenfalls die seit Version 2.15.3 eingeführte `srcdoc`-Ausführung.

## Offene Aufgaben

1. Toskanisches Lammkarree gemeinsam testen und anschließend Garzeit sowie Rub-Menge präzisieren.
2. Beer Can Chicken gemeinsam testen und Garzeit sowie Gewürzmenge präzisieren.
3. Chicken Asado gemeinsam testen und anschließend Mengen, Grillhitze und Gesamtgrillzeit präzisieren.
4. Grillgemüse gemeinsam testen und später auf Version 1.0.0 setzen.
5. Honig-Senf-Lachs und Gemüsefinish-Mild gemeinsam prüfen.
6. Weitere Salate, Beilagen und vegane Rezepte ergänzen.
7. Übergangsseite `kochbuch.html` später reduzieren oder auflösen.

## Verbindliche Hinweise

- Neue Rezeptseiten zeigen keine sichtbaren Versions- oder Arbeitsstatusangaben.
- Interne Rezeptversionen bleiben als HTML-Meta-Daten erhalten.
- Der Einkaufslistenblock steht am Ende des Rezeptinhalts.
- Fleisch-Unterkategorien sind derzeit Rind, Geflügel, Schwein, Lamm und Fisch.
- Food-Fotos werden als weboptimierte JPEG-Dateien eingebunden.
- Quellenbasierte Rezepte dürfen fehlende oder unklare Angaben nicht stillschweigend ergänzen; gemeinsame Festlegungen werden dokumentiert und anschließend als normaler Rezeptbestandteil geführt.
- Quellenhinweise bleiben intern und erscheinen nicht auf der sichtbaren Rezeptseite, sofern sie nicht ausdrücklich Teil des Kochbuchinhalts sein sollen.
- Frühere Detailstände bleiben über die Git-Commit-Historie nachvollziehbar.

## Änderungshistorie

### Version 2.19.0 – 10.10.2026

- Neue eigenständige Ansicht `einkaufsliste-ansicht.html` für den Linkversand.
- Beide Einkaufslisten haben zusätzlich zum PDF-Versand die Option „Link senden“.
- Geteilte Listen behalten Zutaten, Mengen und Häkchen-Ausgangszustand bei. Abhaken erfolgt unabhängig je Gerät.



### Version 2.18.6 – 10.10.2026

- „Senden“ in beiden Einkaufslisten erzeugt jetzt eine formatierte PDF-Datei statt eines Links.
- Unterstützt Dateifreigabe über das Betriebssystem (wenn verfügbar); andernfalls PDF-Download zum manuellen Anhängen.
- Separaten Druckknopf für die Druckansicht wiederhergestellt.
- Benötigt zum Erzeugen der PDF-Datei die jsPDF-Bibliothek vom CDN; bei Ladefehler öffnet sich der Druckdialog.


### Version 2.18.5 – 10.10.2026

- Grundlagen-Tabelle um Lamm (Karree/Lammlachse) und Schweine-Carré einschließlich Ibérico ergänzt.
- Sicherheitshinweis unter der Tabelle umfasst alle Fleischarten einschließlich Rind sowie Fisch und unterscheidet Genuss-Gargrad von hygienischen Mindesttemperaturen.
- Hinweis aufgenommen, dass einzelne ältere Mindestwerte der Tabelle kulinarische Richtwerte und keine allgemeinen Sicherheitsgrenzen sind.


### Version 2.18.4 – 10.10.2026

- Hochgeladenes Bild `assets/Lammlachse.jpeg` als Hero-Bild im Rezept und als Thumbnail in der Fleischübersicht (Lamm) eingebunden.
- Lammlachse mit Bild unter „Neu hinzugefügt“ auf der Startseite aufgenommen.
- Lammlachs-Rezeptversion auf 0.1.1 erhöht.


### Version 2.18.3 – 10.10.2026

- Klassische Lammlachse mit Rosmarin, Thymian, Knoblauch und Butter als dreizehntes Rezept angelegt.
- Fleischübersicht (Lamm), Startseiten-Metadaten und beide Einkaufslisten ergänzt.
- Eigenes Rezeptfoto noch offen; deshalb bewusst kein fremdes Lammfoto verwendet.


### Version 2.18.3 – 10.10.2026

- Ibérico Bellota Carré und Salsa Verde in Einzel- und gemeinsame Einkaufsliste integriert.
- Mengen für vier Personen als Grundlage, Rosmarin optional, Salz und Pfeffer nach Geschmack.
- Salsa-Verde-JPEG als Rezept-Hero und Thumbnail in der Soßenübersicht eingebunden.


### Version 2.18.1 – 10.10.2026

- Ibérico-Rezeptseite an die vorhandene Beer-Can-Chicken-Formatvorlage angeglichen: Hero-Bild, Faktenkarten, zweispaltige Zutaten/Zubereitung, nummerierte Schritte, Kim-Tipp und Detailkarten.
- Inhalte des Rezeptes beibehalten; Dry Brining bleibt optional und Salsa Verde separat verlinkt.


### Version 2.18.0 – 10.10.2026

- Ibérico: Zubereitungsschritte 1 und 6 entfernt, Salzmenge aus Hauptrezept genommen, Dry Brining als optionalen Anhang angefügt
- Salsa Verde als eigenständiges Rezept unter Soßen & Finishes angelegt und in Kim-Tipp verlinkt
- JPEG auf der Rezeptseite mit aktualisiertem Cache-Parameter eingebunden; Dateiname bleibt unverändert
- Rezeptbild und automatische Einkaufslistenintegration der Salsa Verde noch offen


### Version 2.17.1 – 10.10.2026

- Bereits hochgeladenes Ibérico-JPEG im 16:9-Hero der Rezeptseite sowie in Fleischübersicht und Startseite eingebunden
- Rezeptversion auf 0.1.1 erhöht


### Version 2.17.1 – 10.10.2026

- Ibérico Bellota Carré als elftes Rezept ergänzt, unter Schwein verlinkt und auf der Startseite aufgenommen
- Dry Brining, Grillmethode und optionale Salsa Verde dokumentiert
- Automatische Einkaufslistenintegration noch offen


### Version 2.17.1 – 22.08.2026

- JPEG `assets/toskanisches_lammkarree.jpg` geprüft und eingebunden
- Toskanisches Lammkarree auf Rezeptversion 0.1.2 erhöht
- 16:9-Hero-Bild mit Alternativtext und Bildunterschrift ergänzt
- Lamm-Kategorie in der Fleischübersicht um ein anklickbares Thumbnail erweitert
- Toskanisches Lammkarree als neueste Karte im Bereich **Neu hinzugefügt** aufgenommen
- Keto-Pudding dort aus dem Vierer-Raster verdrängt; Rezept und Kategorie bleiben unverändert erhalten
- Anzahl der Rezeptseiten mit Hero-Bild auf 10 erhöht
- Buchversion auf 2.17.1 erhöht

### Version 2.16.1 – 22.08.2026

- Toskanisches Lammkarree auf Rezeptversion 0.1.1 erhöht
- 2 EL Rapsöl für die Kartoffeln festgelegt
- Kartoffelschritt entsprechend auf Rapsöl angepasst
- Kim-Tipp zur dünnen Benetzung und hohen direkten Hitze ergänzt
- sichtbaren Quellenblock und sonstige redaktionelle Quellenformulierungen von der Rezeptseite entfernt
- Garpunkt als normaler Rezeptbestandteil formuliert
- Einzel- und gemeinsame Einkaufsliste auf 2 EL Rapsöl aktualisiert
- Rapsöl in der gemeinsamen Einkaufsliste über die bestehende Zutaten-ID zusammengeführt
- Buchversion auf 2.16.1 erhöht

### Version 2.16.0 – 22.08.2026

- Toskanisches Lammkarree als zehntes Rezept angelegt
- neue Fleisch-Unterkategorie **Lamm** ergänzt
- Rezept aus der bereitgestellten BURNHARD-PDF in den bestehenden Rezeptstil übertragen
- Mengen, Zeiten und Temperaturangaben der Vorlage beibehalten
- fehlende Ölmenge für die Kartoffeln zunächst als offenen Punkt dokumentiert
- Einzel-Einkaufsliste um das Lammkarree erweitert
- gemeinsame Einkaufsliste um das Lammkarree erweitert
- Rezeptzahl auf 10 und Arbeitsfassungen auf 9 erhöht
- Buchversion auf 2.16.0 erhöht

### Version 2.15.3 – 12.08.2026

- Fehleranalyse der Einzel-Einkaufsliste durchgeführt: Rezeptparameter war korrekt, Basis-JavaScript wurde nach `document.write()` jedoch nicht ausgeführt
- `einkaufsliste.html` auf zuverlässige `srcdoc`-Ausführung umgestellt
- Rezept-ID und Personenzahl werden wieder korrekt aus der URL übernommen
- `Neu berechnen`, `Senden`, gespeicherte Häkchen und `Häkchen zurücksetzen` wieder mit ausgeführter Basislogik verbunden
- gemeinsame Einkaufsliste wegen identischer Fehlerquelle ebenfalls umgestellt

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
