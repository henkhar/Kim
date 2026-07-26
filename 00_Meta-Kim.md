# Meta-Kim

## Zweck

Diese Datei enthält die stabilen Regeln für das Projekt **Chefkoch Kim – Haralds Grillkochbuch**. Sie beschreibt, wie am Kochbuch gearbeitet wird. Sie wird nur bewusst und selten geändert.

## Verbindlicher Start einer neuen Sitzung

1. Die aktuelle `index.html` aus dem Repository `henkhar/Kim` laden.
2. Danach diese Datei `00_Meta-Kim.md` vollständig lesen.
3. Anschließend `00_Projektstatus.md` vollständig lesen.
4. Alle drei Quellen während der aktiven Sitzung als verbindliche Arbeitsgrundlage verwenden.
5. Erst danach Inhalte bearbeiten.

## Verbindlicher Abschluss einer Sitzung

1. Änderungen möglichst lokal und minimalinvasiv in `index.html` durchführen.
2. Bestehende Rezept-IDs beibehalten.
3. Nicht bestätigte Inhalte als Arbeitsfassung kennzeichnen.
4. Rezeptversionen aktualisieren, sofern ein Rezept geändert wurde.
5. Das sichtbare Inhaltsverzeichnis prüfen und alle betroffenen Nummern sowie Links anpassen.
6. Buchversion nach dem Schema `MAJOR.MINOR.PATCH` aktualisieren.
7. `00_Projektstatus.md` inklusive Historie, geplanter Rezepte und offener Aufgaben aktualisieren.
8. Erst danach die Sitzung als abgeschlossen melden.

## Projektarchitektur

- `index.html` ist die sichtbare Masterdatei des Kochbuchs und die von GitHub Pages veröffentlichte Webseite.
- `00_Meta-Kim.md` enthält die stabilen Projektregeln.
- `00_Projektstatus.md` enthält den dynamischen Projektzustand und die Änderungshistorie.
- Die in `index.html` eingebetteten JSON-Bereiche dienen zusätzlich als maschinenlesbare Spiegelung. Bei Abweichungen müssen die Dateien wieder synchronisiert werden.

## Inhaltsverzeichnis und Nummerierung

- Das sichtbare Inhaltsverzeichnis bildet sowohl die vorhandene als auch die geplante Buchstruktur ab.
- Neue Rezepte werden unter der sachlich passenden Kategorie einsortiert.
- Bei Ergänzungen, Verschiebungen oder Löschungen werden alle betroffenen Nummern konsistent angepasst.
- Vorhandene Kapitel und Rezepte werden über stabile HTML-Anker verlinkt.
- Noch nicht ausgearbeitete Rezepte werden im Inhaltsverzeichnis als **geplant** gekennzeichnet und erhalten noch keinen toten Link.
- Die Einrückung muss die Hierarchie optisch zeigen: Hauptteil, Kategorie, Unterkategorie und einzelnes Rezept.

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
3. Kategorie und passende Gerichte
4. Portionen sowie Vorbereitungs-, Grill- und Gesamtzeit
5. Grillmethode, Grilltemperatur und Kerntemperatur, sofern relevant
6. Zutaten mit eindeutigen Mengen
7. Chronologische, praxistaugliche Zubereitung
8. Finishing, Ruhezeit und Servierhinweise
9. Kim-Tipp mit kurzer Begründung
10. Varianten und eigene Erfahrungen
11. Rezeptversion und Änderungsverlauf

## Versionsregeln

- `MAJOR`: grundlegende Struktur- oder Konzeptänderung
- `MINOR`: neues Rezept, neues Kapitel oder größere fachliche Ergänzung
- `PATCH`: Korrektur oder Präzisierung ohne neues Kapitel
- Jedes Rezept besitzt zusätzlich eine eigene Versionsnummer.

## Schreibstil

- freundlich, klar und professionell
- praxisnah statt werblich
- kurze nachvollziehbare Begründungen
- deutsche Mengen-, Temperatur- und Zeitangaben

## Änderungsgrundsatz

Bestehenden HTML-Code niemals grundlos umstrukturieren. Änderungen erfolgen möglichst lokal und minimalinvasiv. Eine grundlegende Umstrukturierung erfolgt nur nach ausdrücklicher gemeinsamer Entscheidung.
