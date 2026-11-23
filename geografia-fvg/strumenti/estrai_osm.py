"""Estrae dall'estratto OpenStreetMap del FVG i livelli elencati in catalogo_osm.txt.

Uso: python3 estrai_osm.py ESTRATTO.osm.pbf CARTELLA_USCITA
Scrive un file <id>.jsonl per livello, con un elemento GeoJSON per riga.
"""
import collections
import json
import pathlib
import sys

import osmium
import osmium.geom

PRECISIONE = 7
STATI_CONFINANTI = {"AT": "Austria", "SI": "Slovenia"}
STRADE = {
    "osm_strade_autostrade": {"motorway", "motorway_link", "trunk", "trunk_link"},
    "osm_strade_principali": {"primary", "primary_link", "secondary", "secondary_link",
                              "tertiary", "tertiary_link"},
    "osm_strade_locali": {"unclassified", "residential", "living_street", "service",
                          "pedestrian", "road", "busway"},
    "osm_strade_campestri": {"track"},
    "osm_sentieri": {"path", "footway", "bridleway", "steps", "via_ferrata"},
    "osm_piste_ciclabili": {"cycleway"},
}
STRADA_LIVELLO = {v: k for k, vs in STRADE.items() for v in vs}
PERCORSI = {
    "bicycle": "osm_percorsi_ciclabili", "mtb": "osm_percorsi_ciclabili",
    "hiking": "osm_percorsi_escursionistici", "foot": "osm_percorsi_escursionistici",
    "bus": "osm_linee_autobus", "trolleybus": "osm_linee_autobus",
    "ferry": "osm_traghetti", "piste": "osm_piste_sci", "ski": "osm_piste_sci",
}
SUOLO_NATURALE = {"wood", "scrub", "grassland", "heath", "bare_rock", "scree", "wetland",
                  "beach", "sand", "shingle", "fell", "mud", "shrubbery"}
SANITA = {"hospital", "clinic", "doctors", "pharmacy", "dentist", "veterinary",
          "nursing_home", "social_facility"}
UFFICI = {"townhall", "courthouse", "post_office", "community_centre", "public_building"}
SICUREZZA = {"police", "fire_station", "ranger_station"}
ISTRUZIONE = {"school", "kindergarten", "university", "college", "library", "music_school"}
CULTURA = {"theatre", "cinema", "arts_centre"}
CULTO = {"place_of_worship", "monastery"}
PARCHEGGI = {"parking", "bicycle_parking", "motorcycle_parking"}
SCARTA_AMENITY = {"parking_space", "parking_entrance"}


def arrotonda(coordinate):
    if isinstance(coordinate[0], (int, float)):
        return [round(coordinate[0], PRECISIONE), round(coordinate[1], PRECISIONE)]
    return [arrotonda(c) for c in coordinate]


