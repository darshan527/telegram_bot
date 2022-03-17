# import imp
from bs4 import BeautifulSoup
import asyncio
import aiohttp


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


def parse(res: str) -> float:
    soup = BeautifulSoup(res, "html.parser")
    tmp = soup.find("div", class_="_30jeq3 _16Jk6d")
    # print(tmp.text)
    if tmp != None:
        tmp = tmp.text
        tmp = tmp[1:]
        tmp = tmp.replace(",", "")
        # print(float(tmp))
        # print("Done")
        return float(tmp)
    else:
        return 0


async def fk_fetch(url: str, session: aiohttp.ClientSession):
    async with session.get(url, headers=headers) as response:
        res = await response.text()
        return parse(res)


async def main():
    async with aiohttp.ClientSession() as session:
        await fk_fetch(
            "https://www.flipkart.com/benq-25-inch-quad-hd-ultra-slim-bezel-height-adjustable-monitor-pd2500q/p/itmfa3eb55bc0d26",
            session,
        )
    # try:
    #     with open("data.html", "r") as f:
    #         res = f.read()
    #         parse(res)
    # except Exception as e:
    #     print("HTML File Not found")


if __name__ == "__main__":
    asyncio.run(main())
