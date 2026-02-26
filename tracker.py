import requests
import time
import sys

TOKEN = sys.argv[1]
CHAT_ID = sys.argv[2]
MOVIE = sys.argv[3]
CITY = sys.argv[4]

def send_telegram(text):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )

def check_booking():
    url = f"https://in.bookmyshow.com/{CITY.lower().replace(' ', '-')}/movies"
    r = requests.get(url)
    
    page = r.text.lower()

    if MOVIE.lower() in page and "book" in page:
        send_telegram(f"🔥 TICKETS LIVE for {MOVIE} in {CITY}!\n{url}")
        return True

    return False

for _ in range(10):
    print("Checking...")
    if check_booking():
        break
    time.sleep(30)
