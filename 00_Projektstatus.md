# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.6.0  
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
- `gemuesefinish-mild.html` – eigene Rezeptseite für Gemüsefinish-Mild
- `kochbuch.html` – Übergangsseite für die frühere Gesamtansicht
- `00_Meta-Kim.md` – stabile Regeln und Architektur
- `00_Projektstatus.md` – dynamischer Zustand und Änderungshistorie
- GitHub Pages – Veröffentlichung der Website

## Aktueller Bestand

- 3 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 2 Arbeitsfassungen
- 5 geplante Fleisch- und Fischrezepte
- noch keine veganen Rezepte
- 1 vollständige Grundlagen-Seite
- 1 Startseite
- 3 Kategorie-Übersichtsseiten
- 3 eigenständige Rezeptseiten
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

Der Home-Button führt unmittelbar zu `index.html`.

## Gestaltungsregel für Rezeptkarten

Rezeptkarten auf Übersichtsseiten zeigen keine farbigen Status- oder Informations-Pills. Arbeitsstand, Portionen und Rezeptstatus bleiben auf den Rezeptseiten beziehungsweise in den internen Projektdateien dokumentiert.

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

- Grillgemüse – Rubrik Salate & Gemüse, Arbeitsfassung, Version 0.9.2, Seite `grillgemuese.html`
- Gemüsefinish-Fresh – Rubrik Soßen & Finishes, bestätigt, Version 1.0.2, Seite `finishing-sauce.html`
- Gemüsefinish-Mild – Rubrik Soßen & Finishes, Arbeitsfassung, Version 0.1.0, Seite `gemuesefinish-mild.html`

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

## Rezepte

### Gemüsefinish-Fresh

- ID: `finishing-sauce-grillgemuese-haehnchen`
- Seite: `finishing-sauce.html`
- Version: 1.0.2
- Status: bestätigt
- Rubrik: Soßen & Finishes
- Passt zu: Hähnchen, Lachs, Steak
- Frühere Bezeichnung: Grillgemüse-Finish

Aktueller Zutatenstand:

- 2 EL mildes Olivenöl
- 1 EL frischer Zitronensaft
- 1 TL Honig
- 2 kleine Zehen Knoblauch, frisch gepresst
- 1–2 EL Petersilie, fein gehackt
- ½ TL Salz
- schwarzer Pfeffer, frisch gemahlen
- optional je ¼ TL fein abgeriebene Zitronenschale sowie fein gehackter Thymian oder Rosmarin

### Gemüsefinish-Mild

- ID: `gemuesefinish-mild`
- Seite: `gemuesefinish-mild.html`
- Version: 0.1.0
- Status: Arbeitsfassung
- Rubrik: Soßen & Finishes

Aktueller Zutatenstand:

- 2 EL mildes Olivenöl
- 1 TL Salz
- Pfeffer nach Geschmack
- 1 TL Knoblauchpulver oder 2 kleine Knoblauchzehen
- 1 TL Zitronensaft
- optional wenig Thymian oder Rosmarin, sehr sparsam

Die Zubereitung ist als erste Arbeitsfassung dokumentiert: Zutaten verrühren, eine der beiden Knoblauchvarianten verwenden, Kräuter sparsam dosieren und das Finish erst nach dem Grillen über das heiße Gemüse geben.

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
- eigene Fleisch-, Vegan-, Grundlagen- und Salate-&-Beilagen-Seiten angelegt
- Grillgemüse als eigene Rezeptseite angelegt
- Gemüsefinish-Fresh als eigene Rezeptseite angelegt
- Gemüsefinish-Mild als zweite Finish-Rezeptseite angelegt
- Gemüsefinish-Mild unter Soßen & Finishes verlinkt
- Buchversion auf 2.6.0 erhöht

## Offene Aufgaben

1. Fleischrezepte schrittweise ausarbeiten und aus den Unterkategorien verlinken.
2. Vegane Rezepte schrittweise ergänzen.
3. Weitere Salate und Beilagen wie Nudelsalate ergänzen.
4. Gemüsefinish-Mild gemeinsam testen und bestätigen.
5. Arbeitsfassung Grillgemüse gemeinsam prüfen und auf Version 1.0.0 setzen.
6. Übergangsseite `kochbuch.html` später reduzieren oder auflösen.
7. Später Suche, Filter, PWA, Favoriten und Einkaufsliste prüfen.
8. Eigene Fotos ergänzen.

