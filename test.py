import requests

TOKEN = "8720397267:AAFqBU_vahEpBR1Qm4TDvwdFpr-d_xdRak0"
CHAT_ID = "280709449"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
print(url)

r = requests.post(url, data={"chat_id": CHAT_ID, "text": "test"})
print(r.status_code)
print(r.text)