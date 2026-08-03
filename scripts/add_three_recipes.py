from pathlib import Path
import json
import re

BOOK = "2.13.0"
DATE = "2026-08-03"

def read(path):
    return Path(path).read_text(encoding="utf-8")

def write(path, text):
    Path(path).write_text(text, encoding="utf-8")

# Fleischübersicht
text = read("fleisch.html")
replacements = {
'<article class="category" id="rind"><div><h2>Rind</h2><p>Steaks, Entrecôte, Rumpsteak und Filet – mit Grillmethode, Garstufe und passender Kerntemperatur.</p></div><div class="recipe-preview"><span class="recipe-name">Entrecôte Steakhouse</span><span class="recipe-status">Rezept geplant</span></div></article>':
'<article class="category" id="rind"><div><h2>Rind</h2><p>Steaks, Entrecôte, Rumpsteak und Filet – mit Grillmethode, Garstufe und passender Kerntemperatur.</p></div><div class="recipe-preview"><a class="recipe-card-link" href="entrecote-steakhouse.html">Entrecôte Steakhouse</a></div></article>',
'<article class="category" id="haehnchen"><div><h2>Hähnchen</h2><p>Ganzes Hähnchen, Brust und Schenkel – saftig gegrillt und sicher auf den richtigen Garpunkt gebracht.</p></div><div class="recipe-preview"><span class="recipe-name">Beer Can Chicken · Chicken Asado</span><span class="recipe-status">2 Rezepte geplant</span></div></article>':
'<article class="category" id="haehnchen"><div><h2>Hähnchen</h2><p>Ganzes Hähnchen, Brust und Schenkel – saftig gegrillt und sicher auf den richtigen Garpunkt gebracht.</p></div><div class="recipe-preview"><span class="recipe-name">Beer Can Chicken · Chicken Asado</span></div></article>',
'<article class="category" id="schwein"><div><h2>Schwein</h2><p>Nackensteaks und weitere Zuschnitte mit Marinaden, kräftigen Röstaromen und kontrollierter Kerntemperatur.</p></div><div class="recipe-preview"><span class="recipe-name">Schweinenackensteak mariniert</span><span class="recipe-status">Rezept geplant</span></div></article>':
'<article class="category" id="schwein"><div><h2>Schwein</h2><p>Nackensteaks und weitere Zuschnitte mit Marinaden, kräftigen Röstaromen und kontrollierter Kerntemperatur.</p></div><div class="recipe-preview"><a class="recipe-card-link" href="schweinenackensteak-senf-kraeuter.html">Schweinenackensteak mit Senf-Kräuter-Sauce</a></div></article>',
'<a class="recipe-card-link" href="honig-senf-lachs.html">Honig-Senf-Lachs vom Grill</a><span class="recipe-status">Rezept öffnen</span>':
'<a class="recipe-card-link" href="honig-senf-lachs.html">Honig-Senf-Lachs vom Grill</a>'
}
for old, new in replacements.items():
    if old not in text:
        raise RuntimeError("Fleischübersicht: erwarteter Block fehlt")
    text = text.replace(old, new, 1)
text = text.replace('<a href="honig-senf-lachs.html">Honig-Senf-Lachs</a>', '<a href="entrecote-steakhouse.html">Entrecôte Steakhouse</a><a href="schweinenackensteak-senf-kraeuter.html">Schweinenackensteak</a><a href="honig-senf-lachs.html">Honig-Senf-Lachs</a>', 1)
write("fleisch.html", text)

