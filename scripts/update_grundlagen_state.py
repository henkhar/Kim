from pathlib import Path
import json
import re


def update_json_script(text, script_id, updater):
    pattern = rf'(<script id="{re.escape(script_id)}" type="application/json">\n)(.*?)(\n</script>)'
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise RuntimeError(f'{script_id} nicht gefunden')
    data = json.loads(match.group(2))
    updater(data)
    replacement = match.group(1) + json.dumps(data, ensure_ascii=False, indent=2) + match.group(3)
    return text[:match.start()] + replacement + text[match.end():]

index_path = Path('index.html')
index = index_path.read_text(encoding='utf-8')

def update_state(data):
    data['bookVersion'] = '2.12.0'
    data['lastUpdated'] = '2026-08-03'
    for page in data.get('pages', []):
        if page.get('path') == 'grundlagen.html':
            page['role'] = 'Grundlagen-Seite für Kerntemperaturen, Garpunkte, Salzlake und Dry Brine'
            page['status'] = 'aktiv mit zwei Kapiteln'
    if not any(item.get('version') == '2.12.0' for item in data.get('history', [])):
        data.setdefault('history', []).append({
            'date': '2026-08-03',
            'version': '2.12.0',
            'change': 'Grundlagen-Seite neu geordnet: Kerntemperaturen und Garpunkte stehen an erster Stelle; Salzlake und Dry Brine wurden als neues Verfahrenskapitel ergänzt und die bisherigen Kapitel zu Hitzearten, Deckelregel und Zwei-Zonen-Aufbau entfernt.'
        })

index = update_json_script(index, 'chefkoch-kim-state', update_state)
index = re.sub(r'2026 · Chefkoch Kim · Version [0-9.]+', '2026 · Chefkoch Kim · Version 2.12.0', index, count=1)
index_path.write_text(index, encoding='utf-8')

status_path = Path('00_Projektstatus.md')
status = status_path.read_text(encoding='utf-8')
status = re.sub(r'\*\*Buchversion:\*\* [0-9.]+', '**Buchversion:** 2.12.0', status, count=1)
status = re.sub(r'\*\*Letzte Aktualisierung:\*\* [^\n]+', '**Letzte Aktualisierung:** 03.08.2026  ', status, count=1)
status = status.replace('- `grundlagen.html` – eigene Seite für Grillzonen, Hitzearten und Kerntemperaturen', '- `grundlagen.html` – eigene Seite für Kerntemperaturen, Garpunkte, Salzlake und Dry Brine')
replacement = '''### Grundlagen

Eigene Seite: `grundlagen.html`

Vorhanden – in dieser Reihenfolge:

1. Kerntemperaturen und Garpunkte
2. Salzlake & Dry Brine

Das Kapitel **Salzlake & Dry Brine** beschreibt bewusst ein Vorbereitungsverfahren und ist kein eigenständiges Rezept. Die früheren Kapitel zu direkter Hitze, indirekter Hitze, Deckelregel und Zwei-Zonen-Aufbau wurden entfernt.

'''
status, count = re.subn(r'### Grundlagen\n\nEigene Seite: `grundlagen\.html`\n\nVorhanden:\n\n.*?\n\n## Rezepte', replacement + '## Rezepte', status, count=1, flags=re.S)
if count != 1:
    raise RuntimeError('Grundlagen-Abschnitt im Projektstatus nicht ersetzt')
completed = '- Grundlagen-Seite auf die Kapitel Kerntemperaturen und Garpunkte sowie Salzlake & Dry Brine reduziert\n- Kapitel Salzlake & Dry Brine als Verfahren ergänzt\n- Kapitel direkte Hitze, indirekte Hitze, Deckelregel und Zwei-Zonen-Aufbau entfernt\n- Buchversion auf 2.12.0 erhöht\n'
if completed not in status:
    status = status.replace('## Offene Aufgaben\n', completed + '\n## Offene Aufgaben\n', 1)
if '### Version 2.12.0' not in status:
    history = '''### Version 2.12.0 – 03.08.2026

- Reihenfolge der Grundlagen neu festgelegt: zuerst Kerntemperaturen und Garpunkte, danach Salzlake & Dry Brine
- Salzlake und Dry Brine als kompaktes Verfahrenskapitel ergänzt
- Kapitel direkte Hitze, indirekte Hitze, Deckelregel und Zwei-Zonen-Aufbau entfernt
- Buchversion auf 2.12.0 erhöht

'''
    status = status.replace('## Änderungshistorie\n', '## Änderungshistorie\n' + history, 1)
status_path.write_text(status, encoding='utf-8')

assert '"bookVersion": "2.12.0"' in index_path.read_text(encoding='utf-8')
assert '**Buchversion:** 2.12.0' in status_path.read_text(encoding='utf-8')
