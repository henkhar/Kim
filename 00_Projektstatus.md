# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.1.0  
**Letzte Aktualisierung:** 26.07.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt wird schrittweise als mehrseitige Kochbuch-Website aufgebaut.

- `index.html` – Apple-inspirierte Startseite
- `fleisch.html` – Übersichtsseite für Rind, Hähnchen, Schwein und Fisch
- `kochbuch.html` – Übergangsseite mit den bisher vorhandenen Grundlagen und Rezepten
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
- 1 Fleisch-Übersichtsseite
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

Der Eintrag **Fleisch** verweist jetzt auf `fleisch.html`.

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

Die Seite verwendet dieselbe Apple-inspirierte Gestaltung wie die Startseite. Die vier Unterkategorien werden als große Karten dargestellt. Noch nicht ausgearbeitete Rezepte sind als geplant gekennzeichnet.

### Gemüse & Salat

Vorhanden:

- Grillgemüse – Arbeitsfassung, Version 0.9.1
- Finishing-Sauce für Grillgemüse – bestätigt, Version 1.0.0

Der Bereich verweist derzeit direkt auf das Grillgemüse in `kochbuch.html`.

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
- Version: 1.0.0
- Status: bestätigt
- Passt zu: Hähnchen, Lachs, Steak

### Grillgemüse

- ID: `grillgemuese-gasgrill`
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
- Buchversion auf 2.0.0 erhöht
- eigene Fleisch-Übersichtsseite als `fleisch.html` angelegt
- Startseite und Menü mit der Fleisch-Seite verknüpft
- Unterkategorien Rind, Hähnchen, Schwein und Fisch als Karten umgesetzt
- Buchversion auf 2.1.0 erhöht

## Offene Aufgaben

1. Gemüse & Salat als eigene Übersichtsseite aufbauen.
2. Vegan als eigene Übersichtsseite aufbauen.
3. Grundlagen aus `kochbuch.html` in eine eigene Seite überführen.
4. Fleischrezepte schrittweise ausarbeiten und aus den Unterkategorien verlinken.
5. Grillgemüse in eine eigene Rezeptseite überführen.
6. Finishing-Sauce in eine eigene Rezeptseite überführen.
7. Arbeitsfassung Grillgemüse gemeinsam prüfen und auf Version 1.0.0 setzen.
8. Später Suche, Filter, PWA, Favoriten und Einkaufsliste prüfen.
9. Eigene Fotos ergänzen.

## Verbindliche Hinweise für die nächste Sitzung

- `index.html`, `00_Meta-Kim.md` und `00_Projektstatus.md` zuerst vollständig lesen.
- Bei Arbeiten an Fleisch zusätzlich `fleisch.html` lesen.
- Bei Rezeptänderungen zusätzlich `kochbuch.html` oder die später zuständige Rezeptseite lesen.
- Die Startseite enthält bewusst keine vollständigen Rezepte.
- Die Fleisch-Seite ist eine Übersichtsseite; die einzelnen Rezepte sind noch geplant.
- Die Finishing-Sauce gilt als bestätigt.
- Das Grillgemüse bleibt bis zur gemeinsamen Kontrolle eine Arbeitsfassung.
- Die Gestaltung nutzt ausschließlich lokale Systemschriften.
- Änderungen an Website, Meta und Status müssen synchron gehalten werden.

## Änderungshistorie

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