# Salate & Beilagen
text = read("gemuese-salat.html")
old = '<div class="recipe-grid"><article class="recipe-card"><div><h3>Grillgemüse</h3><p>Buntes Gemüse mit kräftigen Röstaromen, gestaffelt nach Garzeit gegrillt und anschließend mit Gemüsefinish-Fresh vollendet.</p><a class="card-thumb" href="grillgemuese.html" aria-label="Grillgemüse-Rezept öffnen"><img src="assets/grillgemuese.jpg?v=280" alt="Buntes Grillgemüse mit Röstaromen" width="1199" height="675" loading="lazy" decoding="async"></a></div><a class="recipe-link" href="grillgemuese.html">Rezept öffnen →</a></article></div>\n<div class="future-note"><b>Später:</b> Hier finden auch Nudel-, Kartoffel- und andere Beilagensalate ihren Platz.</div>'
new = '<div class="recipe-grid"><article class="recipe-card"><div><h3>Grillgemüse</h3><p>Buntes Gemüse mit kräftigen Röstaromen, gestaffelt nach Garzeit gegrillt und anschließend mit Gemüsefinish-Fresh vollendet.</p><a class="card-thumb" href="grillgemuese.html" aria-label="Grillgemüse-Rezept öffnen"><img src="assets/grillgemuese.jpg?v=280" alt="Buntes Grillgemüse mit Röstaromen" width="1199" height="675" loading="lazy" decoding="async"></a></div><a class="recipe-link" href="grillgemuese.html">Rezept öffnen →</a></article><article class="recipe-card"><div><h3>Keto-Pudding</h3><p>Eine kalte Quarkspeise mit Nüssen, Sojaflocken, Chiasamen und kleinen Apfelstücken.</p></div><a class="recipe-link" href="keto-pudding.html">Rezept öffnen →</a></article></div>'
if old not in text:
    raise RuntimeError("Salateübersicht: Rezeptblock fehlt")
text = text.replace(old, new, 1)
text = text.replace('<a href="gemuese-salat.html">Salate &amp; Beilagen</a>', '<a href="gemuese-salat.html">Salate &amp; Beilagen</a><a href="keto-pudding.html">Keto-Pudding</a>', 1)
write("gemuese-salat.html", text)

# Einzel-Einkaufsliste
text = read("einkaufsliste-basis.html")
entries = """,
'schweinenackensteak-senf-kraeuter':{title:'Schweinenackensteak mit Senf-Kräuter-Sauce',baseServings:3,page:'schweinenackensteak-senf-kraeuter.html',backLabel:'Schweinenackensteak',ingredients:[{id:'schweinenacken',name:'Schweinenackensteaks (ca. 2 cm dick)',amount:500,unit:'g'},{id:'salz-lake',name:'Salz für die Salzlake',note:'nach Grundlagen'},{id:'wasser-sauce',name:'Wasser',amount:100,unit:'ml'},{id:'staerke',name:'Stärke',amount:5,unit:'g'},{id:'zwiebel',name:'Zwiebel',amount:0.5,unit:'Stück'},{id:'knoblauch',name:'Knoblauchzehe',amount:1,unit:'Stück',whole:true},{id:'ingwer',name:'Ingwer',amount:1,unit:'cm'},{id:'grober-senf',name:'Grober Senf',amount:2,unit:'EL'},{id:'mittelscharfer-senf',name:'Mittelscharfer Senf',amount:1,unit:'EL'},{id:'zucker',name:'Zucker',amount:1,unit:'EL'},{id:'indian-masala',name:'Indian Masala oder Gewürzmischung nach Wahl',amount:1,unit:'EL'},{id:'thymian',name:'Thymian',amount:1,unit:'TL'},{id:'rosmarin',name:'Rosmarin',amount:1,unit:'TL'},{id:'milder-essig',name:'Milder Essig',amount:30,unit:'ml'},{id:'oel-alternative',name:'Rapsöl oder mildes Olivenöl',amount:50,unit:'ml'},{id:'salz',name:'Salz',note:'zum Abschmecken'}]},
'keto-pudding':{title:'Keto-Pudding',baseServings:2,page:'keto-pudding.html',backLabel:'Keto-Pudding',ingredients:[{id:'magerquark',name:'Magerquark',amount:500,unit:'g'},{id:'suessstoff',name:'Süßstoff',amount:1,unit:'TL'},{id:'nuesse',name:'Nüsse',amount:2,unit:'EL'},{id:'milch',name:'Milch',amount:200,unit:'ml'},{id:'sojaflocken',name:'Sojaflocken',amount:3,unit:'EL'},{id:'chiasamen',name:'Chiasamen',amount:1,unit:'TL'},{id:'apfel',name:'Apfel',amount:1,unit:'Stück',whole:true}]},
'entrecote-steakhouse':{title:'Entrecôte Steakhouse',baseServings:1,page:'entrecote-steakhouse.html',backLabel:'Entrecôte Steakhouse',ingredients:[{id:'entrecote',name:'Entrecôte, mindestens 3 cm dick',amount:200,unit:'g'},{id:'salz',name:'Salz',note:'für Dry Brine und grobes Salz zum Finish'},{id:'pfeffer',name:'Pfeffer',note:'nach Geschmack'},{id:'butter-alternative',name:'Butter oder Kräuterbutter',note:'nach Bedarf'}]}"""
start = text.find("'gemuesefinish-mild':")
end = text.find("\n};", start)
if start < 0 or end < 0:
    raise RuntimeError("Einzel-Einkaufsliste: Rezeptobjekt nicht gefunden")
