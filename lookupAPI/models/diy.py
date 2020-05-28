"""
Object for DIY recipes

Licenced under MIT
"""
import datetime
from .master import fieldCreator


class Diy:
    def __init__(self, name: str, data: dict):
        self.response = {}  # Holds the response for the bot.
        self.name = name
        self.response['timestamp'] = datetime.datetime.now().isoformat()
        self.response['color'] = 0xCF70D3
        self.response['title'] = name
        self.response['description'] = "Here's DIY info on {}".format(name)
        self.response['author'] = {
            "name": "Turnip Bot",
            "icon_url": "https://cdn.vlee.me.uk/TurnipBot/icon.png",
            "url": "https://github.com/vlee489/Turnip-Bot/"
        }
        self.response['thumbnail'] = {
            "url": data.get('image')
        }
        materials = "```\n"
        for key, value in data["materials"].items():
            materials = materials + "{} : {}\n".format(key, value)
        materials = materials + "```"
        self.response['fields'] = [
            {
                "name": "Materials Needed:",
                "value": materials,
                "inline": False
            },
            {
                "name": "Recipe from:",
                "value": fieldCreator(data.get("source")),
                "inline": False
            },
            {
                "name": "Recipe Sell Price:",
                "value": fieldCreator(data.get("sell")),
                "inline": True
            },
            {
                "name": "Recipe Buy Price:",
                "value": fieldCreator(data.get("buy")),
                "inline": True
            },
            {
                "name": "Mile Buy Price:",
                "value": fieldCreator(data.get("miles")),
                "inline": True
            },
            {
                "name": "Category:",
                "value": fieldCreator(data.get("category")),
                "inline": True
            },
            {
                "name": "Unlocked in:",
                "value": fieldCreator(data.get("unlocked")),
                "inline": True
            }
        ]
        self.response["footer"] = {
            "text": "Info from ACNH Spreadsheet",
            "icon_url": "https://cdn.vlee.me.uk/TurnipBot/ACNHSpreadhseet.png"
        }
