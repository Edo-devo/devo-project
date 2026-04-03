import requests, time, os

URL = "http://localhost"
TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")


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