text = text[:end] + entries + text[end:]
text = text.replace('<a href="gemuesefinish-mild.html">Gemüsefinish-Mild</a>', '<a href="gemuesefinish-mild.html">Gemüsefinish-Mild</a><a href="entrecote-steakhouse.html">Entrecôte Steakhouse</a><a href="schweinenackensteak-senf-kraeuter.html">Schweinenackensteak</a><a href="keto-pudding.html">Keto-Pudding</a>', 1)
write("einkaufsliste-basis.html", text)

# Gemeinsame Einkaufsliste
text = read("einkaufsliste-gesamt-basis.html")
text = text.replace("Was möchtest du grillen?", "Was möchtest du zubereiten?", 1)
choice = '<article class="recipe-choice"><label class="choice-main"><input class="recipe-checkbox" type="checkbox" value="mild"><span class="choice-copy"><b>Gemüsefinish-Mild</b><span>Mildes Finish mit wählbarer Knoblauchvariante.</span></span></label><div class="choice-extra"><label class="field"><span>Knoblauch für Gemüsefinish-Mild</span><select id="mild-garlic"><option value="powder">Knoblauchpulver</option><option value="fresh">Frische Knoblauchzehen</option></select></label></div></article>'
addition = choice + '\n<article class="recipe-choice"><label class="choice-main"><input class="recipe-checkbox" type="checkbox" value="entrecote"><span class="choice-copy"><b>Entrecôte Steakhouse</b><span>200 g Entrecôte pro Person, Salz, Pfeffer und Butter.</span></span></label></article>\n<article class="recipe-choice"><label class="choice-main"><input class="recipe-checkbox" type="checkbox" value="nacken"><span class="choice-copy"><b>Schweinenackensteak mit Senf-Kräuter-Sauce</b><span>Nackensteaks aus Salzlake und die vollständige Sauce.</span></span></label></article>\n<article class="recipe-choice"><label class="choice-main"><input class="recipe-checkbox" type="checkbox" value="keto"><span class="choice-copy"><b>Keto-Pudding</b><span>Magerquark, Milch, Nüsse, Sojaflocken, Chiasamen und Apfel.</span></span></label></article>'
if choice not in text:
    raise RuntimeError("Gemeinsame Einkaufsliste: Auswahlblock fehlt")
text = text.replace(choice, addition, 1)
text = text.replace("const cats=['fisch','frisch','vorrat'],catNames={fisch:'Fisch',frisch:'Gemüse & Kräuter',vorrat:'Öle, Gewürze & Vorrat'};", "const cats=['fleisch','fisch','milch','frisch','vorrat'],catNames={fleisch:'Fleisch',fisch:'Fisch',milch:'Milchprodukte',frisch:'Gemüse, Obst & Kräuter',vorrat:'Öle, Gewürze & Vorrat'};", 1)
new_r = """entrecote:{title:'Entrecôte Steakhouse',base:1,items:[['entrecote','Entrecôte, mindestens 3 cm dick','fleisch','g',200],['salz','Salz','vorrat','note',0,'für Dry Brine und grobes Salz zum Finish'],['pfeffer','Schwarzer Pfeffer','vorrat','note',0,'nach Geschmack'],['butter-alternative','Butter oder Kräuterbutter','milch','note',0,'nach Bedarf']]},
nacken:{title:'Schweinenackensteak mit Senf-Kräuter-Sauce',base:3,items:[['schweinenacken','Schweinenackensteaks, ca. 2 cm dick','fleisch','g',500],['salz','Salz','vorrat','note',0,'für Salzlake und zum Abschmecken'],['wasser-sauce','Wasser','vorrat','ml',100],['staerke','Stärke','vorrat','g',5],['zwiebel','Zwiebel','frisch','count',0.5,'Stück'],['knoblauch','Knoblauch','frisch','count',1,'Zehe',1],['ingwer','Ingwer','frisch','count',1,'cm'],['senf-grob','Grober Senf','vorrat','ml',30],['senf-mittel','Mittelscharfer Senf','vorrat','ml',15],['zucker','Zucker','vorrat','ml',15],['indian-masala','Indian Masala oder Gewürzmischung nach Wahl','vorrat','ml',15],['thymian','Thymian','vorrat','ml',5],['rosmarin','Rosmarin','vorrat','ml',5],['milder-essig','Milder Essig','vorrat','ml',30],['oel-alternative','Rapsöl oder mildes Olivenöl','vorrat','ml',50]]},
keto:{title:'Keto-Pudding',base:2,items:[['magerquark','Magerquark','milch','g',500],['suessstoff','Süßstoff','vorrat','ml',5],['nuesse','Nüsse','vorrat','ml',30],['milch','Milch','milch','ml',200],['sojaflocken','Sojaflocken','vorrat','ml',45],['chiasamen','Chiasamen','vorrat','ml',5],['apfel','Apfel','frisch','count',1,'Stück',1]]}"""
script_pos = text.find("\nconst nf=")
if script_pos < 0:
    raise RuntimeError("Gemeinsame Einkaufsliste: Datenobjekt fehlt")
