def analyze_sentiment(buy_volume, sell_volume):

    total = buy_volume + sell_volume

    if total == 0:
        return {
            "signal": "⚪ Нет данных",
            "strength": 0
        }


    buy_percent = (buy_volume / total) * 100


    if buy_percent >= 70:

        return {
            "signal": "🟢 НАКОПЛЕНИЕ КИТАМИ",
            "strength": round(buy_percent)
        }


    elif buy_percent <= 30:

        return {
            "signal": "🔴 ВОЗМОЖНАЯ ПРОДАЖА",
            "strength": round(100 - buy_percent)
        }


    else:

        return {
            "signal": "🟡 НЕЙТРАЛЬНО",
            "strength": round(abs(50 - buy_percent) * 2)
        }