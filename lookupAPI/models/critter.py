"""
Licenced under MIT
"""
from .master import MasterDesign, fieldCreator
import datetime


class Critter(MasterDesign):
    def __init__(self, data: dict, expire: datetime):
        super().__init__(data, expire)
        self.response['description'] = "Here's some info on {}:".format(data.get("name"))
        self.response['fields'] = [
            {
                "name": "Time of Year:",
                "value": fieldCreator(data.get("time-year")),
                "inline": False
            },
            {
                "name": "Time of Day:",
                "value": fieldCreator(data.get("time-day")),
                "inline": False
            },
            {
                "name": "Size:",
                "value": fieldCreator(data.get("size")),
                "inline": True
            },
            {
                "name": "Rarity:",
                "value": fieldCreator(data.get("rarity")),
                "inline": True
            },
            {
                "name": "Family:",
                "value": fieldCreator(data.get("family")),
                "inline": True
            },
            {
                "name": "Sale Price:",
                "value": fieldCreator(data.get("price")),
                "inline": False
            },
            {
                "name": "Catch Phrase:",
                "value": fieldCreator(data.get("caught")),
                "inline": False
            }
        ]
        self.response["footer"] = {
            "text": "Info from nookipedia.com",
            "icon_url": "https://vleedn.fra1.cdn.digitaloceanspaces.com/TurnipBot/Nookipedia.png"
        }
