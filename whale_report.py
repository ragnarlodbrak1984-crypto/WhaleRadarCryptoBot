import json
import os
from datetime import datetime, timedelta


FILE = "whale_history.json"


def load_history():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def generate_report():

    history = load_history()

    if not history:
        return "🐋 WHALE REPORT\n\nНет данных за период"



    limit_time = datetime.now() - timedelta(hours=24)

    recent = []


    for item in history:

        try:
            tx_time = datetime.strptime(
                item["time"],
                "%Y-%m-%d %H:%M:%S"
            )

            if tx_time >= limit_time:
                recent.append(item)

        except:
            continue



    if not recent:
        return (
            "🐋 WHALE REPORT (24h)\n\n"
            "Крупных движений не обнаружено"
        )



    total_value = 0
    buys = 0
    sells = 0


    tokens = {}


    for item in recent:

        value = item.get(
            "value",
            0
        )

        total_value += value


        direction = item.get(
            "direction",
            ""
        )


        if "накопление" in direction:
            buys += value


        if "продажа" in direction:
            sells += value



        token = item.get(
            "token",
            "UNKNOWN"
        )


        tokens[token] = (
            tokens.get(token, 0)
            + value
        )



    report = (
        "🐋 WHALE REPORT (24h)\n\n"
        f"📊 Операций: {len(recent)}\n"
        f"💰 Общий объём: ${total_value:,.0f}\n\n"
        f"🟢 Накопление: ${buys:,.0f}\n"
        f"🔴 Продажи: ${sells:,.0f}\n\n"
        "🪙 Топ токены:\n"
    )


    for token, value in sorted(
        tokens.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]:

        report += (
            f"{token}: ${value:,.0f}\n"
        )


    return report