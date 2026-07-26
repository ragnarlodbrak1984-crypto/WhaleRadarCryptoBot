import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, ETHERSCAN_API_KEY
from tokens import TOKENS

async def send_message(text):
    bot = Bot(BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


def get_latest_block():
    url = "https://api.etherscan.io/api"

    params = {
        "module": "proxy",
        "action": "eth_blockNumber",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("result")


async def monitor():
    last_block = None

    while True:
        block = get_latest_block()

        if block and block != last_block:
            last_block = block

            await send_message(
                f"🐋 Whale Radar Ethereum\n\n"
                f"⛓ Новый блок:\n{block}\n\n"
                f"✅ Сеть работает\n\n"
f"📌 Отслеживаем: {len(TOKENS)} монет"
            )

        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(monitor())