def calculate_score(
    buy_volume,
    sell_volume,
    exchange_flow,
    usd_value
):

    score = 50


    # направление движения денег
    if buy_volume > sell_volume:
        score += 20

    elif sell_volume > buy_volume:
        score -= 20


    # движение с бирж или на биржи
    if exchange_flow == "OUT":
        score += 15

    elif exchange_flow == "IN":
        score -= 15


    # размер сделки
    if usd_value >= 10000000:
        score += 15

    elif usd_value >= 1000000:
        score += 5


    # ограничение 0-100
    score = max(0, min(score, 100))


    return score