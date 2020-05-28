"""
Licenced under MIT
"""
from .master import MasterDesign, fieldCreator
import datetime


class Villager(MasterDesign):
    def __init__(self, data: dict, expire: datetime):
        super().__init__(data, expire)
        self.response['description'] = data.get("quote")
        self.response['fields'] = [
            {
                "name": "Species:",
                "value": fieldCreator(data.get("species")),
                "inline": True
            },
            {
                "name": "Personality:",
                "value": fieldCreator(data.get("personality")),
                "inline": True
            },
            {
                "name": "Sign:",
                "value": fieldCreator(data.get("sign")),
                "inline": True
            },
            {
                "name": "Phrase:",
                "value": fieldCreator(data.get("phrase")),
                "inline": True
            },
            {
                "name": "Birthday:",
                "value": fieldCreator(data.get("birthday")),
                "inline": True
            },
            {
                "name": "Gender:",
                "value": fieldCreator(data.get("gender")),
                "inline": True
            },
            {
                "name": "Favourite Clothes:",
                "value": fieldCreator(data.get("favclothing")),
                "inline": True
            },
            {
                "name": "Favourite Colour:",
                "value": fieldCreator(data.get("favcolor")),
                "inline": True
            }
        ]
        self.response["footer"] = {
            "text": "Info from nookipedia.com",
            "icon_url": "https://cdn.vlee.me.uk/TurnipBot/Nookipedia.png"
        }
