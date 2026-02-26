import requests
import time
import sys

TOKEN = sys.argv[1]
CHAT_ID = sys.argv[2]
MOVIE_URL = sys.argv[3]

def send_telegram(text):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )

def check_booking():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(MOVIE_URL, headers=headers)
    page = r.text.lower()

    if "book tickets" in page or "book now" in page:
        send_telegram(f"🔥 TICKETS ARE LIVE!\n{MOVIE_URL}")
        return True

    return False

for _ in range(10):
    print("Checking movie page...")
    if check_booking():
        break
    time.sleep(30)