## Verbindliche Hinweise für die nächste Sitzung

- `index.html`, `00_Meta-Kim.md` und `00_Projektstatus.md` zuerst vollständig lesen.
- Bei Arbeiten an Fleisch zusätzlich `fleisch.html` lesen.
- Bei Arbeiten an Salaten, Gemüse, Soßen oder Finishes zusätzlich `gemuese-salat.html` lesen.
- Bei Arbeiten an Gemüsefinish-Fresh zusätzlich `finishing-sauce.html` lesen.
- Bei Arbeiten an Gemüsefinish-Mild zusätzlich `gemuesefinish-mild.html` lesen.
- Bei Arbeiten an veganen Inhalten zusätzlich `vegan.html` lesen.
- Bei Arbeiten an Grillwissen oder Temperaturen zusätzlich `grundlagen.html` lesen.
- Bei Rezeptänderungen immer die zuständige Rezeptseite laden.
- Rezeptkarten auf Übersichtsseiten enthalten keine farbigen Status- oder Informations-Pills.
- Gemüsefinish-Fresh gilt als bestätigt.
- Gemüsefinish-Mild und Grillgemüse bleiben bis zur gemeinsamen Kontrolle Arbeitsfassungen.
- Änderungen an Website, Meta und Status müssen synchron gehalten werden.

## Änderungshistorie

### Version 2.6.0 – 01.08.2026

- neue Datei `gemuesefinish-mild.html` angelegt
- neues Rezept „Gemüsefinish-Mild“ als Arbeitsfassung Version 0.1.0 aufgenommen
- Zutaten übernommen: 2 EL mildes Olivenöl, 1 TL Salz, Pfeffer, 1 TL Knoblauchpulver oder 2 kleine Knoblauchzehen und 1 TL Zitronensaft
- optional wenig Thymian oder Rosmarin ergänzt
- erste Zubereitungsfassung dokumentiert
- Rezeptkarte unter „Soßen & Finishes“ ergänzt
- gegenseitige Navigation zwischen Gemüsefinish-Fresh und Gemüsefinish-Mild ergänzt
- Rezeptanzahl auf 3 erhöht
- Buchversion auf 2.6.0 erhöht

### Version 2.5.2 – 01.08.2026

- Gemüsefinish-Fresh auf Rezeptversion 1.0.2 erhöht
- mildes Olivenöl von 4 EL auf 2 EL reduziert
- Knoblauch auf 2 kleine, frisch gepresste Zehen geändert
- optionale Zitronenschale sowie Thymian oder Rosmarin auf jeweils ¼ TL reduziert

### Version 2.5.1 – 01.08.2026

- farbige Status- und Informations-Pills aus den Rezeptkarten auf `gemuese-salat.html` entfernt
- dauerhafte Gestaltungsregel in `00_Meta-Kim.md` ergänzt

### Version 2.5.0 – 01.08.2026

- Hauptbereich „Gemüse & Salat“ in „Salate & Beilagen“ umbenannt
- Rubriken „Salate & Gemüse“ und „Soßen & Finishes“ angelegt
- Grillgemüse unter „Salate & Gemüse“ einsortiert
- Grillgemüse-Finish in „Gemüsefinish-Fresh“ umbenannt

### Version 2.4.1 – 01.08.2026

- runden Home-Button mit Haus-Symbol auf den Unter- und Rezeptseiten ergänzt

### Version 2.4.0 – 31.07.2026

- neue Datei `grundlagen.html` mit Grillzonen und Kerntemperaturtabelle angelegt

### Version 2.3.0 – 31.07.2026

- neue Datei `vegan.html` als Platzhalter angelegt

### Version 2.2.0 – 27.07.2026

- Übersichtsseite für Gemüse & Salat sowie getrennte Rezeptseiten für Grillgemüse und Finish ergänzt

### Version 2.1.0 – 26.07.2026

- neue Fleisch-Übersichtsseite angelegt

### Version 2.0.0 – 26.07.2026

- Kochbuch auf eine mehrseitige Website-Architektur umgestellt