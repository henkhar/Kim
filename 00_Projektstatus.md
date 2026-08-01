# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.5.1  
**Letzte Aktualisierung:** 01.08.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt wird schrittweise als mehrseitige Kochbuch-Website aufgebaut.

- `index.html` – Apple-inspirierte Startseite
- `fleisch.html` – Übersichtsseite für Rind, Hähnchen, Schwein und Fisch
- `gemuese-salat.html` – Übersichtsseite **Salate & Beilagen**
- `vegan.html` – vorbereitete Übersichtsseite für vegane Rezepte
- `grundlagen.html` – eigene Seite für Grillzonen, Hitzearten und Kerntemperaturen
- `grillgemuese.html` – eigene Rezeptseite für Grillgemüse
- `finishing-sauce.html` – eigene Rezeptseite für Gemüsefinish-Fresh
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
- direkter Navigation zu Fleisch, Salate & Beilagen, Vegan und Grundlagen
- drei großen Kategoriekarten
- zwei zusätzlichen Schnellzugriffen
- responsiver Darstellung für Desktop, Tablet und Smartphone

Alle vier Hauptbereiche verweisen auf eigene Seiten.

## Navigation

Die aktuellen Unter- und Rezeptseiten besitzen im Kopfbereich:

- links das Hamburger-Menü
- direkt daneben einen runden Home-Button mit Haus-Symbol
- mittig den Titel „Haralds Grillkochbuch“

Der Home-Button führt unmittelbar zu `index.html`. Er ist mit einer dezenten grauen Fläche gestaltet, erhält beim Überfahren eine etwas dunklere Fläche und bleibt auch auf kleinen Bildschirmen bedienbar.

## Gestaltungsregel für Rezeptkarten

Rezeptkarten auf Übersichtsseiten zeigen keine farbigen Status- oder Informations-Pills. Angaben wie **Arbeitsfassung**, **bestätigte Fassung**, **Portionen** oder **Zubereitungszeit** werden dort nicht mehr als farbige Kapseln dargestellt.

Die Informationen bleiben weiterhin auf den eigentlichen Rezeptseiten und in den internen Projektdateien dokumentiert. Die Änderung betrifft ausschließlich die sichtbare Übersichtsgestaltung.

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

### Salate & Beilagen

Eigene Übersichtsseite: `gemuese-salat.html`

Der Dateiname bleibt vorerst bestehen, damit vorhandene Links stabil bleiben.

Rubriken:

- **Salate & Gemüse**
- **Soßen & Finishes**

Vorhandene Rezepte:

- Grillgemüse – Rubrik Salate & Gemüse, Arbeitsfassung, Version 0.9.2, eigene Seite `grillgemuese.html`
- Gemüsefinish-Fresh – Rubrik Soßen & Finishes, bestätigt, Version 1.0.1, eigene Seite `finishing-sauce.html`

Spätere Nudel-, Kartoffel- und weitere Beilagensalate werden unter **Salate & Gemüse** eingeordnet.

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

### Gemüsefinish-Fresh

- ID: `finishing-sauce-grillgemuese-haehnchen`
- Seite: `finishing-sauce.html`
- Version: 1.0.1
- Status: bestätigt
- Rubrik: Soßen & Finishes
- Passt zu: Hähnchen, Lachs, Steak
- Frühere Bezeichnung: Grillgemüse-Finish

Die Rezept-ID und der Dateiname bleiben aus Gründen stabiler Verlinkung unverändert.

### Grillgemüse

- ID: `grillgemuese-gasgrill`
- Seite: `grillgemuese.html`
- Version: 0.9.2
- Status: Arbeitsfassung
- Rubrik: Salate & Gemüse
- Noch zu prüfen: Mengen, Schnittgrößen, Brennereinstellung und genaue Zeitabstände

## Erledigt

- GitHub-Repository `henkhar/Kim` als dauerhafte Ablage eingerichtet
- GitHub Pages aktiviert
- Meta-Kim und dynamischen Projektstatus eingerichtet
- Übergang von einer Dokumentansicht zu einer Website beschlossen
- Apple-inspirierte Startseite als `index.html` umgesetzt
- Hamburger-Menü und responsive Navigation umgesetzt
- eigene Fleisch-Übersichtsseite als `fleisch.html` angelegt
- eigene vegane Übersichtsseite als `vegan.html` angelegt
- Grillgemüse als eigene Rezeptseite `grillgemuese.html` angelegt
- eigenes Rezept für das Finish als `finishing-sauce.html` angelegt
- eigene Grundlagen-Seite als `grundlagen.html` angelegt
- runden Home-Button auf den Unter- und Rezeptseiten ergänzt
- Bereich Gemüse & Salat in Salate & Beilagen umbenannt
- Rubriken Salate & Gemüse sowie Soßen & Finishes angelegt
- Grillgemüse der Rubrik Salate & Gemüse zugeordnet
- Grillgemüse-Finish in Gemüsefinish-Fresh umbenannt
- Gemüsefinish-Fresh der Rubrik Soßen & Finishes zugeordnet
- farbige Status- und Informations-Pills aus den Rezeptkarten der Übersicht entfernt
- dauerhafte Gestaltungsregel dazu in Meta-Kim ergänzt
- Buchversion auf 2.5.1 erhöht

