from whale_database import get_recent_whales
from whale_sentiment import analyze_sentiment
from whale_score import calculate_score


def generate_report():

    whales = get_recent_whales(24)


    if not whales:

        return (
            "🐋 Whale Report 24h\n\n"
            "Крупных движений не найдено."
        )


    total_value = 0
    buy = 0
    sell = 0

    tokens = {}


    for whale in whales:

        value = float(
            whale.get(
                "usd_value",
                0
            )
        )

        total_value += value


        token = whale.get(
            "token",
            "UNKNOWN"
        )


        tokens[token] = (
            tokens.get(token, 0)
            + value
        )


        direction = whale.get(
            "direction",
            ""
        ).upper()


        if "BUY" in direction:
            buy += value

        elif "SELL" in direction:
            sell += value



    sentiment = analyze_sentiment(
        buy,
        sell
    )


    score = calculate_score(
        buy,
        sell,
        "OUT",
        total_value
    )


    report = (
        "🐋 WHALE REPORT 24H\n\n"
        f"{sentiment}\n\n"
        f"⭐ Whale Score: {score}/100\n\n"
        f"💰 Volume: ${total_value:,.0f}\n"
        f"🟢 Buy: ${buy:,.0f}\n"
        f"🔴 Sell: ${sell:,.0f}\n\n"
        "🔥 Top tokens:\n"
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