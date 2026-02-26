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
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(MOVIE_URL, headers=headers)
    print("STATUS:", r.status_code)
    print("PAGE LENGTH:", len(r.text))
    print(r.text[:2000])  # print first 2000 characters
    return True

for _ in range(10):
    print("Checking movie page...")
    if check_booking():
        break
    time.sleep(30)