## Offene Aufgaben

1. Fleischrezepte schrittweise ausarbeiten und aus den Unterkategorien verlinken.
2. Vegane Rezepte schrittweise ergänzen.
3. Weitere Salate und Beilagen wie Nudelsalate ergänzen.
4. Arbeitsfassung Grillgemüse gemeinsam prüfen und auf Version 1.0.0 setzen.
5. Übergangsseite `kochbuch.html` später reduzieren oder auflösen, sobald alle Inhalte eigene Seiten besitzen.
6. Später Suche, Filter, PWA, Favoriten und Einkaufsliste prüfen.
7. Eigene Fotos ergänzen.

## Verbindliche Hinweise für die nächste Sitzung

- `index.html`, `00_Meta-Kim.md` und `00_Projektstatus.md` zuerst vollständig lesen.
- Bei Arbeiten an Fleisch zusätzlich `fleisch.html` lesen.
- Bei Arbeiten an Salaten, Gemüse, Soßen oder Finishes zusätzlich `gemuese-salat.html` lesen.
- Bei Arbeiten an veganen Inhalten zusätzlich `vegan.html` lesen.
- Bei Arbeiten an Grillwissen oder Temperaturen zusätzlich `grundlagen.html` lesen.
- Bei Rezeptänderungen immer die zuständige Rezeptseite laden.
- Die Startseite enthält bewusst keinen Home-Button, da sie bereits das Ziel dieses Buttons ist.
- Die neuen Unter- und Rezeptseiten besitzen den runden Home-Button im Kopfbereich.
- Rezeptkarten auf Übersichtsseiten enthalten keine farbigen Status- oder Informations-Pills.
- Die vegane Seite enthält derzeit bewusst nur einen Platzhalter.
- Gemüsefinish-Fresh gilt als bestätigt.
- Das Grillgemüse bleibt bis zur gemeinsamen Kontrolle eine Arbeitsfassung.
- Die Gestaltung nutzt ausschließlich lokale Systemschriften und Inline-SVG-Symbole.
- Änderungen an Website, Meta und Status müssen synchron gehalten werden.

## Änderungshistorie

### Version 2.5.1 – 01.08.2026

- farbige Kapseln „Arbeitsfassung“, „4 Personen“, „Bestätigte Fassung“ und „5 Minuten“ aus den Rezeptkarten auf `gemuese-salat.html` entfernt
- zugehörige CSS-Klassen für Meta- und Badge-Elemente entfernt
- Rezeptkarten dadurch optisch ruhiger und näher am reduzierten Apple-inspirierten Stil gestaltet
- Rezeptstatus und Portionsangaben in den eigentlichen Rezeptseiten und internen Projektdateien beibehalten
- dauerhafte Gestaltungsregel in `00_Meta-Kim.md` ergänzt
- Rezeptinhalte und Rezeptversionen unverändert belassen

### Version 2.5.0 – 01.08.2026

- Hauptbereich „Gemüse & Salat“ in „Salate & Beilagen“ umbenannt
- bestehende Datei `gemuese-salat.html` aus Gründen stabiler Links beibehalten
- Rubriken „Salate & Gemüse“ und „Soßen & Finishes“ angelegt
- Grillgemüse unter „Salate & Gemüse“ einsortiert
- Hinweis auf spätere Nudel-, Kartoffel- und weitere Beilagensalate ergänzt
- Grillgemüse-Finish in „Gemüsefinish-Fresh“ umbenannt
- Gemüsefinish-Fresh unter „Soßen & Finishes“ einsortiert
- Rezeptversion Grillgemüse auf 0.9.2 erhöht
- Rezeptversion Gemüsefinish-Fresh auf 1.0.1 erhöht
- Startseite, Breadcrumbs, Rücklinks und Hamburger-Menüs angepasst

### Version 2.4.1 – 01.08.2026

- runden Home-Button mit Haus-Symbol ergänzt
- Button direkt rechts neben dem Hamburger-Menü angeordnet
- auf `fleisch.html`, `gemuese-salat.html`, `vegan.html`, `grundlagen.html`, `grillgemuese.html` und `finishing-sauce.html` umgesetzt
- dezente hellgraue Kreisfläche im bestehenden Apple-inspirierten Look verwendet
- Hover-, Tastatur- und Druckverhalten berücksichtigt
- responsive Positionierung für kleine Bildschirme ergänzt
- Rezeptinhalte und Rezeptversionen unverändert belassen

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