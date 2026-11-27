#!/usr/bin/env python3
"""
Consulta los contratos del Departamento de Antioquia en SECOP II a través de Datos Abiertos
(datos.gov.co, conjunto "SECOP II - Contratos Electrónicos", id jbjy-vk9h, API Socrata).

Por defecto filtra la entidad por NIT 890900286 (Departamento de Antioquia; la Asamblea comparte NIT y se
excluye por nombre). SECOP II no trae la secretaría como campo: para la Secretaría de Infraestructura
Física se filtra por palabras del objeto (vía, puente, pavimentación, placa huella, interventoría...).

Requiere internet y solo la biblioteca estándar (pandas/openpyxl si exporta a .xlsx).
Opcional: variable de entorno SOCRATA_APP_TOKEN para evitar límites de velocidad.

Ejemplos:
    # Resumen por tipo y modalidad de los contratos de infraestructura firmados en 2026
    python consultar_secop.py resumen --desde 2026-01-01 --infra

    # Listado de contratos de obra con "pavimentación" desde 2025, exportado
    python consultar_secop.py buscar pavimentacion --tipo Obra --desde 2025-01-01 --salida pav.xlsx

    # Un contrato por referencia o id de SECOP
    python consultar_secop.py contrato 4600017794

Campos útiles del conjunto (verificados nov. 2026): referencia_del_contrato, id_contrato, proceso_de_compra,
estado_contrato, descripcion_del_proceso, objeto_del_contrato, tipo_de_contrato, modalidad_de_contratacion,
justificacion_modalidad_de, fecha_de_firma, fecha_de_inicio_del_contrato, fecha_de_fin_del_contrato,
proveedor_adjudicado, valor_del_contrato, valor_pagado, valor_facturado, valor_pendiente_de_pago,
dias_adicionados, origen_de_los_recursos, sistema_general_de_regal_as, recursos_propios, documentos_tipo,
urlproceso, ultima_actualizacion.

Valores reales de tipo_de_contrato: Obra, Interventoría, Consultoría, Prestación de servicios, Suministros,
Compraventa, Otro, Decreto 092 de 2017, Asociación Público Privada, Comodato, Arrendamiento de inmuebles...
Valores reales de modalidad_de_contratacion: "Licitación pública Obra Publica", "Concurso de méritos abierto",
"Selección Abreviada de Menor Cuantía", "Mínima cuantía", "Contratación directa",
"Contratación Directa (con ofertas)", "Contratación régimen especial", "Contratación régimen especial
(con ofertas)", "Selección abreviada subasta inversa", "Licitación pública".

Privacidad: el conjunto publica cédulas, cuentas bancarias y datos de representantes. Este script NO los
descarga (consulta solo las columnas de la lista CAMPOS).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

URL = "https://www.datos.gov.co/resource/jbjy-vk9h.json"
NIT_DEPTO = "890900286"
ENTIDAD_EXCLUIR = "ASAMBLEA DEPARTAMENTAL DE ANTIOQUIA"
PAGINA = 1000
TIMEOUT = 90

CAMPOS = [
    "referencia_del_contrato", "id_contrato", "proceso_de_compra", "estado_contrato", "tipo_de_contrato",
    "modalidad_de_contratacion", "fecha_de_firma", "fecha_de_inicio_del_contrato", "fecha_de_fin_del_contrato",
    "proveedor_adjudicado", "valor_del_contrato", "valor_pagado", "valor_pendiente_de_pago", "dias_adicionados",
    "origen_de_los_recursos", "documentos_tipo", "objeto_del_contrato", "urlproceso", "ultima_actualizacion",
]

PALABRAS_INFRA = [
    "VIA", "VÍA", "VIAL", "PUENTE", "PAVIMENT", "PLACA HUELLA", "CARRETERA", "CORREDOR", "MALLA VIAL",
    "INFRAESTRUCTURA FISICA", "INFRAESTRUCTURA FÍSICA", "OBRAS COMPLEMENTARIAS", "SITIOS CRITICOS",
    "SITIOS CRÍTICOS", "DERRUMBE", "BANCA", "MUELLE", "CABLE AEREO", "CABLE AÉREO", "ANDEN", "ANDÉN",
    "ESPACIO PUBLICO", "ESPACIO PÚBLICO", "PREDIAL", "AVALUO", "AVALÚO", "VALORIZACION", "VALORIZACIÓN",
]


# ----------------------------------------------------------------- HTTP

def _get(params: dict, reintentos: int = 3) -> list:
    url = f"{URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url)
    token = os.environ.get("SOCRATA_APP_TOKEN")
    if token:
        req.add_header("X-App-Token", token)
    ultimo = None
    for i in range(reintentos):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                datos = json.loads(r.read().decode("utf-8"))
            if isinstance(datos, dict) and datos.get("error"):
                raise RuntimeError(datos.get("message", datos))
            return datos
        except (urllib.error.URLError, TimeoutError, RuntimeError) as e:
            ultimo = e
            time.sleep(2 * (i + 1))
    raise SystemExit(f"No se pudo consultar datos.gov.co ({ultimo}).")


def _esc(t: str) -> str:
    return t.replace("'", "''")


def construir_where(desde=None, hasta=None, tipo=None, modalidad=None, texto=None, infra=False,
                    nit=NIT_DEPTO) -> str:
    w = [f"nit_entidad = '{_esc(nit)}'", f"nombre_entidad != '{ENTIDAD_EXCLUIR}'"]
    if desde:
        w.append(f"fecha_de_firma >= '{desde}T00:00:00.000'")
    if hasta:
        w.append(f"fecha_de_firma <= '{hasta}T23:59:59.999'")
    if tipo:
        w.append("(" + " OR ".join(f"tipo_de_contrato = '{_esc(t)}'" for t in tipo) + ")")
    if modalidad:
        w.append(f"upper(modalidad_de_contratacion) like '%{_esc(modalidad.upper())}%'")
    if texto:
        t = _esc(texto.upper())
        w.append(f"(upper(objeto_del_contrato) like '%{t}%' OR upper(descripcion_del_proceso) like '%{t}%')")
    if infra:
        w.append("(" + " OR ".join(f"upper(objeto_del_contrato) like '%{_esc(p)}%'" for p in PALABRAS_INFRA) + ")")
    return " AND ".join(w)


def listar(where: str, maximo: int = 20000) -> list[dict]:
    filas, offset = [], 0
    while offset < maximo:
        lote = _get({"$select": ",".join(CAMPOS), "$where": where, "$order": "fecha_de_firma DESC",
                     "$limit": PAGINA, "$offset": offset})
        filas += lote
        if len(lote) < PAGINA:
            break
        offset += PAGINA
    return [normalizar(f) for f in filas]


def resumen(where: str) -> list[dict]:
    datos = _get({"$select": "tipo_de_contrato, modalidad_de_contratacion, count(*) as contratos, "
                             "sum(valor_del_contrato) as valor",
                  "$where": where, "$group": "tipo_de_contrato, modalidad_de_contratacion",
                  "$order": "valor DESC", "$limit": 200})
    for d in datos:
        d["contratos"] = int(float(d.get("contratos", 0)))
        d["valor"] = float(d.get("valor") or 0)
    return datos


# ----------------------------------------------------------------- Limpieza y formato

def normalizar(f: dict) -> dict:
    g = dict(f)
    for k in ("valor_del_contrato", "valor_pagado", "valor_pendiente_de_pago", "dias_adicionados"):
        if g.get(k) not in (None, ""):
            try:
                g[k] = float(g[k])
            except ValueError:
                pass
    for k in ("fecha_de_firma", "fecha_de_inicio_del_contrato", "fecha_de_fin_del_contrato", "ultima_actualizacion"):
        if g.get(k):
            g[k] = str(g[k])[:10]
    if isinstance(g.get("urlproceso"), dict):
        g["urlproceso"] = g["urlproceso"].get("url")
    if g.get("objeto_del_contrato"):
        g["objeto_del_contrato"] = re.sub(r"\s+", " ", g["objeto_del_contrato"]).strip()
    return g


def cop(x) -> str:
    try:
        s = f"{float(x):,.0f}"
    except (TypeError, ValueError):
        return ""
    return "$ " + s.replace(",", ".")


def imprimir(filas, campos, anchos=None, maximo=40):
    if not filas:
        print("Sin resultados.")
        return
    anchos = anchos or {}
    for f in filas[:maximo]:
        print(" | ".join(str(f.get(c, "") if c not in ("valor", "valor_del_contrato") else cop(f.get(c)))
                         [:anchos.get(c, 30)] for c in campos))
    if len(filas) > maximo:
        print(f"... {len(filas) - maximo} más (use --salida)")


def exportar(filas, ruta):
    if ruta.lower().endswith(".xlsx"):
        try:
            import pandas as pd
        except ImportError:
            raise SystemExit("Instale pandas y openpyxl o use .csv")
        pd.DataFrame(filas).to_excel(ruta, index=False)
    else:
        import csv
        claves = list(dict.fromkeys(k for f in filas for k in f))
        with open(ruta, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=claves, delimiter=";")
            w.writeheader()
            w.writerows(filas)
    print(f"Exportado: {ruta} ({len(filas)} filas)")


# ----------------------------------------------------------------- CLI

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for nombre in ("resumen", "buscar"):
        s = sub.add_parser(nombre)
        if nombre == "buscar":
            s.add_argument("texto", nargs="?")
        s.add_argument("--desde")
        s.add_argument("--hasta")
        s.add_argument("--tipo", nargs="+", help="Obra Interventoría Consultoría ...")
        s.add_argument("--modalidad", help="texto parcial, p. ej. 'licitación' o 'concurso'")
        s.add_argument("--infra", action="store_true", help="filtrar objetos de infraestructura física")
        s.add_argument("--nit", default=NIT_DEPTO)
        s.add_argument("--salida")
    c = sub.add_parser("contrato")
    c.add_argument("referencia")
    a = p.parse_args(argv)

    for fecha in (getattr(a, "desde", None), getattr(a, "hasta", None)):
        if fecha and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fecha):
            raise SystemExit("Fechas en formato AAAA-MM-DD")

    if a.cmd == "contrato":
        r = _esc(a.referencia)
        filas = [normalizar(x) for x in _get({"$select": ",".join(CAMPOS), "$limit": 20,
                 "$where": f"referencia_del_contrato = '{r}' OR id_contrato = '{r}' OR proceso_de_compra = '{r}'"})]
        for f in filas:
            for k in CAMPOS:
                v = f.get(k)
                print(f"{k:32} {cop(v) if k.startswith('valor') else v}")
            print("-" * 60)
        if not filas:
            print("No encontrado. Pruebe con el id CO1.PCCNTR... o el número de proceso.")
        return 0

    where = construir_where(a.desde, a.hasta, a.tipo, a.modalidad, getattr(a, "texto", None), a.infra, a.nit)

    if a.cmd == "resumen":
        datos = resumen(where)
        total_n = sum(d["contratos"] for d in datos)
        total_v = sum(d["valor"] for d in datos)
        print(f"{'Tipo':28} {'Modalidad':42} {'N.º':>6} {'Valor':>24}")
        for d in datos:
            print(f"{str(d.get('tipo_de_contrato'))[:28]:28} {str(d.get('modalidad_de_contratacion'))[:42]:42} "
                  f"{d['contratos']:>6} {cop(d['valor']):>24}")
        print(f"\nTOTAL: {total_n} contratos · {cop(total_v)}")
        print("Fuente: SECOP II – Contratos Electrónicos (datos.gov.co, jbjy-vk9h), consulta del "
              + time.strftime("%Y-%m-%d") + ". Valor = valor_del_contrato registrado (no incluye adiciones "
              "posteriores no registradas).")
        if a.salida:
            exportar(datos, a.salida)
        return 0

    filas = listar(where)
    imprimir(filas, ["fecha_de_firma", "referencia_del_contrato", "tipo_de_contrato", "valor_del_contrato",
                     "estado_contrato", "objeto_del_contrato"],
             {"objeto_del_contrato": 70, "referencia_del_contrato": 18})
    print(f"\n{len(filas)} contratos · valor total {cop(sum(f.get('valor_del_contrato') or 0 for f in filas))}")
    if a.salida:
        exportar(filas, a.salida)
    return 0


if __name__ == "__main__":
    sys.exit(main())
