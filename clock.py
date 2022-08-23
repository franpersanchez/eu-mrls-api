from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from FileGenerator import fileCreation


sched = BlockingScheduler()

# Schedule job_function to be called every day
sched.add_job(fileCreation, 'cron', hour=3, minute=30)

sched.start()