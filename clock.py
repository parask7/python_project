import datetime
import time

print("clock")

while True:
    clock = datetime.datetime.now()
    print("\r", clock.strftime("%H:%M:%S"), flush=True, end=" ")
    time.sleep(1)