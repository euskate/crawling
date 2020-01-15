# pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time

def exec_interval():     # 일정시간 간격으로 수행
    print("hello world")

def exec_cron():
    str = time.strftime('%c', time.localtime(time.time()))
    print("cron: ",str)

sched = BlockingScheduler()

# # 5초간격으로 함수 호출
# sched.add_job(exec_interval, 'interval', seconds=5)
# sched.start()

# 예약 방식 (매시간 10초, 30초일 경우 구동)
sched.add_job(exec_cron,'cron', minute="*", second="10, 30")
sched.start()