from apscheduler.schedulers.background import BackgroundScheduler
import datetime

scheduler = BackgroundScheduler()

def schedule_job(job_id, interval, func):
    if interval == 'Every Monday':
        scheduler.add_job(func, 'cron', day_of_week='mon', id=str(job_id))
    # Add more interval conditions here
    
def dummy_job():
    print(f"Job executed at {datetime.datetime.now()}")

scheduler.start()