prefix = text[:script_pos]
close = prefix.rfind("}}")
if close < 0:
    raise RuntimeError("Gemeinsame Einkaufsliste: Objektende fehlt")
prefix = prefix[:close+1] + ",\n" + new_r + "}" + prefix[close+2:]
text = prefix + text[script_pos:]
old_aggregate = "function aggregate(ids,p){const m=new Map(),f=p/4;ids.forEach(id=>{R[id].items.forEach(a=>add(m,a,R[id].title,f));"
new_aggregate = "function aggregate(ids,p){const m=new Map();ids.forEach(id=>{const f=p/(R[id].base||4);R[id].items.forEach(a=>add(m,a,R[id].title,f));"
if old_aggregate not in text:
    raise RuntimeError("Gemeinsame Einkaufsliste: Skalierungsfunktion fehlt")
text = text.replace(old_aggregate, new_aggregate, 1)
text = text.replace("function vol(ml){ml=Math.round(ml*100)/100;if(ml>=15){", "function vol(ml){ml=Math.round(ml*100)/100;if(ml>=100)return `${nf.format(ml)} ml`;if(ml>=15){", 1)
write("einkaufsliste-gesamt-basis.html", text)

# Alle sichtbaren Seiten auf die neue unsichtbare Buchversion setzen
for path in Path('.').glob('*.html'):
    text = read(path)
    text = re.sub(r'(<meta name="book-version" content=")[^"]+(">)', rf'\g<1>{BOOK}\2', text)
    write(path, text)

# Meta-Zuordnung
text = read("00_Meta-Kim.md")
marker = "- Gemüsefinish-Mild → Soßen & Finishes\n"
if marker not in text:
    raise RuntimeError("Meta: Rezeptzuordnung fehlt")
text = text.replace(marker, marker + "- Entrecôte Steakhouse → Fleisch → Rind\n- Schweinenackensteak mit Senf-Kräuter-Sauce → Fleisch → Schwein\n- Keto-Pudding → Salate & Beilagen → Salate & Gemüse\n", 1)
write("00_Meta-Kim.md", text)

# Eingebetteter Projektzustand
text = read("index.html")
def update_json(text, script_id, updater):
    pattern = rf'(<script id="{re.escape(script_id)}" type="application/json">\n)(.*?)(\n</script>)'
    match = re.search(pattern, text, re.S)
    if not match:
        raise RuntimeError(f"Index: {script_id} fehlt")
    data = json.loads(match.group(2))
    updater(data)
    replacement = match.group(1) + json.dumps(data, ensure_ascii=False, indent=2) + match.group(3)
    return text[:match.start()] + replacement + text[match.end():]

