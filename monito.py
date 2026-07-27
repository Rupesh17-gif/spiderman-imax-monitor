import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URLS = [
    "https://www.pvrcinemas.com/moviesessions/Chennai/SPIDERMAN-BRAND-NEW-DAY/35294",
    "https://in.bookmyshow.com/movies/chennai/spider-man-brand-new-day/buytickets/ET00447840/20260730"
]

found = False

for url in URLS:
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        )

        text = r.text.lower()

        if (
            "imax" in text
            or "palazzo" in text
            or "luxe" in text
            or "showtime" in text
            or "book tickets" in text
        ):
            found = True

    except Exception as e:
        print(e)

if found:

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text":
            "🚨 POSSIBLE SPIDER-MAN IMAX UPDATE!\n\n"
            "Check Palazzo IMAX and Luxe IMAX immediately:\n"
            "https://www.pvrcinemas.com/moviesessions/Chennai/SPIDERMAN-BRAND-NEW-DAY/35294"
        }
    )

    print("Alert sent")

else:
    print("No update found")
