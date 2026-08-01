# Meta-Kim

## Zweck

Diese Datei enthält die stabilen Regeln für das Projekt **Chefkoch Kim – Haralds Grillkochbuch**. Das Projekt wird ab Version 2.0 als schrittweise wachsende Kochbuch-Website aufgebaut.

## Verbindlicher Start einer neuen Sitzung

1. Die aktuelle `index.html` aus dem Repository `henkhar/Kim` laden.
2. Danach diese Datei `00_Meta-Kim.md` vollständig lesen.
3. Anschließend `00_Projektstatus.md` vollständig lesen.
4. Bei Rezept- oder Grundlagenänderungen zusätzlich die jeweils betroffene Inhaltsseite laden.
5. Alle gelesenen Quellen während der aktiven Sitzung als verbindliche Arbeitsgrundlage verwenden.
6. Erst danach Inhalte bearbeiten.

## Verbindlicher Abschluss einer Sitzung

1. Änderungen möglichst lokal und nachvollziehbar durchführen.
2. Bestehende Rezept-IDs dauerhaft beibehalten.
3. Nicht bestätigte Inhalte als Arbeitsfassung kennzeichnen.
4. Rezeptversionen aktualisieren, sofern ein Rezept geändert wurde.
5. Navigation, Links und mobile Darstellung prüfen.
6. Buchversion nach dem Schema `MAJOR.MINOR.PATCH` aktualisieren.
7. Eingebetteten Projektstatus in `index.html` sowie `00_Projektstatus.md` synchron aktualisieren.
8. Bei einer bewussten Regeländerung auch diese Datei aktualisieren.
9. Erst danach die Sitzung als abgeschlossen melden.

## Projektarchitektur

- `index.html` ist die von GitHub Pages veröffentlichte Startseite.
- `kochbuch.html` ist derzeit die Übergangsseite für die bereits vorhandenen Grundlagen und Rezepte.
- Künftige Kategorien und Rezepte dürfen auf eigene HTML-Seiten verteilt werden.
- `00_Meta-Kim.md` enthält die stabilen Projektregeln.
- `00_Projektstatus.md` enthält den dynamischen Projektzustand und die Änderungshistorie.
- Der JSON-Bereich in `index.html` dient als maschinenlesbare Spiegelung der wichtigsten Meta- und Zustandsdaten.
- Bei Abweichungen müssen Website, Meta-Datei und Projektstatus wieder synchronisiert werden.

## Website-Grundsätze

- Die Startseite dient der Orientierung und enthält keine vollständigen Rezepte.
- Kategorien, Grundlagen und Rezepte werden schrittweise in passende Unterseiten aufgeteilt.
- Die Navigation muss jederzeit einen klaren Weg zurück zur Startseite bieten.
- Alle Seiten müssen auf Desktop, Tablet und Smartphone gut lesbar und bedienbar sein.
- Die Gestaltung bleibt reduziert, großzügig und Apple-inspiriert.
- Rezeptkarten auf Übersichtsseiten zeigen keine farbigen Status- oder Informations-Pills. Arbeitsstand, Portionen und Rezeptstatus bleiben auf den Rezeptseiten beziehungsweise in den internen Projektdateien dokumentiert.
- Rezeptbilder werden als große Bilder im Seitenverhältnis 16:9 direkt unter der Rezepteinleitung eingebunden. Sie erhalten großzügig abgerundete Ecken, eine dezente Schattenwirkung, einen aussagekräftigen Alternativtext und eine zurückhaltende Bildunterschrift.
- Das erste verbindliche Bildmuster ist die Rezeptseite `honig-senf-lachs.html`. Weitere Rezeptbilder sollen sich an diesem ruhigen, hellen und hochwertigen Food-Fotografie-Stil orientieren.
- Rezeptbilder werden als eigenständige, browserkompatible Bilddateien im Repository gespeichert. Direkte Daten-URLs im HTML sowie verschachtelte Rasterbilder in SVG-Dateien werden vermieden.
- Als Schrift werden vorrangig lokale Systemschriften verwendet; es werden keine Schriftdateien verteilt.
- HTML, CSS und JavaScript dürfen genutzt werden.
- GitHub Pages führt keinen serverseitigen PHP-Code aus. Funktionen mit Datenbank, Benutzerkonto oder zentralem Speichern benötigen später ein geeignetes Backend oder anderes Hosting.
- Noch nicht vorhandene Seiten dürfen vorübergehend auf die Übergangsseite verweisen, müssen aber später durch echte Zielseiten ersetzt werden.

