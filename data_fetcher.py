import os
import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv()

PINNACLE_API_KEY = os.getenv("PINNACLE_API_KEY")
LIVESCORE_API_KEY = os.getenv("LIVESCORE_API_KEY")
API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")

async def fetch_pinnacle_odds():
    url = "<https://pinnacle-odds.p.rapidapi.com/kit/v1/special-markets>"
    headers = {"x-rapidapi-key": PINNACLE_API_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()

async def fetch_livescore_data():
    url = "<https://livescore6.p.rapidapi.com/v2/search>"
    headers = {"x-rapidapi-key": LIVESCORE_API_KEY}
    params = {"Category": "soccer", "Query": "chel"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            return await response.json()

async def fetch_api_football_data():
    url = "<https://api-football-v1.p.rapidapi.com/v2/odds/league/865927/bookmaker/5>"
    headers = {"x-rapidapi-key": API_FOOTBALL_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()

async def fetch_all_data():
    pinnacle_data = await fetch_pinnacle_odds()
    livescore_data = await fetch_livescore_data()
    football_data = await fetch_api_football_data()
    return pinnacle_data, livescore_data, football_data

if __name__ == "__main__":
    asyncio.run(fetch_all_data())
