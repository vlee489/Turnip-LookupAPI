"""
This file deals with looking up items dedicated to
Turnip Bot and it's file storage.

Licenced under MIT (c) Vincent Lee 2020
"""
import datetime
import aiohttp
from typing import Optional
from lookupAPI.models import Diy
import requests

# Timeout for requests in seconds
timeout = aiohttp.ClientTimeout(total=20)
base_url = ""


class LocalLookup:
    def __init__(self):
        """
        Constructor
        """
        response = requests.get(url="{}/{}".format(base_url, "diy.json"))
        if response.status_code != 200:
            raise SystemError("Unable to get DIY File")
        self.diy_cache = response.json()

    async def updateData(self) -> bool:
        """
        Updates the data cached
        :return: bool
            If the update was successful or not
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url="{}/{}".format(base_url, "diy.json")) as response:
                if response.status != 200:
                    return False
                response = await response.json()
                if response is None:
                    return False
                else:
                    self.diy_cache = response
                    return True

    async def getDiy(self, name: str) -> Optional[Diy]:
        """
        Lookup a DIY recipe
        :param name: str
            Name of the item
        :return: Diy
            Diy Object or None
        """
        name = name.title()
        if name in self.diy_cache:
            return Diy(name, self.diy_cache[name])
        else:
            return None
