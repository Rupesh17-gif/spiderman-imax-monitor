import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

print("TOKEN:", BOT_TOKEN[:15])

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

r = requests.get(url)

print("Status:", r.status_code)
print("Response:", r.text)
