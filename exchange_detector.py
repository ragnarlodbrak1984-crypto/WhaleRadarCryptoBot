# Известные адреса бирж
# Потом будем расширять список

EXCHANGE_WALLETS = {

    "binance": [
        "0x0000000000000000000000000000000000000000"
    ],

    "okx": [
        "0x0000000000000000000000000000000000000000"
    ],

    "coinbase": [
        "0x0000000000000000000000000000000000000000"
    ]
}



def is_exchange(address):

    address = address.lower()


    for exchange, wallets in EXCHANGE_WALLETS.items():

        if address in wallets:

            return exchange


    return None



def detect_flow(from_address, to_address):

    sender = is_exchange(from_address)

    receiver = is_exchange(to_address)


    if sender and not receiver:

        return {
            "flow": "OUT",
            "exchange": sender,
            "meaning": "🟢 Вывод с биржи (накопление)"
        }


    if receiver and not sender:

        return {
            "flow": "IN",
            "exchange": receiver,
            "meaning": "🔴 Ввод на биржу (риск продажи)"
        }


    return {
        "flow": "UNKNOWN",
        "exchange": None,
        "meaning": "⚪ Неизвестное направление"
    }