from pathlib import Path
import json
import re

def read(path): return Path(path).read_text(encoding='utf-8')
def write(path,text): Path(path).write_text(text,encoding='utf-8')

status=read('00_Projektstatus.md')
status=status.replace('- 1 Einzelrezept-Einkaufsliste für alle 7 Rezepte mit Mengenberechnung und Druckansicht','- 1 Einzelrezept-Einkaufsliste für alle 7 Rezepte mit Mengenberechnung und Senden-Funktion',1)
status=status.replace('- automatische Umrechnung ausgehend von jeweils 4 Personen','- automatische Umrechnung ausgehend von der jeweiligen Grundmenge des Rezepts (1, 2, 3 oder 4 Personen)',1)
status=status.replace('- Druckansicht blendet Bedienelemente und bereits abgehakte Zutaten aus','- die Liste lässt sich über das systemeigene Teilen-Menü senden; ohne Web Share wird sie in die Zwischenablage kopiert',1)
status=status.replace('- Zutaten lassen sich abhaken und die Liste kann gedruckt werden','- Zutaten lassen sich abhaken und die Liste lässt sich über das systemeigene Teilen-Menü senden',1)
write('00_Projektstatus.md',status)

index=read('index.html')
pattern=r'(<script id="chefkoch-kim-state" type="application/json">\n)(.*?)(\n</script>)'
m=re.search(pattern,index,re.S)
if not m: raise RuntimeError('Index-Status fehlt')
data=json.loads(m.group(2))
for page in data.get('pages',[]):
    if page.get('path')=='einkaufsliste.html':
        page['role']='Dynamische Einkaufsliste mit Mengenberechnung, Abhaken und Senden-Funktion'
    if page.get('path')=='einkaufsliste-gesamt.html':
        page['role']='Gemeinsame Einkaufsliste mit Rezeptauswahl, Mengenberechnung, Zutatenkumulierung und Senden-Funktion'
replacement=m.group(1)+json.dumps(data,ensure_ascii=False,indent=2)+m.group(3)
index=index[:m.start()]+replacement+index[m.end():]
write('index.html',index)