def state_update(data):
    data['bookVersion'] = BOOK
    data['lastUpdated'] = DATE
    pages = {p.get('path') for p in data.get('pages', [])}
    additions = [
        {'path':'entrecote-steakhouse.html','role':'Eigene Rezeptseite für Entrecôte Steakhouse unter Fleisch und Rind','status':'Arbeitsfassung mit Einkaufsliste; ohne Rezeptbild'},
        {'path':'schweinenackensteak-senf-kraeuter.html','role':'Eigene Rezeptseite für Schweinenackensteak mit Senf-Kräuter-Sauce unter Fleisch und Schwein','status':'Arbeitsfassung mit Einkaufsliste; ohne Rezeptbild'},
        {'path':'keto-pudding.html','role':'Eigene Rezeptseite für Keto-Pudding unter Salate & Beilagen','status':'Arbeitsfassung mit Einkaufsliste; ohne Rezeptbild'}]
    for item in additions:
        if item['path'] not in pages:
            data.setdefault('pages', []).append(item)
    for page in data.get('pages', []):
        if page.get('path') == 'einkaufsliste.html': page['status'] = 'aktiv für alle sieben Einzelrezepte'
        if page.get('path') == 'einkaufsliste-gesamt.html': page['status'] = 'aktiv für sieben auswählbare Rezepte'
    ids = {r.get('id') for r in data.get('recipes', [])}
    recipes = [
        {'id':'entrecote-steakhouse','title':'Entrecôte Steakhouse','page':'entrecote-steakhouse.html','version':'0.1.0','status':'Arbeitsfassung'},
        {'id':'schweinenackensteak-senf-kraeuter','title':'Schweinenackensteak mit Senf-Kräuter-Sauce','page':'schweinenackensteak-senf-kraeuter.html','version':'0.1.0','status':'Arbeitsfassung'},
        {'id':'keto-pudding','title':'Keto-Pudding','page':'keto-pudding.html','version':'0.1.0','status':'Arbeitsfassung'}]
    for item in recipes:
        if item['id'] not in ids:
            data.setdefault('recipes', []).append(item)
    data['recipeCount'] = 7
    data['confirmedRecipeCount'] = 1
    data['draftRecipeCount'] = 6
    data['plannedRecipes'] = [x for x in data.get('plannedRecipes', []) if x not in {'Entrecôte Steakhouse','Schweinenackensteak mariniert'}]
    data['plannedRecipeCount'] = len(data['plannedRecipes'])
    if not any(h.get('version') == BOOK for h in data.get('history', [])):
        data.setdefault('history', []).append({'date':DATE,'version':BOOK,'change':'Entrecôte Steakhouse, Schweinenackensteak mit Senf-Kräuter-Sauce und Keto-Pudding ergänzt; Kategorieübersichten und beide Einkaufslisten auf sieben Rezepte erweitert.'})
text = update_json(text, 'chefkoch-kim-state', state_update)
write("index.html", text)

# Projektstatus
text = read("00_Projektstatus.md")
text = text.replace("**Buchversion:** 2.12.2", "**Buchversion:** 2.13.0", 1)
text = text.replace("- `honig-senf-lachs.html` – Rezeptseite für Honig-Senf-Lachs vom Grill\n", "- `honig-senf-lachs.html` – Rezeptseite für Honig-Senf-Lachs vom Grill\n- `entrecote-steakhouse.html` – Rezeptseite für Entrecôte Steakhouse\n- `schweinenackensteak-senf-kraeuter.html` – Rezeptseite für Schweinenackensteak mit Senf-Kräuter-Sauce\n", 1)
text = text.replace("- `gemuese-salat.html` – Übersichtsseite **Salate & Beilagen**\n", "- `gemuese-salat.html` – Übersichtsseite **Salate & Beilagen**\n- `keto-pudding.html` – Rezeptseite für Keto-Pudding\n", 1)
for old, new in [("- 4 ausgearbeitete Rezepte","- 7 ausgearbeitete Rezepte"),("- 3 Arbeitsfassungen","- 6 Arbeitsfassungen"),("- 4 geplante Fleischrezepte","- 2 geplante Fleischrezepte"),("- 4 eigenständige Rezeptseiten","- 7 eigenständige Rezeptseiten"),("- 1 Einzelrezept-Einkaufsliste für alle 4 Rezepte","- 1 Einzelrezept-Einkaufsliste für alle 7 Rezepte")]:
    text = text.replace(old, new, 1)
pattern = re.compile(r"Vorhandenes Fischrezept:\n\n- Honig-Senf-Lachs vom Grill.*?\n\nGeplante Rezepte:\n\n- Entrecôte Steakhouse\n- Beer Can Chicken\n- Chicken Asado\n- Schweinenackensteak mariniert", re.S)
text, count = pattern.subn("Vorhandene Fleischrezepte:\n\n- Entrecôte Steakhouse – Arbeitsfassung, Version 0.1.0, Seite `entrecote-steakhouse.html`\n- Schweinenackensteak mit Senf-Kräuter-Sauce – Arbeitsfassung, Version 0.1.0, Seite `schweinenackensteak-senf-kraeuter.html`\n- Honig-Senf-Lachs vom Grill – Arbeitsfassung, Version 0.1.9, Seite `honig-senf-lachs.html`\n\nGeplante Rezepte:\n\n- Beer Can Chicken\n- Chicken Asado", text, count=1)
if count != 1:
    raise RuntimeError("Projektstatus: Fleischabschnitt fehlt")
