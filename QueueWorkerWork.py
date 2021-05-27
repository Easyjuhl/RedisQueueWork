from redis import Redis
from time import sleep
import psutil
from rq import Queue
from PING import MyPing

# Creates Queue
q = Queue(connection=Redis())

overwrite = False

# Used to test the Redis queue part
overIn = input("Run mode: ").lower()
if overIn == "test":
    overwrite = True


while True:

    # Converts RAM info into a percentage
    RAMInfo = psutil.virtual_memory()
    RAMPercent = (RAMInfo[3]/RAMInfo[1])*100

    while psutil.cpu_percent() > 80 or RAMPercent > 80 or overwrite == True:
        # Adds job to queue
        ret = q.enqueue(MyPing, "Hej")

        sleep(1)
        print(ret.result, "Test")
    
    # Code for normal use below this point