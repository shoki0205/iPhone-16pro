import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1507884513571635341/1b_RgTKpfVRvJo0EinBo1EtDeG3BJZnYr6W2U0VzijoMAgmCrsaCO8096RT26f8hh2xm"

URL = "https://www.apple.com/jp/shop/refurbished/iphone"

sent = set()

while True:
    html = requests.get(URL).text

    targets = [
        "iPhone 16 Pro 128GB",
        "iPhone 16 Pro 256GB"
    ]

    for t in targets:
        if t in html and t not in sent:
            requests.post(
                WEBHOOK,
                json={
                    "content": f"入荷検知: {t}"
                }
            )
            sent.add(t)

    time.sleep(180)