def livelli_punto(t):
    """Livelli a cui appartiene un punto di interesse (nodo o baricentro di area)."""
    trovati = []
    amenity = t.get("amenity")
    if amenity in UFFICI or t.get("office") == "government":
        trovati.append(("osm_municipi_uffici", amenity or "government"))
    if amenity in SANITA or "healthcare" in t:
        trovati.append(("osm_sanita", amenity or t.get("healthcare")))
    if amenity in SICUREZZA or "emergency" in t and t["emergency"] not in ("no", "yes", "designated", "private", "destination", "official"):
        trovati.append(("osm_sicurezza_emergenza", amenity if amenity in SICUREZZA else t["emergency"]))
    if amenity in ISTRUZIONE:
        trovati.append(("osm_istruzione", amenity))
    if amenity in CULTO:
        trovati.append(("osm_culto", amenity))
    turismo = t.get("tourism")
    if "historic" in t or amenity in CULTURA or turismo in ("museum", "gallery", "artwork", "attraction"):
        trovati.append(("osm_cultura_storia", t.get("historic") or amenity or turismo))
    elif turismo:
        trovati.append(("osm_turismo", turismo))
    if "leisure" in t or (t.get("sport") and not trovati):
        trovati.append(("osm_sport_tempo_libero", t.get("leisure") or t.get("sport")))
    if amenity in PARCHEGGI:
        trovati.append(("osm_parcheggi", amenity))
    if "man_made" in t or t.get("power") in ("plant", "substation", "generator", "tower") or "telecom" in t:
        trovati.append(("osm_infrastrutture", t.get("man_made") or t.get("power") or t.get("telecom")))
    if "aeroway" in t:
        trovati.append(("osm_aeroporti", t["aeroway"]))
    if t.get("leisure") == "marina" or t.get("harbour") == "yes" or t.get("landuse") == "harbour" \
            or t.get("seamark:type") == "harbour" or amenity == "ferry_terminal" or t.get("man_made") == "pier":
        trovati.append(("osm_porti", "porto"))
    if not trovati or "shop" in t or "craft" in t:
        chiave = next((k for k in ("shop", "craft", "amenity", "office") if k in t), None)
        if chiave and t[chiave] not in SCARTA_AMENITY and not (chiave == "amenity" and trovati):
            trovati.append(("osm_commercio_servizi", t[chiave]))
    return trovati


def livelli_nodo(t):
    trovati = []
    if "place" in t:
        trovati.append(("osm_luoghi", t["place"]))
    naturale = t.get("natural")
    if naturale in ("peak", "volcano"):
        trovati.append(("osm_cime", naturale))
    if naturale == "saddle" or t.get("mountain_pass") == "yes":
        trovati.append(("osm_passi", naturale or "mountain_pass"))
    if naturale == "spring":
        trovati.append(("osm_sorgenti", naturale))
    if naturale == "cave_entrance":
        trovati.append(("osm_grotte", naturale))
    if t.get("waterway") == "waterfall":
        trovati.append(("osm_cascate", "waterfall"))
    if t.get("railway") in ("station", "halt", "tram_stop"):
        trovati.append(("osm_stazioni", t["railway"]))
    if t.get("highway") == "bus_stop":
        trovati.append(("osm_fermate_autobus", "bus_stop"))
    return trovati + livelli_punto(t)


def livelli_linea(t):
    trovati = []
    strada = t.get("highway")
    if strada in STRADA_LIVELLO:
        trovati.append((STRADA_LIVELLO[strada], strada))
    if "railway" in t and t["railway"] not in ("platform", "station", "turntable", "roundhouse"):
        trovati.append(("osm_ferrovie", t["railway"]))
    if "waterway" in t and t["waterway"] not in ("riverbank", "dock", "boatyard", "dam", "weir", "lock_gate", "fuel"):
        trovati.append(("osm_corsi_acqua", t["waterway"]))
    if "aerialway" in t and t["aerialway"] not in ("station", "pylon"):
        trovati.append(("osm_impianti_fune", t["aerialway"]))
    if t.get("power") in ("line", "minor_line", "cable"):
        trovati.append(("osm_linee_elettriche", t["power"]))
    naturale = t.get("natural")
    if naturale == "coastline":
        trovati.append(("osm_linea_costa", naturale))
    if naturale in ("ridge", "arete", "cliff"):
        trovati.append(("osm_creste_pareti", naturale))
    if naturale == "valley":
        trovati.append(("osm_valli", naturale))
    if "piste:type" in t:
        trovati.append(("osm_piste_sci", t["piste:type"]))
    if t.get("route") == "ferry":
        trovati.append(("osm_traghetti", "ferry"))
    if t.get("aeroway") in ("runway", "taxiway"):
        trovati.append(("osm_aeroporti", t["aeroway"]))
    return trovati


