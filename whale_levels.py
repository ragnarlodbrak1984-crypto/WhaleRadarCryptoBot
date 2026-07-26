def get_whale_level(usd_value):

    if usd_value >= 10000000:
        return "🐳 MEGA WHALE"

    elif usd_value >= 1000000:
        return "🐋 WHALE"

    elif usd_value >= 500000:
        return "🐬 BIG MOVE"

    elif usd_value >= 100000:
        return "🐟 SMALL WHALE"

    else:
        return "⚪ Normal"