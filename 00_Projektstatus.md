# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.2.0  
**Letzte Aktualisierung:** 27.07.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt wird schrittweise als mehrseitige Kochbuch-Website aufgebaut.

- `index.html` – Apple-inspirierte Startseite
- `fleisch.html` – Übersichtsseite für Rind, Hähnchen, Schwein und Fisch
- `gemuese-salat.html` – Übersichtsseite für Gemüse, Salate und Finishes
- `grillgemuese.html` – eigene Rezeptseite für Grillgemüse
- `finishing-sauce.html` – eigene Rezeptseite für das Grillgemüse-Finish
- `kochbuch.html` – Übergangsseite für Grundlagen und frühere Gesamtansicht
- `00_Meta-Kim.md` – stabile Regeln und Architektur
- `00_Projektstatus.md` – dynamischer Zustand und Änderungshistorie
- GitHub Pages – Veröffentlichung der Website

## Aktueller Bestand

- 2 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 1 Arbeitsfassung
- 5 geplante Fleisch- und Fischrezepte
- 1 Grundlagenbereich
- 1 Startseite
- 2 Kategorie-Übersichtsseiten
- 2 eigenständige Rezeptseiten
- 1 Übergangsseite für vorhandene Inhalte

## Startseite

Die Startseite verwendet eine reduzierte, Apple-inspirierte Gestaltung mit:

- sehr großer Hauptüberschrift
- lokaler Apple-/Systemtypografie
- Hamburger-Menü
- direkter Navigation zu Fleisch, Gemüse & Salat, Vegan und Grundlagen
- drei großen Kategoriekarten
- zwei zusätzlichen Schnellzugriffen
- responsiver Darstellung für Desktop, Tablet und Smartphone

Die Einträge **Fleisch** und **Gemüse & Salat** verweisen auf eigene Übersichtsseiten.

## Kategorien

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

Zusätzlich ist auf der Übersichtsseite der spätere Bereich **Salate** als geplant markiert.

### Vegan

- derzeit noch ohne Rezept
- eigene Übersichtsseite noch nicht angelegt

### Grundlagen

Vorhanden:

- direkte Hitze
- indirekte Hitze
- Zwei-Zonen-Aufbau
- Deckelregel
- Kerntemperatur- und Garpunkttabelle für Rind, Hähnchen, Pute, Lachs und Schweinenacken

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
- Grundlagen und Kerntemperaturübersicht ergänzt
- Grillgemüse und Finishing-Sauce aufgenommen
- Übergang von einer Dokumentansicht zu einer Website beschlossen
- Apple-inspirierte Startseite als `index.html` umgesetzt
- Hamburger-Menü und responsive Navigation umgesetzt
- vorhandene Inhalte in `kochbuch.html` gesichert und neu gestaltet
- Meta-Kim auf die mehrseitige Website-Architektur umgestellt
- eigene Fleisch-Übersichtsseite als `fleisch.html` angelegt
- Unterkategorien Rind, Hähnchen, Schwein und Fisch als Karten umgesetzt
- eigene Gemüse-&-Salat-Übersichtsseite als `gemuese-salat.html` angelegt
- Startseite und Menüs mit der Gemüse-&-Salat-Seite verknüpft
- Grillgemüse als eigene Rezeptseite `grillgemuese.html` angelegt
- Finishing-Sauce als eigene Rezeptseite `finishing-sauce.html` angelegt
- beide Rezeptseiten im Apple-inspirierten Stil responsiv umgesetzt
- Buchversion auf 2.2.0 erhöht

## Offene Aufgaben

1. Vegan als eigene Übersichtsseite aufbauen.
2. Grundlagen aus `kochbuch.html` in eine eigene Seite überführen.
3. Fleischrezepte schrittweise ausarbeiten und aus den Unterkategorien verlinken.
4. Arbeitsfassung Grillgemüse gemeinsam prüfen und auf Version 1.0.0 setzen.
5. Übergangsseite `kochbuch.html` später reduzieren oder auflösen, sobald alle Inhalte eigene Seiten besitzen.
6. Später Suche, Filter, PWA, Favoriten und Einkaufsliste prüfen.
7. Eigene Fotos ergänzen.

## Verbindliche Hinweise für die nächste Sitzung

- `index.html`, `00_Meta-Kim.md` und `00_Projektstatus.md` zuerst vollständig lesen.
- Bei Arbeiten an Fleisch zusätzlich `fleisch.html` lesen.
- Bei Arbeiten an Gemüse oder Salat zusätzlich `gemuese-salat.html` lesen.
- Bei Rezeptänderungen immer die zuständige Rezeptseite laden.
- Die Startseite enthält bewusst keine vollständigen Rezepte.
- Die Finishing-Sauce gilt als bestätigt.
- Das Grillgemüse bleibt bis zur gemeinsamen Kontrolle eine Arbeitsfassung.
- Die Gestaltung nutzt ausschließlich lokale Systemschriften.
- Änderungen an Website, Meta und Status müssen synchron gehalten werden.

## Änderungshistorie

### Version 2.2.0 – 27.07.2026

- neue Datei `gemuese-salat.html` angelegt
- Apple-inspirierten Stil der Startseite übernommen
- große Überschrift „Gemüse & Salat“ ergänzt
- Bereiche Grillgemüse, Finishes und Salate aufgenommen
- Grillgemüse als eigene Rezeptseite `grillgemuese.html` angelegt
- Finishing-Sauce als eigene Rezeptseite `finishing-sauce.html` angelegt
- Rezeptinhalte vollständig aus der bisherigen Gesamtseite übernommen
- Querverlinkung zwischen Grillgemüse und Finishing-Sauce ergänzt
- Startseite und Hamburger-Menüs auf die neue Übersichtsseite umgestellt
- responsive Darstellung für Desktop, Tablet und Smartphone umgesetzt

### Version 2.1.0 – 26.07.2026

- neue Datei `fleisch.html` angelegt
- Apple-inspirierten Stil der Startseite übernommen
- große Überschrift „Fleisch“ ergänzt
- direkte Navigation zu Rind, Hähnchen, Schwein und Fisch ergänzt
- vier große Unterkategorie-Karten umgesetzt
- geplante Rezepte den passenden Unterkategorien zugeordnet
- Fleisch-Links auf der Startseite und im Hamburger-Menü auf die neue Seite umgestellt
- responsive Darstellung für Desktop, Tablet und Smartphone umgesetzt

### Version 2.0.0 – 26.07.2026

- grundlegende Architekturänderung vom Single-Document-Kochbuch zur mehrseitigen Website
- `index.html` vollständig als Apple-inspirierte Startseite neu aufgebaut
- sehr große typografische Hauptüberschrift und reduzierte Navigation eingeführt
- Kategoriekarten für Fleisch, Gemüse & Salat und Vegan ergänzt
- Schnellzugriffe zu Grundlagen und gesamtem Kochbuch ergänzt
- funktionierendes Hamburger-Menü eingebaut
- responsive Darstellung für Desktop, Tablet und Smartphone umgesetzt
- bisherige Inhalte in der neuen Datei `kochbuch.html` erhalten
- `00_Meta-Kim.md` an die Website-Architektur angepasst
- serverseitige Funktionen und GitHub-Pages-Grenzen in Meta-Kim dokumentiert

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