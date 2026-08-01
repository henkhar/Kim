# Projektstatus – Chefkoch Kim

**Status:** aktiv  
**Buchversion:** 2.7.2  
**Letzte Aktualisierung:** 01.08.2026  
**Einstiegsseite:** `index.html`

## Aktuelle Architektur

Das Projekt wird schrittweise als mehrseitige Kochbuch-Website aufgebaut.

- `index.html` – Apple-inspirierte Startseite
- `fleisch.html` – Übersichtsseite für Rind, Hähnchen, Schwein und Fisch
- `honig-senf-lachs.html` – Rezeptseite für Honig-Senf-Lachs vom Grill mit direkt eingebettetem Rezeptbild
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

- 4 ausgearbeitete Rezepte
- 1 bestätigtes Rezept
- 3 Arbeitsfassungen
- 4 geplante Fleischrezepte
- noch keine veganen Rezepte
- 1 vollständige Grundlagen-Seite
- 1 Startseite
- 3 Kategorie-Übersichtsseiten
- 4 eigenständige Rezeptseiten
- 1 Rezeptseite mit eingebautem Hero-Bild
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

Die Seite `honig-senf-lachs.html` ist die erste verbindliche Vorlage für dieses Bildlayout. Das Bild ist nun direkt als komprimiertes JPEG in die HTML-Seite eingebettet. Dadurch ist keine separate Bilddatei erforderlich und die Darstellung funktioniert zuverlässig über GitHub Pages.

## Kategorien und Hauptbereiche

### Fleisch

Eigene Übersichtsseite: `fleisch.html`

Unterkategorien:

- Rind
- Hähnchen
- Schwein
- Fisch

Vorhandenes Fischrezept:

- Honig-Senf-Lachs vom Grill – Arbeitsfassung, Version 0.1.2, Seite `honig-senf-lachs.html`

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

- Grillgemüse – Rubrik Salate & Gemüse, Arbeitsfassung, Version 0.9.2, Seite `grillgemuese.html`
- Gemüsefinish-Fresh – Rubrik Soßen & Finishes, bestätigt, Version 1.0.2, Seite `finishing-sauce.html`
- Gemüsefinish-Mild – Rubrik Soßen & Finishes, Arbeitsfassung, Version 0.1.1, Seite `gemuesefinish-mild.html`

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

### Honig-Senf-Lachs vom Grill

- ID: `honig-senf-lachs-grill`
- Seite: `honig-senf-lachs.html`
- Bild: direkt als komprimiertes JPEG in der HTML-Seite eingebettet
- Version: 0.1.2
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

Das Bild zeigt einen glasierten Lachs mit Dill und Grillgemüse. Es ist direkt unter der Einleitung eingebaut und dient als Vorlage für weitere Rezeptbilder.

### Gemüsefinish-Fresh

- ID: `finishing-sauce-grillgemuese-haehnchen`
- Seite: `finishing-sauce.html`
- Version: 1.0.2
- Status: bestätigt
- Rubrik: Soßen & Finishes

### Gemüsefinish-Mild

- ID: `gemuesefinish-mild`
- Seite: `gemuesefinish-mild.html`
- Version: 0.1.1
- Status: Arbeitsfassung
- Rubrik: Soßen & Finishes

Die Zubereitung folgt derselben Abfolge wie bei Gemüsefinish-Fresh. Das Finish wird nicht mitgegrillt.

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
- Honig-Senf-Lachs vom Grill als erstes ausgearbeitetes Fischrezept angelegt
- Fischkarte auf `fleisch.html` mit dem neuen Rezept verknüpft
- passende Beilagen Grillgemüse und Gemüsefinish-Mild auf der Rezeptseite verlinkt
- erstes Rezeptbild für Honig-Senf-Lachs erstellt
- Bild als großes 16:9-Hero-Bild auf der Rezeptseite eingebaut
- fehlerhafte externe SVG-Einbindung entfernt
- Bild als komprimiertes JPEG direkt in die Rezeptseite eingebettet
- Bildlayout als Standard für weitere Rezeptseiten dokumentiert
- Rezeptversion Honig-Senf-Lachs auf 0.1.2 erhöht
- Buchversion auf 2.7.2 erhöht

## Offene Aufgaben

1. Honig-Senf-Lachs vom Grill gemeinsam testen und bestätigen.
2. Weitere Rezeptbilder im festgelegten 16:9-Hero-Stil ergänzen.
3. Weitere Fleischrezepte schrittweise ausarbeiten und verlinken.
4. Vegane Rezepte schrittweise ergänzen.
5. Weitere Salate und Beilagen wie Nudelsalate ergänzen.
6. Gemüsefinish-Mild gemeinsam testen und bestätigen.
7. Arbeitsfassung Grillgemüse gemeinsam prüfen und auf Version 1.0.0 setzen.
8. Übergangsseite `kochbuch.html` später reduzieren oder auflösen.
9. Später Suche, Filter, PWA, Favoriten und Einkaufsliste prüfen.
10. Eigene Fotos später bei Bedarf ergänzen oder bestehende Bilder ersetzen.

## Verbindliche Hinweise für die nächste Sitzung

- `index.html`, `00_Meta-Kim.md` und `00_Projektstatus.md` zuerst vollständig lesen.
- Bei Arbeiten an Fleisch zusätzlich `fleisch.html` lesen.
- Bei Arbeiten am Honig-Senf-Lachs zusätzlich `honig-senf-lachs.html` lesen.
- Bei Arbeiten an Salaten, Gemüse, Soßen oder Finishes zusätzlich `gemuese-salat.html` lesen.
- Bei Arbeiten an Gemüsefinish-Fresh zusätzlich `finishing-sauce.html` lesen.
- Bei Arbeiten an Gemüsefinish-Mild zusätzlich `gemuesefinish-mild.html` lesen.
- Bei Arbeiten an veganen Inhalten zusätzlich `vegan.html` lesen.
- Bei Arbeiten an Grillwissen oder Temperaturen zusätzlich `grundlagen.html` lesen.
- Bei Rezeptänderungen immer die zuständige Rezeptseite laden.
- Rezeptkarten auf Übersichtsseiten enthalten keine farbigen Status- oder Informations-Pills.
- Neue Rezeptbilder orientieren sich am bestätigten 16:9-Hero-Stil des Honig-Senf-Lachses.
- Rezeptbilder können zur zuverlässigen Darstellung direkt in die HTML-Seite eingebettet werden.
- Gemüsefinish-Fresh gilt als bestätigt.
- Honig-Senf-Lachs, Gemüsefinish-Mild und Grillgemüse bleiben bis zur gemeinsamen Kontrolle Arbeitsfassungen.
- Änderungen an Website, Meta und Status müssen synchron gehalten werden.

## Änderungshistorie

### Version 2.7.2 – 01.08.2026

- Bildfehler beim Honig-Senf-Lachs korrigiert
- nicht zuverlässig dargestellte externe SVG-Datei entfernt
- Bild auf 1400 × 788 Pixel optimiert und als komprimiertes JPEG direkt in `honig-senf-lachs.html` eingebettet
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