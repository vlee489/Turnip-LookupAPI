from .master import MasterDesign, fieldCreator
import datetime


class Fossil(MasterDesign):
    def __init__(self, data: dict, expire: datetime):
        super().__init__(data, expire)
        self.response['description'] = "Here's some info on {}:".format(data.get("name"))
        self.response['fields'] = [
            {
                "name": "Sections:",
                "value": fieldCreator(data.get("sections")),
                "inline": False
            },
            {
                "name": "Price:",
                "value": fieldCreator(data.get("price")),
                "inline": False
            },
            {
                "name": "Length:",
                "value": fieldCreator(data.get("length")),
                "inline": True
            },
            {
                "name": "Period:",
                "value": fieldCreator(data.get("period")),
                "inline": True
            },
            {
                "name": "Scientific Name:",
                "value": fieldCreator(data.get("scientific-name")),
                "inline": True
            }
        ]
        self.response["footer"] = {
            "text": "Info from nookipedia.com",
            "icon_url": "https://vleedn.fra1.cdn.digitaloceanspaces.com/TurnipBot/Nookipedia.png"
        }
