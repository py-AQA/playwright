import math

from playwright.sync_api import Dialog


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


def handle_stepik_alert(alert: Dialog):
    assert alert.message.startswith("Congrats"), "NOPE!"
    print(f"\nStepik code: {alert.message.split()[-1]}")
    alert.accept()
