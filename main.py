from src.wall_steet_breakfast import get_today_link
from src.bot import send_message

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone, timedelta
from time import sleep

import logging
from logging.config import fileConfig

logger = logging.getLogger()
fileConfig('logging_config.ini')

def get_utc_time() ->datetime.time:
    now_utc_date = datetime.now(timezone.utc)
    now_utc_time = now_utc_date.time() # coverts datetime into time object
    return now_utc_time

def utc_to_nyc():
    nyc_time = get_utc_time() - timedelta(hours=5)
    return nyc_time

def wait_for_publishing(wait_minutes:int):
    #inital time is 6.am nyc or 11 utc
    # the time does not matter here
    data=get_today_link()
    while not data:
        sleep(60*wait_minutes)
        data=get_today_link()

    return data



def main():
    data = wait_for_publishing(15)
    sched = BlockingScheduler()
    sched.add_job(send_message(
    data), 
    'cron', 
    minute =13,
    hour=14)


#wsb usually publishes around 6am
#start conquence then
#while not get_today_link
##wait x=15 mins
#else send_message(get_today_link())



if __name__=='__main__':
    logging.debug("I'm a message for debugging purposes.")
    print(get_utc_time())
    # main()
    sched = BlockingScheduler()
    sched.add_job(send_message(
    get_today_link()), 
    'cron', 
    minute =13,
    hour=14)


    