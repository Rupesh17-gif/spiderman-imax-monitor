import requests
import os

BOT_TOKEN = os.getenv("8850541633:AAFyLTq27M1zQEP2E9TDeAqv0CkiLSmdL9M")
CHAT_ID = os.getenv("729459307")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    r = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

    print(r.status_code)

send_telegram("✅ GitHub Spider-Man Monitor Test")