def livelli_area(t):
    """Restituisce (livelli con poligono, livelli con baricentro)."""
    poligoni = []
    naturale, uso = t.get("natural"), t.get("landuse")
    if naturale == "water" or t.get("waterway") == "riverbank" or uso in ("reservoir", "basin"):
        poligoni.append(("osm_acque", t.get("water") or naturale or uso))
    if t.get("building") and t["building"] != "no":
        poligoni.append(("osm_edifici", t["building"]))
    if t.get("place") in ("island", "islet"):
        poligoni.append(("osm_isole", t["place"]))
    if naturale == "glacier":
        poligoni.append(("osm_ghiacciai", naturale))
    if uso == "military" or "military" in t:
        poligoni.append(("osm_aree_militari", t.get("military") or uso))
    elif (uso and uso not in ("reservoir", "basin")) or naturale in SUOLO_NATURALE:
        poligoni.append(("osm_uso_suolo", uso or naturale))
    if t.get("boundary") in ("protected_area", "national_park") or t.get("leisure") == "nature_reserve":
        poligoni.append(("osm_aree_protette", t.get("protect_class") or t.get("boundary") or "nature_reserve"))
    if t.get("boundary") == "administrative" and t.get("admin_level") in ("9", "10"):
        poligoni.append(("osm_frazioni_confini", t["admin_level"]))
    if t.get("aeroway") in ("aerodrome", "apron", "helipad", "heliport"):
        poligoni.append(("osm_aeroporti", t["aeroway"]))
    if t.get("amenity") in PARCHEGGI:
        poligoni.append(("osm_parcheggi", t["amenity"]))
    gia = {l for l, _ in poligoni}
    punti = [x for x in livelli_punto(t) if x[0] not in gia]
    return poligoni, punti


class Scrittore:
    def __init__(self, cartella):
        self.cartella = pathlib.Path(cartella)
        self.cartella.mkdir(parents=True, exist_ok=True)
        self.file = {}
        self.conteggi = collections.Counter()

    def scrivi(self, livello, geometria, proprieta):
        if livello not in self.file:
            self.file[livello] = open(self.cartella / f"{livello}.jsonl", "w", encoding="utf8")
        elemento = {"type": "Feature", "properties": proprieta, "geometry": geometria}
        self.file[livello].write(json.dumps(elemento, ensure_ascii=False, separators=(",", ":")) + "\n")
        self.conteggi[livello] += 1

    def chiudi(self):
        for f in self.file.values():
            f.close()


def proprieta(oggetto, tipo, categoria, extra=None):
    p = {"osm_id": f"{tipo}/{oggetto.id}" if not isinstance(oggetto, str) else oggetto, "categoria": categoria}
    return p


def baricentro_anelli(coordinate, tipo):
    anelli = [coordinate[0]] if tipo == "Polygon" else [p[0] for p in coordinate]
    anello = max(anelli, key=len)
    n = len(anello)
    return [round(sum(c[0] for c in anello) / n, PRECISIONE), round(sum(c[1] for c in anello) / n, PRECISIONE)]


