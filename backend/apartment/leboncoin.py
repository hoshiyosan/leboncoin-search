import requests
from datetime import datetime
from apartment.errors import SearchError

LOCATION = "9"
SELL = "10"

DEFAULT_FAKE_HEADERS = {
    "Host": "api.leboncoin.fr",
    "Origin": "https://www.leboncoin.fr",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
}


def parse_attributes(attributes):
    parsed = {}
    for attribute in attributes:
        if attribute["key"] == "square":
            parsed["surface"] = int(float(attribute["value"]))
        elif attribute["key"] == "ges":
            parsed["ges"] = (
                None
                if attribute["value"] == "v" or attribute["value"].startswith("Non")
                else attribute["value"]
            )
        elif attribute["key"] == "energy_rate":
            parsed["energy_rate"] = (
                None
                if attribute["value"] == "v" or attribute["value"].startswith("Non")
                else attribute["value"]
            )
        elif attribute["key"] == "rooms":
            parsed["rooms"] = int(attribute["value"])
        elif attribute["key"] == "fai_included":
            parsed["honoraires"] = bool(int(attribute["value"]))
    return parsed


def parse_anounce(anounce):
    uid = "leboncoin:%s" % anounce["list_id"]
    try:
        date = datetime.strptime(anounce["first_publication_date"], "%Y-%m-%d %H:%M:%S")
    except:
        date = datetime.now()

    try:
        images = anounce["images"]["urls_large"]
    except:
        images = None

    normalized = {
        "uid": uid,
        "title": anounce["subject"],
        "price": anounce["price"][0],
        "timestamp": int(date.timestamp()),
        "description": anounce["body"],
        "images": images,
        "anounce_url": anounce["url"],
        "apartment": parse_attributes(anounce["attributes"]),
        "location": anounce["location"],
    }

    return normalized


filters = {
    "category": {"id": "10"},
    "enums": {"ad_type": ["offer"], "furnished": ["2"]},
    "keywords": {"text": "appartement"},
    "location": {
        "locations": [
            {
                "locationType": "city",
                "label": "Cesson-Sévigné (35510)",
                "city": "Cesson-Sévigné",
                "zipcode": "35510",
                "department_id": "35",
                "region_id": "6",
                "area": {"lat": 48.11713, "lng": -1.60421, "default_radius": 4856},
            },
            {
                "locationType": "city",
                "label": "Rennes (35200)",
                "city": "Rennes",
                "zipcode": "35200",
                "department_id": "35",
                "region_id": "6",
                "area": {"lat": 48.08861, "lng": -1.66045, "default_radius": 7841},
            },
            {
                "locationType": "city",
                "label": "Rennes (35700)",
                "city": "Rennes",
                "zipcode": "35700",
                "department_id": "35",
                "region_id": "6",
                "area": {"lat": 48.13277, "lng": -1.65757, "default_radius": 9002},
            },
            {
                "locationType": "city",
                "label": "Chantepie (35135)",
                "city": "Chantepie",
                "zipcode": "35135",
                "department_id": "35",
                "region_id": "6",
                "area": {"lat": 48.08851, "lng": -1.6195, "default_radius": 4322},
            },
        ]
    },
    "ranges": {
        "price": {"min": 400, "max": 650},
        "rooms": {"min": 2},
        "square": {"min": 40},
    },
}

waouh = {
    "filters": filters,
    "limit": 35,
    "limit_alu": 3,
    "owner_type": "all",
}


class Leboncoin:
    def search(
        self,
        anounce_type=LOCATION,
        min_size=7,
        max_size=500,
        min_rooms=1,
        max_rooms=10,
        min_price=0,
        max_price=1000000,
        professional=False,
    ):
        query = {
            "filters": {
                "category": {"id": anounce_type},
                "enums": {"ad_type": ["offer"]},
                "location": {
                    "locations": [
                        {
                            "locationType": "city",
                            "city": "Rennes",
                            "label": "Rennes (toute la ville)",
                            "area": {
                                "lat": 48.10980729840584,
                                "lng": -1.6675040381352901,
                                "default_radius": 10000,
                                "radius": 5000,
                            },
                        }
                    ]
                },
                "keywords": {"text": "vente", "parrot_used": 4},
                "ranges": {
                    "square": {"min": min_size, "max": max_size},
                    "price": {"min": min_price, "max": max_price},
                    "rooms": {"min": min_rooms, "max": max_rooms},
                },
            },
            "limit": 35,
            "limit_alu": 3,
            "owner_type": "all",
        }
        headers = {
            "Connection": "keep-alive",
            "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            "api_key": "ba0c2dad52b3ec",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://www.leboncoin.fr",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.leboncoin.fr/",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        }

        response = requests.post(
            "https://api.leboncoin.fr/finder/search",
            headers=headers,
            json=query
        )

        response_data = response.json()
        raw_anounces = response_data.get("ads")

        if not raw_anounces:
            return None

        anounces = []

        import json

        with open("tata.json", "w") as out:
            json.dump(raw_anounces, out)

        for anounce in raw_anounces:
            anounces.append(parse_anounce(anounce))

        with open("tutu.json", "w") as out:
            json.dump(anounces, out)

        print(anounces)

        return anounces
