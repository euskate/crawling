import random
from apscheduler.schedulers.blocking import BlockingScheduler
import time

a = random.randint(1, 10)
b = str(a)

def exec_cron():
    str = time.strftime('%c', time.localtime(time.time()))
    print("cron: ",str)

sched = BlockingScheduler()

sched.add_job(exec_cron,'cron', minute="*", second=b)
sched.start()