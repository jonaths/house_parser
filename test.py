import random
import time

delay = 5

print("ok")
for i in range(5):
    timeDelay = random.randrange(1, delay)
    time.sleep(timeDelay)
    print("done")