def get_whale_level(usd_value):

    if usd_value >= 5000000:
        return "🐋 BIG WHALE"

    elif usd_value >= 1000000:
        return "🐬 MEDIUM WHALE"

    elif usd_value >= 100000:
        return "🐟 SMALL WHALE"

    else:
        return "Normal"


def analyze_direction(from_address, to_address, exchanges):

    from_address = from_address.lower()
    to_address = to_address.lower()

    for exchange, wallets in exchanges.items():

        wallets = [
            w.lower()
            for w in wallets
        ]

        if to_address in wallets:
            return (
                "🔴 POSSIBLE SELL\n"
                f"Wallet → {exchange}"
            )

        if from_address in wallets:
            return (
                "🟢 POSSIBLE ACCUMULATION\n"
                f"{exchange} → Wallet"
            )

    return "⚪ Wallet → Wallet"