# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.14.0  
**Letzte Aktualisierung:** 03.08.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt ist eine mehrseitige, statische Kochbuch-Website auf GitHub Pages.

- `index.html` – Startseite und eingebetteter maschinenlesbarer Projektstatus
- `fleisch.html` – Übersicht für Rind, Hähnchen, Schwein und Fisch
- `gemuese-salat.html` – Übersicht Salate & Beilagen
- `vegan.html` – vorbereiteter Bereich für vegane Rezepte
- `grundlagen.html` – Kerntemperaturen, Garpunkte, Salzlake und Dry Brine
- `einkaufsliste.html` – Einkaufsliste für ein Rezept
- `einkaufsliste-gesamt.html` – gemeinsame Einkaufsliste für mehrere Rezepte
- `kochbuch.html` – Übergangsseite der früheren Gesamtansicht
- `00_Meta-Kim.md` – stabile Regeln
- `00_Projektstatus.md` – dynamischer Zustand und Änderungshistorie

## Aktueller Bestand

- 8 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 7 Arbeitsfassungen
- 1 geplantes Fleischrezept: Beer Can Chicken
- 8 eigenständige Rezeptseiten
- 7 Rezeptseiten mit Hero-Bild
- beide Einkaufslisten unterstützen alle 8 Rezepte
- sichtbare Versions- und Statushinweise bleiben ausgeblendet

## Rezeptübersicht

### Fleisch

- Entrecôte Steakhouse – Version 0.1.1 – `entrecote-steakhouse.html`
- Chicken Asado – Version 0.1.0 – `chicken-asado.html`
- Schweinenackensteak mit Senf-Kräuter-Sauce – Version 0.1.1 – `schweinenackensteak-senf-kraeuter.html`
- Honig-Senf-Lachs vom Grill – Version 0.1.9 – `honig-senf-lachs.html`

### Salate & Beilagen

- Grillgemüse – Version 0.9.7 – `grillgemuese.html`
- Gemüsefinish-Fresh – Version 1.0.6 – bestätigt – `finishing-sauce.html`
- Gemüsefinish-Mild – Version 0.1.5 – `gemuesefinish-mild.html`
- Keto-Pudding – Version 0.1.1 – `keto-pudding.html`

## Chicken Asado

- ID: `chicken-asado`
- Rubrik: Fleisch → Hähnchen
- Grundmenge: 2 Personen / 1 Maishähnchen
- Marinierzeit: mindestens 6–8 Stunden im Kühlschrank
- Methode: Hähnchen als Spatchcock vorbereiten und direkt grillen
- Wenden: etwa alle 5 Minuten
- Marinade: Orange, Limette, Knoblauch, Kreuzkümmel, Oregano, Salz, geräuchertes Paprikapulver, Essig und Olivenöl
- Für das Nachstreichen wird vor dem Kontakt mit rohem Geflügel ein sauberer Teil der Marinade separat zurückbehalten.
- Kerntemperaturen werden über die vorhandene Grundlagen-Seite geprüft.
- Noch ohne Rezeptbild

## Einkaufslisten

### Einzelrezept

`einkaufsliste.html` unterstützt jetzt acht Rezepte. Für Chicken Asado werden Hähnchen und alle Marinadenzutaten ausgehend von zwei Personen skaliert.

### Gemeinsame Einkaufsliste

`einkaufsliste-gesamt.html` enthält Chicken Asado als zusätzliche Rezeptauswahl. Gleiche Zutaten werden über bestehende dauerhafte Zutaten-IDs zusammengeführt.

## Offene Aufgaben

1. Chicken Asado gemeinsam testen und anschließend Mengen, Grillhitze und Gesamtgrillzeit präzisieren.
2. Ein Rezeptbild für Chicken Asado ergänzen.
3. Grillgemüse gemeinsam testen und später auf Version 1.0.0 setzen.
4. Honig-Senf-Lachs und Gemüsefinish-Mild gemeinsam prüfen.
5. Beer Can Chicken ausarbeiten.
6. Weitere Salate, Beilagen und vegane Rezepte ergänzen.
7. Übergangsseite `kochbuch.html` später reduzieren oder auflösen.

## Verbindliche Hinweise

- Neue Rezeptseiten zeigen keine sichtbaren Versions- oder Arbeitsstatusangaben.
- Interne Rezeptversionen bleiben als HTML-Meta-Daten erhalten.
- Der Einkaufslistenblock steht am Ende des Rezeptinhalts.
- Marinaden, die rohes Geflügel berührt haben, werden nicht zum Nachstreichen verwendet.
- Food-Fotos werden als weboptimierte JPEG-Dateien eingebunden.
- Frühere Detailstände bleiben über die Git-Commit-Historie nachvollziehbar.

## Änderungshistorie

### Version 2.14.0 – 03.08.2026

- Chicken Asado als neues Rezept unter Fleisch → Hähnchen ergänzt
- Zutaten und Marinade für zwei Personen erfasst
- Spatchcock-Vorbereitung, Marinierzeit und direktes Grillen mit Fünf-Minuten-Wenderhythmus dokumentiert
- saubere Marinadenportion für das Nachstreichen verbindlich getrennt
- Fleischübersicht mit Chicken Asado verlinkt
- Einzel- und gemeinsame Einkaufsliste auf acht Rezepte erweitert
- Buchversion auf 2.14.0 erhöht

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

### Version 2.11.0 – 02.08.2026

- gemeinsame Einkaufsliste ergänzt

### Version 2.10.0 – 02.08.2026

- Einkaufsliste auf die ersten vier Rezepte erweitert

### Version 2.9.0 – 02.08.2026

- Einzelrezept-Einkaufsliste eingeführt

Ältere Einzeländerungen bleiben vollständig in der Git-Commit-Historie des Repositorys erhalten.
