# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.4.0  
**Letzte Aktualisierung:** 31.07.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt wird schrittweise als mehrseitige Kochbuch-Website aufgebaut.

- `index.html` – Apple-inspirierte Startseite
- `fleisch.html` – Übersichtsseite für Rind, Hähnchen, Schwein und Fisch
- `gemuese-salat.html` – Übersichtsseite für Gemüse, Salate und Finishes
- `vegan.html` – vorbereitete Übersichtsseite für vegane Rezepte
- `grundlagen.html` – eigene Seite für Grillzonen, Hitzearten und Kerntemperaturen
- `grillgemuese.html` – eigene Rezeptseite für Grillgemüse
- `finishing-sauce.html` – eigene Rezeptseite für das Grillgemüse-Finish
- `kochbuch.html` – Übergangsseite für die frühere Gesamtansicht
- `00_Meta-Kim.md` – stabile Regeln und Architektur
- `00_Projektstatus.md` – dynamischer Zustand und Änderungshistorie
- GitHub Pages – Veröffentlichung der Website

## Aktueller Bestand

- 2 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 1 Arbeitsfassung
- 5 geplante Fleisch- und Fischrezepte
- noch keine veganen Rezepte
- 1 vollständige Grundlagen-Seite
- 1 Startseite
- 3 Kategorie-Übersichtsseiten
- 2 eigenständige Rezeptseiten
- 1 Übergangsseite für die frühere Gesamtansicht

## Startseite

Die Startseite verwendet eine reduzierte, Apple-inspirierte Gestaltung mit:

- sehr großer Hauptüberschrift
- lokaler Apple-/Systemtypografie
- Hamburger-Menü
- direkter Navigation zu Fleisch, Gemüse & Salat, Vegan und Grundlagen
- drei großen Kategoriekarten
- zwei zusätzlichen Schnellzugriffen
- responsiver Darstellung für Desktop, Tablet und Smartphone

Alle vier Hauptbereiche verweisen jetzt auf eigene Seiten.

## Kategorien und Hauptbereiche

### Fleisch

Eigene Übersichtsseite: `fleisch.html`

Unterkategorien:

- Rind
- Hähnchen
- Schwein
- Fisch

Geplante Rezepte:

- Entrecôte Steakhouse
- Beer Can Chicken
- Chicken Asado
- Schweinenackensteak mariniert
- Lachsfilet

### Gemüse & Salat

Eigene Übersichtsseite: `gemuese-salat.html`

Vorhandene Rezepte:

- Grillgemüse – Arbeitsfassung, Version 0.9.1, eigene Seite `grillgemuese.html`
- Finishing-Sauce für Grillgemüse – bestätigt, Version 1.0.0, eigene Seite `finishing-sauce.html`

Zusätzlich ist der spätere Bereich **Salate** als geplant markiert.

### Vegan

Eigene Übersichtsseite: `vegan.html`

- derzeit noch ohne Rezept
- als Platzhalter im gleichen Apple-inspirierten Stil wie die anderen Kategorien angelegt
- für spätere vegane Rezepte vorbereitet

### Grundlagen

Eigene Seite: `grundlagen.html`

Vorhanden:

- direkte Hitze
- indirekte Hitze
- Zwei-Zonen-Aufbau
- Deckelregel
- Kerntemperatur- und Garpunkttabelle für Rind, Hähnchen, Pute, Lachs und Schweinenacken

Die Seite verwendet den gleichen Apple-inspirierten Stil wie die Haupt- und Kategorie-Seiten. Die Grillzonen werden als große Karten dargestellt; die Kerntemperaturen stehen in einer responsiven, horizontal scrollbar gehaltenen Tabelle.

## Rezepte

### Finishing-Sauce für Grillgemüse

- ID: `finishing-sauce-grillgemuese-haehnchen`
- Seite: `finishing-sauce.html`
- Version: 1.0.0
- Status: bestätigt
- Passt zu: Hähnchen, Lachs, Steak

### Grillgemüse

- ID: `grillgemuese-gasgrill`
- Seite: `grillgemuese.html`
- Version: 0.9.1
- Status: Arbeitsfassung
- Noch zu prüfen: Mengen, Schnittgrößen, Brennereinstellung und genaue Zeitabstände

## Erledigt

- GitHub-Repository `henkhar/Kim` als dauerhafte Ablage eingerichtet
- GitHub Pages aktiviert
- Meta-Kim und dynamischen Projektstatus eingerichtet
- Übergang von einer Dokumentansicht zu einer Website beschlossen
- Apple-inspirierte Startseite als `index.html` umgesetzt
- Hamburger-Menü und responsive Navigation umgesetzt
- eigene Fleisch-Übersichtsseite als `fleisch.html` angelegt
- eigene Gemüse-&-Salat-Übersichtsseite als `gemuese-salat.html` angelegt
- eigene vegane Übersichtsseite als `vegan.html` angelegt
- Grillgemüse als eigene Rezeptseite `grillgemuese.html` angelegt
- Finishing-Sauce als eigene Rezeptseite `finishing-sauce.html` angelegt
- eigene Grundlagen-Seite als `grundlagen.html` angelegt
- vorhandene Grundlagen aus `kochbuch.html` vollständig übernommen
- Hauptnavigation, Schnellzugriff und relevante Hamburger-Menüs auf `grundlagen.html` umgestellt
- Buchversion auf 2.4.0 erhöht

## Offene Aufgaben

1. Fleischrezepte schrittweise ausarbeiten und aus den Unterkategorien verlinken.
2. Vegane Rezepte schrittweise ergänzen.
3. Arbeitsfassung Grillgemüse gemeinsam prüfen und auf Version 1.0.0 setzen.
4. Übergangsseite `kochbuch.html` später reduzieren oder auflösen, sobald alle Inhalte eigene Seiten besitzen.
5. Später Suche, Filter, PWA, Favoriten und Einkaufsliste prüfen.
6. Eigene Fotos ergänzen.

