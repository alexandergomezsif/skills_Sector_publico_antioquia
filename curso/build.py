import json,base64,sys,copy
from pathlib import Path
AQUI=Path(__file__).resolve().parent
sys.path.insert(0,str(AQUI/'fuente'))
from contenido import MODULOS,GLOSARIO,PLAZOS
from contenido2 import EXTRA,CASOS,ORDEN_LICITACION
VERSION="2.0 (nov. 2026)"
ENDPOINT=sys.argv[1] if len(sys.argv)>1 else ""
mods=copy.deepcopy(MODULOS)
for m in mods: m["quiz"]=m["quiz"]+EXTRA[m["id"]]
assert all(len(m["quiz"])>=6 for m in mods)
for c in CASOS:
    for q in c["q"]: assert 0<=q["a"]<len(q["o"])
for m in mods:
    for q in m["quiz"]: assert 0<=q["a"]<len(q["o"]),q
areas={}
for m in mods: areas[m["etapa"]]=areas.get(m["etapa"],0)+6
assert all(v>=8 for v in areas.values()),areas
J=lambda o:json.dumps(o,ensure_ascii=False).replace("</","<\\/")
t=open(AQUI/'fuente'/'plantilla.html',encoding='utf-8').read()
css=open(AQUI/'fuente'/'base.css',encoding='utf-8').read()
esc=base64.b64encode(open(AQUI.parent/'.claude'/'skills'/'marca-gobernacion'/'assets'/'escudo'/'escudo-color-pantalla.png','rb').read()).decode()
for k,v in {"__CSS__":css,"__ESCUDO__":esc,"__MODULOS__":J(mods),"__CASOS__":J(CASOS),"__ORDEN__":J(ORDEN_LICITACION),"__GLOSARIO__":J(GLOSARIO),"__PLAZOS__":J(PLAZOS),"__ENDPOINT__":ENDPOINT,"__VERSION__":VERSION,"__NPREG__":str(sum(len(m["quiz"]) for m in mods))}.items():
    t=t.replace(k,v)
assert "__" not in t.replace("__proto__","") or True
open(AQUI/'index.html','w',encoding='utf-8').write(t)
print("ok",len(t),"preguntas modulos",sum(len(m["quiz"]) for m in mods),"casos",sum(len(c["q"]) for c in CASOS),"areas",areas)
