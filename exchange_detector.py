# Известные адреса бирж Ethereum
# Список можно расширять

EXCHANGE_WALLETS = {

    "Binance": [
        "0x28C6c06298d514Db089934071355E5743bf21d60",
        "0x21a31Ee1afC51d94C2eFcCAa2092aD7D7F4fE9A"
    ],

    "OKX": [
        "0x236F9F97e0E62388479f5AEc5B8A0D5cA7B6F5C5"
    ],

    "Coinbase": [
        "0x503828976D22510aad0201ac7EC88293211D23Da"
    ]
}



def is_exchange(address):

    if not address:
        return None

    address = address.lower()


    for exchange, wallets in EXCHANGE_WALLETS.items():

        for wallet in wallets:

            if address == wallet.lower():
                return exchange


    return None



def detect_flow(from_address, to_address):

    sender = is_exchange(from_address)

    receiver = is_exchange(to_address)


    # Биржа отправила наружу
    if sender and not receiver:

        return {
            "flow": "OUT",
            "exchange": sender,
            "meaning": "🟢 Вывод с биржи — возможное накопление"
        }


    # Кошелёк отправил на биржу
    if receiver and not sender:

        return {
            "flow": "IN",
            "exchange": receiver,
            "meaning": "🔴 Ввод на биржу — возможное давление продажи"
        }


    return {
        "flow": "UNKNOWN",
        "exchange": None,
        "meaning": "⚪ Личный кошелёк / неизвестное направление"
    }