## Verbindliche Hinweise für die nächste Sitzung

- `index.html`, `00_Meta-Kim.md` und `00_Projektstatus.md` zuerst vollständig lesen.
- Bei Arbeiten an Fleisch zusätzlich `fleisch.html` lesen.
- Bei Arbeiten an Gemüse oder Salat zusätzlich `gemuese-salat.html` lesen.
- Bei Arbeiten an veganen Inhalten zusätzlich `vegan.html` lesen.
- Bei Arbeiten an Grillwissen oder Temperaturen zusätzlich `grundlagen.html` lesen.
- Bei Rezeptänderungen immer die zuständige Rezeptseite laden.
- Die Startseite enthält bewusst keine vollständigen Rezepte.
- Die vegane Seite enthält derzeit bewusst nur einen Platzhalter.
- Die Finishing-Sauce gilt als bestätigt.
- Das Grillgemüse bleibt bis zur gemeinsamen Kontrolle eine Arbeitsfassung.
- Die Gestaltung nutzt ausschließlich lokale Systemschriften.
- Änderungen an Website, Meta und Status müssen synchron gehalten werden.

## Änderungshistorie

### Version 2.4.0 – 31.07.2026

- neue Datei `grundlagen.html` angelegt
- Apple-inspirierten Stil der bestehenden Website übernommen
- große Überschrift „Grundlagen“ ergänzt
- direkte Navigation zu Grillzonen und Kerntemperaturen ergänzt
- direkte Hitze, indirekte Hitze, Zwei-Zonen-Aufbau und Deckelregel als große Karten umgesetzt
- vollständige Kerntemperatur- und Garpunkttabelle übernommen
- Tabelle für kleine Bildschirme horizontal scrollbar gestaltet
- Grundlagen-Links auf Startseite, Kategorie-Seiten und vorhandenen Rezeptseiten auf `grundlagen.html` umgestellt
- responsive Darstellung für Desktop, Tablet und Smartphone umgesetzt

### Version 2.3.0 – 31.07.2026

- neue Datei `vegan.html` angelegt
- Apple-inspirierten Stil der bestehenden Kategorie-Seiten übernommen
- große Überschrift „Vegan“ ergänzt
- Platzhalter „Noch keine Rezepte“ aufgenommen
- Seite für spätere vegane Rezepte vorbereitet
- Vegan-Links auf Startseite und relevanten Unterseiten auf `vegan.html` umgestellt

### Version 2.2.0 – 27.07.2026

- neue Datei `gemuese-salat.html` angelegt
- Apple-inspirierten Stil der Startseite übernommen
- große Überschrift „Gemüse & Salat“ ergänzt
- Bereiche Grillgemüse, Finishes und Salate aufgenommen
- Grillgemüse als eigene Rezeptseite `grillgemuese.html` angelegt
- Finishing-Sauce als eigene Rezeptseite `finishing-sauce.html` angelegt
- Rezeptinhalte vollständig aus der bisherigen Gesamtseite übernommen
- Querverlinkung zwischen Grillgemüse und Finishing-Sauce ergänzt
- responsive Darstellung für Desktop, Tablet und Smartphone umgesetzt

### Version 2.1.0 – 26.07.2026

- neue Datei `fleisch.html` angelegt
- Apple-inspirierten Stil der Startseite übernommen
- große Überschrift „Fleisch“ ergänzt
- direkte Navigation zu Rind, Hähnchen, Schwein und Fisch ergänzt
- vier große Unterkategorie-Karten umgesetzt
- geplante Rezepte den passenden Unterkategorien zugeordnet
- responsive Darstellung für Desktop, Tablet und Smartphone umgesetzt

### Version 2.0.0 – 26.07.2026

- grundlegende Architekturänderung vom Single-Document-Kochbuch zur mehrseitigen Website
- `index.html` vollständig als Apple-inspirierte Startseite neu aufgebaut
- sehr große typografische Hauptüberschrift und reduzierte Navigation eingeführt
- Kategoriekarten für Fleisch, Gemüse & Salat und Vegan ergänzt
- Schnellzugriffe zu Grundlagen und gesamtem Kochbuch ergänzt
- funktionierendes Hamburger-Menü eingebaut
- bisherige Inhalte in der neuen Datei `kochbuch.html` erhalten
- `00_Meta-Kim.md` an die Website-Architektur angepasst

### Version 1.4.1 – 26.07.2026

- Nummern kleiner und blasser dargestellt
- Oberpunkte grau und Rezepttitel schwarz dargestellt
- Markierung „geplant“ rechtsbündig belassen
- Abstand unter „Haralds Grillkochbuch“ verkürzt
- Rezeptnamen korrigiert

### Version 1.4.0 – 26.07.2026

- Dashboard durch ein hierarchisches Inhaltsverzeichnis ersetzt
- vorhandene und geplante Rezepte aufgenommen

### Version 1.3.0 – 26.07.2026

- sichtbare Button-Navigation entfernt
- Kerntemperatur- und Garpunkttabelle ergänzt
- separate Meta- und Projektstatusdateien angelegt

### Version 1.2.0 – 26.07.2026

- Dashboard und Grundlagenkapitel ergänzt
- Arbeitsfassung Grillgemüse aufgenommen

### Version 1.1.0 – 26.07.2026

- Meta-Kim und dynamischen Projektstatus erweitert

### Version 1.0.0 – 26.07.2026

- Kochbuch im GitHub-Repository angelegt