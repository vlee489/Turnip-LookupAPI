from lookupAPI.models import Villager, Critter, Fossil
import datetime
import aiohttp
from typing import Optional, List

# This is the time format that will be stored as DD/MM/YYYY/HH/MM
date_format = "%d/%m/%Y/%H/%M"
# Timeout for requests in seconds
timeout = aiohttp.ClientTimeout(total=20)
base_url = "https://nookipedia.com/api"


def checkValidCache(name: str, cache: list):
    """
    Checks if there's a valid entry of a name in
    :param name: str
        The name of the item to find
    :param cache: dict
        The dict to look through
    :return: dict
        The dict of the villager if in the cache, else returns none
    """
    for x in range(len(cache)):
        cachedItem = cache[x]
        if cachedItem.name == name:
            if cachedItem.localCacheExpire > datetime.datetime.now():
                return cachedItem
            else:
                del cache[x]
                return None
    return None


def clearOutdatedCache(cache: list):
    """
    Goes through Cache List and removes outdated entries
    :param cache: list
        Cache list to cleanup
    """
    for x in range(len(cache)):
        cachedItem = cache[x]
        if cachedItem.localCacheExpire < datetime.datetime.now():
            del cache[x]


class NookipediaAPI:
    cacheExpire = 12  # The default time till cache expires

    def __init__(self, api_key: str):
        """
        Constructor
        :param api_key: str
            The Nookipedia key to use.
        """
        self.header = {"X-API-KEY": api_key}
        self.villager_cache = []
        self.critter_cache = []
        self.fossil_cache = []

    def setCacheExpire(self, hours: int):
        """
        Set the time till a cached item expires
        :param hours: int
            The time in hours till the cache expires
        """
        self.cacheExpire = hours

    async def clearOutdatedCache(self):
        """
        Clear outdated cache from cache entries
        """
        clearOutdatedCache(self.villager_cache)
        clearOutdatedCache(self.critter_cache)
        clearOutdatedCache(self.fossil_cache)

    async def __requestJson(self, url: str) -> Optional[dict]:
        """
        Private Function
        Requests a data from Nookipedia website
        :param url: str
            The URL to request from
        :return: dict
            The dict reply from the website.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.header) as response:
                if response.status != 200:
                    return None
                response = await response.json()
                if response is None:
                    return response
                return response

    async def getVillager(self, name: str) -> Optional[Villager]:
        """
        Requests a villager
        :param name: str
            Name of the villager requested
        :return:
        """
        cachedEntry = checkValidCache(name, self.villager_cache)
        if cachedEntry is None:
            expire = datetime.datetime.now() + datetime.timedelta(hours=self.cacheExpire)
            cachedEntry = await self.__requestJson(f"{base_url}/villager/{name}/")
            if cachedEntry is None:
                return None
            cachedEntry = Villager(cachedEntry, expire)
            self.villager_cache.append(cachedEntry)
        return cachedEntry

    async def getVillagerList(self) -> List[str]:
        """
        Get the villager list from Nookipedia
        :return: List[Str]
            A list of strings with of the villager names
        """
        request = await self.__requestJson(f"{base_url}/villager/")
        villagerList = list()
        for villager in request:
            name = villager.get("villager_key")
            if name is not None:
                villagerList.append(name)
        return villagerList

    async def getCritter(self, name: str) -> Optional[Critter]:
        """
        Requests a critter
        :param name: str
            Name of the critter to lookup
        :return: Critter
            Returns a critter object
        """
        cachedEntry = checkValidCache(name, self.critter_cache)
        if cachedEntry is None:
            expire = datetime.datetime.now() + datetime.timedelta(hours=self.cacheExpire)
            cachedEntry = await self.__requestJson(f"{base_url}/critter/{name}/")
            if cachedEntry is None:
                return None
            cachedEntry = Critter(cachedEntry, expire)
            self.critter_cache.append(cachedEntry)
        return cachedEntry

    async def getFossil(self, name: str) -> Optional[Fossil]:
        """
        Request a fossil
        :param name: str
            Name of fossil in question
        :return: Fossil
            Returns a Fossil Object
        """
        cachedEntry = checkValidCache(name, self.fossil_cache)
        if cachedEntry is None:
            expire = datetime.datetime.now() + datetime.timedelta(hours=self.cacheExpire)
            cachedEntry = await self.__requestJson(f"{base_url}/fossil/{name}/")
            if cachedEntry is None:
                return None
            cachedEntry = Fossil(cachedEntry, expire)
            self.fossil_cache.append(cachedEntry)
        return cachedEntry

    async def getToday(self) -> Optional[dict]:
        response = await self.__requestJson(f"{base_url}/today/")
        if response is None:
            return None
        return response
