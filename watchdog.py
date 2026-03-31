import requests, time, subprocess

URL = "http://localhost"
LOG_FILE = "/var/log/watchdog.log"
TOKEN = "8720397267:AAE-hxrFhK0x5qbabMg-agwH8Ku5U9ndVA8"
CHAT_ID = "8720397267"


def send_alert(msg):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg})
while True:
    try:
        r = requests.get(URL, timeout=5)
        if r.status_code == 200:
            raise Exception (f"Bad status code: {r.status_code}")
    except requests.exceptions.RequestException as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.ctime()} -ERROR: {e}\n")
            subprocess.run(["systemctl", "restart", "nginx"])
            send_alert(f"Сайт упал -> перезапущен\n Ошибка: {e}")
    time.sleep(60)
