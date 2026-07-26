import asyncio
import requests

from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, ETHERSCAN_API_KEY
from tokens import TOKENS
from prices import get_price

from exchange_detector import detect_flow
from whale_analysis import get_whale_level
from price_prediction import predict_market_effect


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
        "offset": 10,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }


    response = requests.get(
        url,
        params=params
    )

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
        "✅ Анализ китов активен"
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


                amount = int(
                    tx["value"]
                ) / (
                    10 ** int(tx["tokenDecimal"])
                )


                price = get_price(name)

                usd_value = amount * price


                minimum = data.get(
                    "min_amount",
                    500000
                )


                if amount < minimum:
                    continue


                from_address = tx["from"].lower()
                to_address = tx["to"].lower()


                flow = detect_flow(
                    from_address,
                    to_address
                )


                level = get_whale_level(
                    usd_value
                )


                prediction = predict_market_effect(
                    usd_value,
                    flow["flow"],
                    usd_value * 20
                )


                await send_alert(

                    f"🐋 WHALE ALERT\n\n"
                    f"🪙 Token: {name}\n"
                    f"💰 Value: ${usd_value:,.0f}\n\n"

                    f"⭐ Whale Level:\n"
                    f"{level}\n\n"

                    f"{flow['meaning']}\n"
                    f"🏦 Exchange: {flow['exchange']}\n\n"

                    f"📈 Market Impact:\n"
                    f"{prediction['signal']}\n"
                    f"Score: {prediction['score']}/100\n\n"

                    f"🔗 TX:\n{tx_hash}"

                )


        await asyncio.sleep(60)



if __name__ == "__main__":

    print("Запуск Whale Detector...")

    asyncio.run(monitor())