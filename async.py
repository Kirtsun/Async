import asyncio

import aiohttp

from dotenv import load_dotenv

import os

load_dotenv()


async def weather1(session):
    res = await session.get('https://api.open-meteo.com/v1/forecast?latitude=40.6971494&'
                            'longitude=-74.2598655&hourly=temperature_2m&start_date=2023-01-14&end_date=2023-01-14')
    res = await res.json()
    res = res['hourly']['temperature_2m']
    res_avg = int(sum(res) // len(res))
    return res_avg


# async def weather2(session):
#     weather22 = os.getenv('WEATHER2')
#     r = await session.get('https://api.weatherbit.io/v2.0/current?lat=40.6971494&lon=-74.2598655&key='+weather22)
#     res = await r.json()
#     print(res)
#     res = res['data'][0]['app_temp']
#     return res


async def weather3(session):
    weather33 = os.getenv('WEATHER3')
    r = await session.get('http://api.weatherstack.com/current?access_key='+weather33+'&query=New%20York')
    res = await r.json()
    res = res['current']['temperature']
    return res


async def main():
    async with aiohttp.ClientSession() as session:
        res = await asyncio.gather(weather1(session), weather3(session))
    res = sum(res) / len(res)
    print(f'Average weather in new york {res} celsius')


# asyncio.run(main())
if __name__ == "__main__":
    asyncio.run(main())