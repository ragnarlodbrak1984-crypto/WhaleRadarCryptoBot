import json
import os
from datetime import datetime


FILE = "whale_history.json"


def load_history():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_whale(data):

    history = load_history()

    data["time"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    history.append(data)


    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            history,
            f,
            indent=4,
            ensure_ascii=False
        )



def get_recent_whales(limit=10):

    history = load_history()

    return history[-limit:]