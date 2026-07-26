from whale_database import get_recent_whales


def get_whale_ranking(hours=24):

    whales = get_recent_whales(hours)


    if not whales:

        return (
            "🐋 TOP WHALE ACTIVITY 24H\n\n"
            "Активность китов не найдена."
        )


    ranking = {}


    for whale in whales:

        token = whale.get(
            "token",
            "UNKNOWN"
        )


        value = float(
            whale.get(
                "usd_value",
                0
            )
        )


        if token not in ranking:

            ranking[token] = {
                "volume": 0,
                "count": 0
            }


        ranking[token]["volume"] += value
        ranking[token]["count"] += 1



    sorted_tokens = sorted(
        ranking.items(),
        key=lambda x: x[1]["volume"],
        reverse=True
    )


    text = "🐋 TOP WHALE ACTIVITY 24H\n\n"


    position = 1


    for token, data in sorted_tokens[:10]:

        text += (
            f"#{position} {token}\n"
            f"💰 Volume: ${data['volume']:,.0f}\n"
            f"🔄 Transactions: {data['count']}\n\n"
        )

        position += 1


    return text