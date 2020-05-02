"""
This is the master object for items coming coming from Nookipedia
"""
import datetime


def fieldCreator(data) -> str:
    if data is None:
        return "Unknown"
    return data


class MasterDesign:
    response = {}  # Holds the response for the bot.

    def __init__(self, data: dict, expire: datetime):
        self.api_expire_cache = data.get("api-expire-cache")
        self.localCacheExpire = expire
        self.name = data.get("name")
        self.response['timestamp'] = datetime.datetime.now().isoformat()
        self.response['color'] = 0xCF70D3
        self.response['title'] = data.get("name")
        self.response['url'] = data.get("link")
        self.response['author'] = {
            "name": "Turnip Bot",
            "icon_url": "https://vleedn.fra1.cdn.digitaloceanspaces.com/TurnipBot/icon.png",
            "url": "https://github.com/vlee489/Turnip-Bot/"
        }
        self.response['thumbnail'] = {
            "url": data.get('image')
        }

