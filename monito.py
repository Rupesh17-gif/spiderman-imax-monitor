import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN Length:", len(BOT_TOKEN))
print("BOT_TOKEN First 10 Chars:", BOT_TOKEN[:10])
print("CHAT_ID:", CHAT_ID)
