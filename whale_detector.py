import asyncio
import requests
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, ETHERSCAN_API_KEY
from tokens import TOKENS
from exchanges import EXCHANGES
from prices import get_price
from whale_levels import get_whale_level


async def send_alert(text):
    bot = Bot(BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


def check_token_transfers(token_name, contract):

    url = "https://api.etherscan.io/api"

    params = {
        "module": "account",
        "action": "tokentx",
        "contractaddress": contract,
        "page": 1,
        "offset": 5,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "1":
        return []

    if not isinstance(data.get("result"), list):
        return []

    return data["result"]


async def monitor():

    checked = set()

    await send_alert(
        "🐋 Whale Detector запущен\n"
        "✅ Мониторинг активен"
    )

    while True:

        for name, data in TOKENS.items():

            transfers = check_token_transfers(
                name,
                data["address"]
            )

            for tx in transfers:

                tx_hash = tx["hash"]

                if tx_hash in checked:
                    continue

                checked.add(tx_hash)

                amount = int(tx["value"]) / (
                    10 ** int(tx["tokenDecimal"])
                )

                price = get_price(name)
                usd_value = amount * price

                whale_level = get_whale_level(usd_value)

                if usd_value > 100000:

                    from_address = tx["from"].lower()
                    to_address = tx["to"].lower()

                    direction = "⚪ Wallet → Wallet"

                    for exchange, wallets in EXCHANGES.items():

                        wallets = [
                            w.lower()
                            for w in wallets
                        ]

                        if to_address in wallets:
                            direction = (
                                f"🔴 Wallet → {exchange}\n"
                                f"⚠️ Возможная продажа"
                            )

                        if from_address in wallets:
                            direction = (
                                f"🟢 {exchange} → Wallet\n"
                                f"📈 Возможное накопление"
                            )


                    await send_alert(
                        f"🐋 WHALE ALERT\n\n"
                        f"🪙 {name}\n"
                        f"💰 Amount: {amount:,.0f}\n"
                        f"💵 Value: ${usd_value:,.0f}\n"
                        f"🏆 Level: {whale_level}\n\n"
                        f"{direction}\n\n"
                        f"🔗 TX:\n{tx_hash}"
                    )

        await asyncio.sleep(60)


print("Запуск Whale Detector...")


if __name__ == "__main__":
    asyncio.run(monitor())