import time
from plyer import notification

while(True):
    notification.notify(
        title="Start Coding NOW!",
        message="You have to crack the coding round of Amazon or Google. So Stop Gaming and Start Coding NOW!",
        app_icon="icon.ico",
        timeout = 10
    )
    time.sleep(10)