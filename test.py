import requests

TOKEN = "8720397267:AAFqBU_vahEpBR1Qm4TDvwdFpr-d_xdRak0"
CHAT_ID = "8720397267"

r = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "test"}
)

print(r.text)