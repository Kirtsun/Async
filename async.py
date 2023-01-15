import asyncio
import aiohttp


async def weather1(session):
    res = await session.get('https://api.open-meteo.com/v1/forecast?latitude=40.6971494&'
                            'longitude=-74.2598655&hourly=temperature_2m&start_date=2023-01-14&end_date=2023-01-14')
    res = await res.json()
    res = res['hourly']['temperature_2m']
    res_avg = int(sum(res) // len(res))
    return res_avg


async def weather2(session):
    r = await session.get('https://api.weatherbit.io/v2.0/current?lat=40.6971494&lon=-74.2598655&key=f8a1e5d2ca1944eca7e07b1d2713ce87&')
    res = await r.json()
    res = res['data'][0]['app_temp']
    return res


async def weather3(session):
    r = await session.get('http://api.weatherstack.com/current?access_key=6fbc9fe04b27f96b5f9dd375dec6b333&query=New%20York')
    res = await r.json()
    res = res['current']['temperature']
    return res


async def main():
    async with aiohttp.ClientSession() as session:
        res = await asyncio.gather(weather1(session), weather2(session), weather3(session))
    res = sum(res) / len(res)
    print(res)


asyncio.run(main())
