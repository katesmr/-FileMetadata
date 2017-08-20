import time
import threading


def threadfunc():
    while True:
        print("thread")
        time.sleep(1)

t = threading.Thread(target=threadfunc)
t.daemon = True
t.start()

