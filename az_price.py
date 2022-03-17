from bs4 import BeautifulSoup
import asyncio
import aiohttp


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


def parse(res: str) -> float:
    soup = BeautifulSoup(res, "html.parser")
    tmp = soup.find("span", class_="a-price-whole")
    # print(tmp.text)
    if tmp != None:
        tmp = tmp.text
        tmp = tmp.replace(",", "")
        # print(float(tmp))
        # print("Done")
        return float(tmp)
    else:
        return 0


async def az_fetch(url: str, session: aiohttp.ClientSession):
    async with session.get(url, headers=headers) as response:
        res = await response.text()
        return parse(res)


async def main():
    # async with aiohttp.ClientSession() as session:
    #     await fetch(
    #         "https://www.amazon.in/AmazonBasics-Mini-DisplayPort-Cable-Feet/dp/B013PWQPFS/",
    #         session,
    #     )
    try:
        with open("dataa.html", "r") as f:
            res = f.read()
            parse(res)
    except Exception as e:
        print("HTML File Not found")


if __name__ == "__main__":
    asyncio.run(main())