def principale():
    pbf, uscita = sys.argv[1], sys.argv[2]
    # Primo passaggio: relazioni di percorso e di confine, per sapere quali vie servono.
    percorsi, confini_via = [], collections.defaultdict(list)
    for r in osmium.FileProcessor(pbf, osmium.osm.RELATION):
        t = dict(r.tags)
        vie = [m.ref for m in r.members if m.type == "w"]
        if t.get("type") == "route" and t.get("route") in PERCORSI:
            percorsi.append((r.id, t, vie))
        elif t.get("boundary") == "administrative" and t.get("admin_level") in ("2", "4", "6", "8", "9", "10"):
            nome = t.get("name:it") or t.get("name") or ""
            for v in vie:
                confini_via[v].append((int(t["admin_level"]), nome, t.get("ISO3166-1") or t.get("ISO3166-1:alpha2") or ""))
    servono = {v for _, _, vie in percorsi for v in vie} | set(confini_via)
    geometrie_via = {}

    scrittore = Scrittore(uscita)
    fabbrica = osmium.geom.GeoJSONFactory()
    lettore = osmium.FileProcessor(pbf).with_locations().with_areas()
    for o in lettore:
        if o.is_node():
            if not o.tags:
                continue
            t = dict(o.tags)
            trovati = livelli_nodo(t)
            if trovati:
                geometria = {"type": "Point", "coordinates": [round(o.location.lon, PRECISIONE), round(o.location.lat, PRECISIONE)]}
                for livello, categoria in trovati:
                    scrittore.scrivi(livello, geometria, {"osm_id": f"node/{o.id}", "categoria": categoria, **t})
        elif o.is_way():
            t = dict(o.tags)
            trovati = livelli_linea(t) if t else []
            if not trovati and o.id not in servono:
                continue
            try:
                coordinate = [[round(n.lon, PRECISIONE), round(n.lat, PRECISIONE)] for n in o.nodes]
            except osmium.InvalidLocationError:
                continue
            if len(coordinate) < 2:
                continue
            if o.id in servono:
                geometrie_via[o.id] = coordinate
            geometria = {"type": "LineString", "coordinates": coordinate}
            for livello, categoria in trovati:
                scrittore.scrivi(livello, geometria, {"osm_id": f"way/{o.id}", "categoria": categoria, **t})
        elif o.is_area():
            t = dict(o.tags)
            poligoni, punti = livelli_area(t)
            if not poligoni and not punti:
                continue
            try:
                geometria = json.loads(fabbrica.create_multipolygon(o))
            except Exception:
                continue
            geometria["coordinates"] = arrotonda(geometria["coordinates"])
            if len(geometria["coordinates"]) == 1:
                geometria = {"type": "Polygon", "coordinates": geometria["coordinates"][0]}
            ident = f"way/{o.orig_id()}" if o.from_way() else f"relation/{o.orig_id()}"
            for livello, categoria in poligoni:
                scrittore.scrivi(livello, geometria, {"osm_id": ident, "categoria": categoria, **t})
            if punti:
                punto = {"type": "Point", "coordinates": baricentro_anelli(geometria["coordinates"], geometria["type"])}
                for livello, categoria in punti:
                    scrittore.scrivi(livello, punto, {"osm_id": ident, "categoria": categoria, "geometria_origine": "area", **t})

    # Percorsi: unione delle vie che li compongono.
    for ident, t, vie in percorsi:
        linee = [geometrie_via[v] for v in vie if v in geometrie_via]
        if linee:
            scrittore.scrivi(PERCORSI[t["route"]], {"type": "MultiLineString", "coordinates": linee},
                             {"osm_id": f"relation/{ident}", "categoria": t["route"], **t})
    # Confini: ogni via con il livello amministrativo più alto a cui appartiene.
    for via, appartenenze in confini_via.items():
        if via not in geometrie_via:
            continue
        geometria = {"type": "LineString", "coordinates": geometrie_via[via]}
        livello_min = min(a[0] for a in appartenenze)
        nomi = sorted({f"{a[0]}:{a[1]}" for a in appartenenze if a[1]})
        p = {"osm_id": f"way/{via}", "livello_amministrativo": livello_min,
             "categoria": {2: "Stato", 4: "regione", 6: "provincia", 8: "comune", 9: "circoscrizione", 10: "frazione"}[livello_min],
             "enti": "; ".join(nomi)}
        scrittore.scrivi("osm_confini_linee", geometria, p)
        stati = sorted({STATI_CONFINANTI[a[2]] for a in appartenenze if a[0] == 2 and a[2] in STATI_CONFINANTI})
        if stati:
            scrittore.scrivi("osm_confine_stato", geometria, {"osm_id": f"way/{via}", "categoria": "confine di Stato", "stato_confinante": " e ".join(stati)})
    scrittore.chiudi()
    for livello, numero in sorted(scrittore.conteggi.items()):
        print(livello, numero)


if __name__ == "__main__":
    principale()
