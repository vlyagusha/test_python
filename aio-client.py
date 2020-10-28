import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:3001/') as response:
            print(await response.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