text = text.replace("- Gemüsefinish-Mild – Rubrik Soßen & Finishes, Arbeitsfassung, Version 0.1.5, Seite `gemuesefinish-mild.html`\n", "- Gemüsefinish-Mild – Rubrik Soßen & Finishes, Arbeitsfassung, Version 0.1.5, Seite `gemuesefinish-mild.html`\n- Keto-Pudding – Rubrik Salate & Gemüse, Arbeitsfassung, Version 0.1.0, Seite `keto-pudding.html`\n", 1)
sections = """### Entrecôte Steakhouse

- ID: `entrecote-steakhouse`
- Seite: `entrecote-steakhouse.html`
- Version: 0.1.0
- Status: Arbeitsfassung
- Rubrik: Fleisch → Rind
- Grundmenge: 200 g Entrecôte pro Person, mindestens 3 cm dick
- Methode: Dry Brine und rückwärts grillen
- Vor dem Sizzler: etwa 4 °C unter der gewünschten Ziel-Kerntemperatur

### Schweinenackensteak mit Senf-Kräuter-Sauce

- ID: `schweinenackensteak-senf-kraeuter`
- Seite: `schweinenackensteak-senf-kraeuter.html`
- Version: 0.1.0
- Status: Arbeitsfassung
- Rubrik: Fleisch → Schwein
- Menge: 3 Personen / 500 g Schweinenacken
- Vorbereitung: Salzlake nach Grundlagen
- Finish: Senf-Kräuter-Sauce erst nach dem Grillen

### Keto-Pudding

- ID: `keto-pudding`
- Seite: `keto-pudding.html`
- Version: 0.1.0
- Status: Arbeitsfassung
- Rubrik: Salate & Beilagen → Salate & Gemüse
- Menge: 2 Personen
- Basis: Magerquark, Milch, Nüsse, Sojaflocken, Chiasamen und Apfel

"""
if "### Entrecôte Steakhouse\n" not in text:
    text = text.replace("## Erledigt\n", sections + "## Erledigt\n", 1)
completed = "- Entrecôte Steakhouse als neue Rezeptseite unter Fleisch → Rind ergänzt\n- Schweinenackensteak mit Senf-Kräuter-Sauce als neue Rezeptseite unter Fleisch → Schwein ergänzt\n- Keto-Pudding als neue Rezeptseite unter Salate & Beilagen ergänzt\n- beide Einkaufslisten auf insgesamt sieben Rezepte erweitert\n- gemeinsame Mengenberechnung auf unterschiedliche Grundportionen pro Rezept umgestellt\n- Buchversion auf 2.13.0 erhöht\n"
if completed not in text:
    text = text.replace("## Erledigt\n", "## Erledigt\n\n" + completed, 1)
history = """### Version 2.13.0 – 03.08.2026

- Entrecôte Steakhouse, Schweinenackensteak mit Senf-Kräuter-Sauce und Keto-Pudding als neue Einzelrezepte ergänzt
- Rind-, Schwein- und Salate-&-Beilagen-Übersichten verlinkt
- Einzelrezept-Einkaufsliste und gemeinsame Einkaufsliste auf sieben Rezepte erweitert
- unterschiedliche Grundportionen von 1, 2, 3 und 4 Personen werden korrekt skaliert
- interne Rezeptversionen der drei neuen Rezepte auf 0.1.0 gesetzt

"""
if "### Version 2.13.0" not in text:
    text = text.replace("## Änderungshistorie\n", "## Änderungshistorie\n" + history, 1)
write("00_Projektstatus.md", text)

# Prüfungen
for path in ["entrecote-steakhouse.html","schweinenackensteak-senf-kraeuter.html","keto-pudding.html"]:
    page = read(path)
    assert page.index('class="panel shopping-panel"') < page.index('class="back-link"')
for token in ["entrecote-steakhouse","schweinenackensteak-senf-kraeuter","keto-pudding"]:
    assert token in read("einkaufsliste-basis.html")
assert "const f=p/(R[id].base||4)" in read("einkaufsliste-gesamt-basis.html")
