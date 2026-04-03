import requests, time, subprocess, os

URL = "http://localhost"
LOG_FILE = "/home/admin/watchdog.log"

TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")


def send_alert(msg):
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": msg}
        )
    except:
        pass  # чтобы не падал сервис


while True:
    try:
        r = requests.get(URL, timeout=5)
        if r.status_code != 200:
            raise Exception(f"Bad status code: {r.status_code}")

    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.ctime()} - ERROR: {e}\n")

        subprocess.run(["sudo", "systemctl", "restart", "nginx"])
        send_alert(f"🚨 Сайт упал → перезапущен\nОшибка: {e}")

    time.sleep(60)