## Navigation und Kategorien

Aktuelle Hauptbereiche:

1. Fleisch
2. Salate & Beilagen
3. Vegan
4. Grundlagen

Der Hauptbereich **Salate & Beilagen** verwendet derzeit weiterhin die bestehende Datei `gemuese-salat.html`, damit vorhandene Links stabil bleiben.

Rubriken innerhalb von **Salate & Beilagen**:

1. Salate & Gemüse
2. Soßen & Finishes

Zuordnung der vorhandenen Rezepte:

- Honig-Senf-Lachs vom Grill → Fleisch → Fisch
- Grillgemüse → Salate & Gemüse
- Gemüsefinish-Fresh → Soßen & Finishes
- Gemüsefinish-Mild → Soßen & Finishes

Weitere Bereiche wie Suche, Favoriten, Einkaufsliste oder Projektinfos können später ergänzt werden.

## Qualitätsregeln

- Keine Mengen, Temperaturen oder Arbeitsschritte stillschweigend erfinden.
- Unsichere Angaben ausdrücklich als Vorschlag, Schätzung oder zu testende Variante kennzeichnen.
- Eigene erprobte Erfahrungen von Harald klar als solche kennzeichnen und höher gewichten als allgemeine Empfehlungen.
- Zutaten sollen möglichst im normalen deutschen Einzelhandel erhältlich sein.
- Anleitungen müssen am Grill ohne zusätzliche Erklärung ausführbar sein.
- Direkte und indirekte Hitze sowie Ziel- und Abnahmetemperaturen klar unterscheiden.
- Lebensmittelsicherheit und Genuss-Garpunkt getrennt erklären, wenn dies relevant ist.
- Bestehende Inhalte nicht ohne dokumentierten Grund entfernen.

## Standardaufbau eines Rezepts

1. Titel und eindeutige Rezept-ID
2. Kurzbeschreibung
3. Großes Rezeptbild im bestätigten 16:9-Hero-Stil, sofern ein Bild vorhanden ist
4. Kategorie und passende Gerichte
5. Portionen sowie Vorbereitungs-, Grill- und Gesamtzeit
6. Grillmethode, Grilltemperatur und Kerntemperatur, sofern relevant
7. Zutaten mit eindeutigen Mengen
8. Chronologische, praxistaugliche Zubereitung
9. Finishing, Ruhezeit und Servierhinweise
10. Kim-Tipp mit kurzer Begründung
11. Varianten und eigene Erfahrungen
12. Rezeptversion und Änderungsverlauf

## Versionsregeln

- `MAJOR`: grundlegende Architektur- oder Konzeptänderung
- `MINOR`: neue Seite, neues Rezept, neues Kapitel oder größere Funktion
- `PATCH`: Korrektur, Text- oder Gestaltungsanpassung
- Jedes Rezept besitzt zusätzlich eine eigene Versionsnummer.

## Schreibstil

- freundlich, klar und professionell
- praxisnah statt werblich
- kurze nachvollziehbare Begründungen
- deutsche Mengen-, Temperatur- und Zeitangaben

## Änderungsgrundsatz

Bestehende Inhalte und funktionierende Seiten niemals grundlos neu aufbauen. Größere Architekturänderungen erfolgen nur nach ausdrücklicher gemeinsamer Entscheidung. Die Umstellung auf die Website-Architektur wurde am 26.07.2026 gemeinsam beschlossen.