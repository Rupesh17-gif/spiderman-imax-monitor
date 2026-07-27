import requests
import os

BOT_TOKEN = os.getenv("8850541633:AAFyLTq27M1zQEP2E9TDeAqv0CkiLSmdL9M")
CHAT_ID = os.getenv("729459307")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "✅ GitHub Test"
    }
)

print("Status:", r.status_code)
print("Response:", r.text)
