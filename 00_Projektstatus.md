# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.15.1  
**Letzte Aktualisierung:** 04.08.2026  
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

Die Startseite zeigt in der oberen Hauptnavigation jetzt direkt:

1. Fleisch
2. Salate & Beilagen
3. Vegan
4. Grundlagen
5. Einkaufsliste

Unterhalb bleiben ausschließlich die drei großen Kategorie-Karten Fleisch, Salate & Beilagen und Vegan. Die früheren Schnellzugriffe Grundlagen, Gemeinsame Einkaufsliste und Gesamtes Kochbuch wurden aus diesem Bereich entfernt. `kochbuch.html` bleibt technisch weiterhin erreichbar.

## Aktueller Bestand

- 9 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 8 Arbeitsfassungen
- 9 eigenständige Rezeptseiten
- 7 Rezeptseiten mit Hero-Bild
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

## Beer Can Chicken

- ID: `beer-can-chicken`
- Rubrik: Fleisch → Geflügel
- Grundmenge: 2 Personen / 1 (Mais-)Hähnchen
- Methode: aufrecht auf einer geöffneten 0,5-l-Bierdose oder einem Hähnchenhalter im Backofen garen
- Garphase: etwa 60 Minuten bei 170 °C Umluft
- Finish: mit Olivenöl und Hähnchengewürz einpinseln und etwa 4 Minuten bei 220 °C knusprig backen
- Beilage: gelbe und rote Zwiebeln mit Bratensud, Salz und Butter
- Kerntemperatur wird zusätzlich über die Grundlagen geprüft
- Noch ohne Rezeptbild

## Rubrik Geflügel

Die bisherige Kategorie `Hähnchen` wurde auf den aktuellen Übersichts- und Rezeptseiten in `Geflügel` umbenannt. Der Seitenanker lautet jetzt `#gefluegel`.

## Einkaufslisten

### Einzelrezept

`einkaufsliste.html` unterstützt jetzt neun Rezepte. Für Beer Can Chicken werden Hähnchen, Bier, beide Zwiebelsorten, Hähnchengewürz, Olivenöl, Salz und Butter ausgehend von zwei Personen skaliert.

### Gemeinsame Einkaufsliste

`einkaufsliste-gesamt.html` enthält Beer Can Chicken als zusätzliche Rezeptauswahl. Gleiche Zutaten werden über bestehende dauerhafte Zutaten-IDs zusammengeführt. Diese gemeinsame Einkaufsliste ist jetzt zusätzlich direkt über die obere Navigation der Startseite erreichbar.

## Offene Aufgaben

1. Beer Can Chicken gemeinsam testen und Garzeit sowie Gewürzmenge präzisieren.
2. Ein Rezeptbild für Beer Can Chicken ergänzen.
3. Chicken Asado gemeinsam testen und anschließend Mengen, Grillhitze und Gesamtgrillzeit präzisieren.
4. Ein Rezeptbild für Chicken Asado ergänzen.
5. Grillgemüse gemeinsam testen und später auf Version 1.0.0 setzen.
6. Honig-Senf-Lachs und Gemüsefinish-Mild gemeinsam prüfen.
7. Weitere Salate, Beilagen und vegane Rezepte ergänzen.
8. Übergangsseite `kochbuch.html` später reduzieren oder auflösen.

## Verbindliche Hinweise

- Neue Rezeptseiten zeigen keine sichtbaren Versions- oder Arbeitsstatusangaben.
- Interne Rezeptversionen bleiben als HTML-Meta-Daten erhalten.
- Der Einkaufslistenblock steht am Ende des Rezeptinhalts.
- Die Fleisch-Unterkategorie heißt `Geflügel`, nicht mehr `Hähnchen`.
- Food-Fotos werden als weboptimierte JPEG-Dateien eingebunden.
- Frühere Detailstände bleiben über die Git-Commit-Historie nachvollziehbar.

## Änderungshistorie

### Version 2.15.1 – 04.08.2026

- Einkaufsliste als fünften Link in die obere Hauptnavigation der Startseite aufgenommen
- die drei unteren Schnellzugriffe Grundlagen, Gemeinsame Einkaufsliste und Gesamtes Kochbuch entfernt
- mobile Hauptnavigation für fünf Links angepasst
- Buchversion auf 2.15.1 erhöht

### Version 2.15.0 – 04.08.2026

- Fleisch-Unterkategorie Hähnchen in Geflügel umbenannt
- Chicken Asado der Rubrik Geflügel zugeordnet und Rezeptversion auf 0.1.1 erhöht
- Beer Can Chicken als zweites Geflügelrezept ergänzt
- Beer Can Chicken mit Zutaten, acht Zubereitungsschritten und Kerntemperaturkontrolle ausgearbeitet
- Fleischübersicht mit beiden Geflügelrezepten verlinkt
- Einzel- und gemeinsame Einkaufsliste auf neun Rezepte erweitert
- Buchversion auf 2.15.0 erhöht

### Version 2.14.0 – 03.08.2026

- Chicken Asado als neues Rezept unter Fleisch → Geflügel ergänzt
- Zutaten und Marinade für zwei Personen erfasst
- Spatchcock-Vorbereitung, Marinierzeit und direktes Grillen mit Fünf-Minuten-Wenderhythmus dokumentiert
- saubere Marinadenportion für das Nachstreichen verbindlich getrennt
- Fleischübersicht mit Chicken Asado verlinkt
- Einzel- und gemeinsame Einkaufsliste auf acht Rezepte erweitert

### Version 2.13.2 – 03.08.2026

- Grillgemüse mit Süßkartoffeln, Kichererbsen, Erdnüssen und Cherrytomaten erweitert
- Aubergine und Frühlingszwiebeln entfernt
- optionale Zutaten Spargel, Parmesan, Feta, Hokkaido-Kürbis und Kartoffelecken ergänzt
- Ablauf auf zwei Planchas und indirektes Fertiggaren bei 120 °C angepasst

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
