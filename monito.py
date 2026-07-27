import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN =", BOT_TOKEN)
print("CHAT_ID =", CHAT_ID)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

r = requests.get(url)

print("Status:", r.status_code)
print("Response:", r.text)
