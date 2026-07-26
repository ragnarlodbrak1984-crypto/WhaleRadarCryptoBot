def predict_market_effect(
    usd_value,
    flow,
    token_volume
):

    score = 50


    # размер кита
    if usd_value >= 10000000:
        score += 20

    elif usd_value >= 1000000:
        score += 10


    # направление
    if flow == "OUT":
        score += 15

    elif flow == "IN":
        score -= 15


    # влияние относительно объёма
    if token_volume > 0:

        impact = (
            usd_value / token_volume
        ) * 100


        if impact > 5:
            score += 10


    score = max(
        0,
        min(score, 100)
    )


    if score >= 75:
        signal = "🟢 Сильное влияние"

    elif score >= 55:
        signal = "🟡 Среднее влияние"

    else:
        signal = "🔴 Слабый/негативный сигнал"


    return {
        "score": score,
        "signal": signal
    }