from whale_database import get_recent_whales


def generate_report():

    whales = get_recent_whales(24)

    if not whales:
        return (
            "🐋 Whale Report 24h\n\n"
            "Пока крупных движений не найдено."
        )


    total = len(whales)

    buy = 0
    sell = 0
    tokens = {}


    for w in whales:

        value = w["usd_value"]

        tokens[w["token"]] = (
            tokens.get(w["token"], 0) + value
        )


        if "BUY" in w["direction"]:
            buy += value

        elif "SELL" in w["direction"]:
            sell += value


    top = sorted(
        tokens.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]


    text = (
        "🐋 Whale Report 24h\n\n"
        f"📊 Всего переводов: {total}\n\n"
        f"🟢 Покупки: ${buy:,.0f}\n"
        f"🔴 Продажи: ${sell:,.0f}\n\n"
        "🔥 Топ токены:\n"
    )


    for token, value in top:

        text += (
            f"{token}: ${value:,.0f}\n"
        )


    return text
