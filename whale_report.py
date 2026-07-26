
from whale_database import get_recent_whales
from whale_sentiment import analyze_sentiment


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

        value = float(w.get("usd_value", 0))

        token = w.get(
            "token",
            "UNKNOWN"
        )

        tokens[token] = (
            tokens.get(token, 0) + value
        )


        direction = w.get(
            "direction",
            ""
        ).upper()


        if "BUY" in direction or "ПОКУП" in direction:
            buy += value


        elif "SELL" in direction or "ПРОДА" in direction:
            sell += value



    sentiment = analyze_sentiment(
        buy,
        sell
    )


    text = (
        "🐋 Whale Report 24h\n\n"
        f"{sentiment['signal']}\n"
        f"Сила сигнала: {sentiment['strength']}%\n\n"
        f"📊 Всего переводов: {total}\n\n"
        f"🟢 Покупки: ${buy:,.0f}\n"
        f"🔴 Продажи: ${sell:,.0f}\n\n"
        "🔥 Топ токены:\n"
    )


    top_tokens = sorted(
        tokens.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]


    for token, value in top_tokens:

        text += (
            f"{token}: ${value:,.0f}\n"
        )


    return text