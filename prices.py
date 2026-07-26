from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

COIN_IDS = {
    "USDT": "tether",
    "USDC": "usd-coin",
    "DAI": "dai",
    "LINK": "chainlink",
    "UNI": "uniswap",
    "AAVE": "aave",
    "SHIB": "shiba-inu",
    "PEPE": "pepe",
    "DEXE": "dexe",

    "ONDO": "ondo-finance",
    "WLD": "worldcoin-wld",
    "MORPHO": "morpho",
    "MKR": "maker"
}


def get_price(symbol):

    if symbol not in COIN_IDS:
        return 0

    data = cg.get_price(
        ids=COIN_IDS[symbol],
        vs_currencies="usd"
    )

    return data[COIN_IDS[symbol]]["usd"]