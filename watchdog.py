import requests, time, subprocess

URL = "http://localhost"
LOG_FILE = "/home/admin/watchdog.log"

TOKEN = "8720397267:AAFqBU_vahEpBR1Qm4TDvwdFpr-d_xdRak0"
CHAT_ID = "280709449"


def send_alert(msg):
    r = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )
    print("TG:", r.status_code, r.text)

while True:
    try:
        r = requests.get(URL, timeout=5)
        if r.status_code != 200:
            raise Exception(f"Bad status code: {r.status_code}")

    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.ctime()} - ERROR: {e}\n")

        subprocess.run(["sudo", "systemctl", "restart", "nginx"])

        send_alert(f"Сайт упал → перезапущен\nОшибка: {e}")

    time.sleep(60)