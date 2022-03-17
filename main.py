import asyncio
import aiohttp
from az_price import az_fetch
from fk_price import fk_fetch

az_url = (
    "https://www.amazon.in/BenQ-PD2500Q-Calibrated-Anti-Glare-Adjustable/dp/B0737M9QP7"
)

fk_url = "https://www.flipkart.com/benq-25-inch-quad-hd-ultra-slim-bezel-height-adjustable-monitor-pd2500q/p/itmfa3eb55bc0d26"


async def main():
    print("Checking")
    async with aiohttp.ClientSession() as session:
        azPrice = await az_fetch(az_url, session)
        fkPrice = await fk_fetch(fk_url, session)
        print("azPrice: ", azPrice)
        print("fkPrice: ", fkPrice)
    print("sleeping for 120s")
    await asyncio.sleep(120)


if __name__ == "__main__":
    while True:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("Exiting")
            break
        except Exception as e:
            print("Error: ", e)
            break
