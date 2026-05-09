from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Juris Sentinel Awb API",
    description="Niet-officiële API voor geselecteerde Awb-artikelen. Controleer actuele wetstekst altijd via wetten.overheid.nl.",
    version="0.1.0"
)

AWB = {
    "1-3": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "1:3",
        "kop": "Besluitbegrip",
        "tekst": "Definitieve tekst controleren via wetten.overheid.nl.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "3-2": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "3:2",
        "kop": "Zorgvuldige voorbereiding",
        "tekst": "Bij de voorbereiding van een besluit vergaart het bestuursorgaan de nodige kennis omtrent de relevante feiten en de af te wegen belangen.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "3-3": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "3:3",
        "kop": "Verbod van détournement de pouvoir",
        "tekst": "Het bestuursorgaan gebruikt de bevoegdheid tot het nemen van een besluit niet voor een ander doel dan waarvoor die bevoegdheid is verleend.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "3-4": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "3:4",
        "kop": "Belangenafweging en evenredigheid",
        "tekst": "Het bestuursorgaan weegt de rechtstreeks bij het besluit betrokken belangen af. De voor een of meer belanghebbenden nadelige gevolgen van een besluit mogen niet onevenredig zijn in verhouding tot de met het besluit te dienen doelen.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "3-46": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "3:46",
        "kop": "Draagkrachtige motivering",
        "tekst": "Een besluit dient te berusten op een deugdelijke motivering.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "4-13": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "4:13",
        "kop": "Beslistermijn",
        "tekst": "Een beschikking dient te worden gegeven binnen de bij wettelijk voorschrift bepaalde termijn of, bij het ontbreken daarvan, binnen een redelijke termijn.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "4-17": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "4:17",
        "kop": "Dwangsom bij niet tijdig beslissen",
        "tekst": "Definitieve tekst controleren via wetten.overheid.nl.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "6-2": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "6:2",
        "kop": "Gelijkstelling met besluit",
        "tekst": "Voor de toepassing van wettelijke voorschriften over bezwaar en beroep worden met een besluit gelijkgesteld: de schriftelijke weigering een besluit te nemen en het niet tijdig nemen van een besluit.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "6-12": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "6:12",
        "kop": "Beroep niet tijdig beslissen",
        "tekst": "Definitieve tekst controleren via wetten.overheid.nl.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "7-2": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "7:2",
        "kop": "Hoorplicht in bezwaar",
        "tekst": "Voordat een bestuursorgaan op het bezwaar beslist, stelt het belanghebbenden in de gelegenheid te worden gehoord.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    },
    "8-81": {
        "wet": "Algemene wet bestuursrecht",
        "afkorting": "Awb",
        "artikel": "8:81",
        "kop": "Voorlopige voorziening",
        "tekst": "Definitieve tekst controleren via wetten.overheid.nl.",
        "bron": "wetten.overheid.nl",
        "status": "niet-officiële weergave; actuele tekst verifiëren"
    }
}

THEMAS = {
    "niet-tijdig-beslissen": {
        "thema": "Niet tijdig beslissen",
        "kernartikelen": ["4:13", "4:17", "6:2", "6:12"],
        "toelichting": "Gebruik voor analyse van besluittermijnen, ingebrekestelling, dwangsom en beroep niet tijdig beslissen."
    },
    "zorgvuldigheid": {
        "thema": "Zorgvuldigheid, motivering en evenredigheid",
        "kernartikelen": ["3:2", "3:4", "3:46"],
        "toelichting": "Gebruik voor analyse van onderzoeksplicht, belangenafweging, evenredigheid en motivering."
    },
    "detournement-de-pouvoir": {
        "thema": "Détournement de pouvoir",
        "kernartikelen": ["3:3"],
        "toelichting": "Gebruik wanneer wordt onderzocht of een bestuursorgaan een bevoegdheid mogelijk voor een ander doel gebruikt dan waarvoor die bevoegdheid is verleend."
    },
    "voorlopige-voorziening": {
        "thema": "Voorlopige voorziening",
        "kernartikelen": ["8:81"],
        "toelichting": "Gebruik voor analyse van spoedeisend belang en tijdelijke rechterlijke voorziening."
    },
    "bezwaar": {
        "thema": "Bezwaarprocedure",
        "kernartikelen": ["6:2", "7:2"],
        "toelichting": "Gebruik voor analyse van bezwaar, hoorplicht en gelijkstelling van niet tijdig beslissen met een besluit."
    }
}

@app.get("/")
def root():
    return {
        "naam": "Juris Sentinel Awb API",
        "versie": "0.1.0",
        "status": "online",
        "disclaimer": "Niet-officiële API. Controleer actuele wetstekst via wetten.overheid.nl."
    }

@app.get("/awb/artikel/{artikel}")
def get_awb_artikel(artikel: str):
    artikel = artikel.replace(":", "-")
    if artikel not in AWB:
        raise HTTPException(status_code=404, detail="Artikel niet gevonden")
    return AWB[artikel]

@app.get("/awb/search")
def search_awb(q: str):
    q_lower = q.lower()
    results = []
    for item in AWB.values():
        searchable = f"{item['artikel']} {item['kop']} {item['tekst']}".lower()
        if q_lower in searchable:
            results.append(item)
    return {"query": q, "results": results}

@app.get("/awb/thema/{thema}")
def get_awb_thema(thema: str):
    if thema not in THEMAS:
        raise HTTPException(status_code=404, detail="Thema niet gevonden")
    return THEMAS[thema]
