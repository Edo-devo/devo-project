import requests, time

URL = "http://localhost"
TOKEN = "8720397267:AAE-hxrFhK0x5qbabMg-agwH8Ku5U9ndVA8"
CHAT_ID = "8720397267"


def send_alert(massage):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": massage}
    requests.post(url, data=data)
def check_server():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print("Server OK")
        else:
            send_alert(f"ALARM! Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        send_alert(f"ALARM! Error: {e}")
while True:
    check_server()
    time.sleep(60)