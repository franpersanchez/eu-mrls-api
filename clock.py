from apscheduler.schedulers.blocking import BackgroundScheduler
from datetime import datetime
from FileGenerator import fileCreation

def thisfunc():
    print("todo bien")
    
sched = BackgroundScheduler()

# Schedule job_function to be called every day
sched.add_job(thisfunc, 'intervals', seconds=30)

sched.start()