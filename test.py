import requests, os

TOKEN = os.getenv(TG_TOKEN)
CHAT_ID = os.getenv(TG_CHAT_ID)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
print(url)

r = requests.post(url, data={"chat_id": CHAT_ID, "text": "test"})
print(r.status_code)
print(r.text)