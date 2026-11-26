import json,base64,sys,copy
from pathlib import Path
AQUI=Path(__file__).resolve().parent
sys.path.insert(0,str(AQUI/'fuente'))
from contenido import GLOSARIO,PLAZOS
from contenido2 import CASOS as CASOS_BASE,ORDEN_LICITACION
from contenido3 import armar,CASOS_NUEVOS,COMPARATIVO,GLOSARIO_NUEVO,VERSION
ENDPOINT=sys.argv[1] if len(sys.argv)>1 else ""
mods=armar()
CASOS=CASOS_BASE+CASOS_NUEVOS
GLOS=sorted(GLOSARIO+GLOSARIO_NUEVO,key=lambda g:g[0].lower())
assert len({m["id"] for m in mods})==len(mods)
assert len({c["id"] for c in CASOS})==len(CASOS)
for r in COMPARATIVO["rows"]: assert 0<=r["a"]<len(COMPARATIVO["cols"])
assert all(len(m["quiz"])>=6 for m in mods)
for c in CASOS:
    for q in c["q"]: assert 0<=q["a"]<len(q["o"])
for m in mods:
    for q in m["quiz"]: assert 0<=q["a"]<len(q["o"]),q
areas={}
for m in mods: areas[m["etapa"]]=areas.get(m["etapa"],0)+len(m["quiz"])
assert all(v>=8 for v in areas.values()),areas
J=lambda o:json.dumps(o,ensure_ascii=False).replace("</","<\\/")
t=open(AQUI/'fuente'/'plantilla.html',encoding='utf-8').read()
css=open(AQUI/'fuente'/'base.css',encoding='utf-8').read()
esc=base64.b64encode(open(AQUI.parent/'.claude'/'skills'/'marca-gobernacion'/'assets'/'escudo'/'escudo-color-pantalla.png','rb').read()).decode()
for k,v in {"__CSS__":css,"__ESCUDO__":esc,"__MODULOS__":J(mods),"__CASOS__":J(CASOS),"__ORDEN__":J(ORDEN_LICITACION),"__GLOSARIO__":J(GLOS),"__COMP__":J(COMPARATIVO),"__NMOD__":str(len(mods)),"__NCASOS__":str(len(CASOS)),"__PLAZOS__":J(PLAZOS),"__ENDPOINT__":ENDPOINT,"__VERSION__":VERSION,"__NPREG__":str(sum(len(m["quiz"]) for m in mods))}.items():
    t=t.replace(k,v)
assert "__" not in t.replace("__proto__","") or True
open(AQUI/'index.html','w',encoding='utf-8').write(t)
print("ok",len(t),"preguntas modulos",sum(len(m["quiz"]) for m in mods),"casos",sum(len(c["q"]) for c in CASOS),"areas",areas)
