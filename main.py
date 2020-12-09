from src.wall_steet_breakfast import get_today_link
from src.bot import send_message

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone, timedelta
from time import sleep

import logging
from logging.config import fileConfig
from os import environ


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
    # I find out which version of python heroku uses

    logging.debug("start of wait_for_publishing")
    data=get_today_link()

    while not data:
        logging.debug("wait_for_publishing while loop")
        logging.debug(f"data: {data}")

        sleep(60*wait_minutes)
        data=get_today_link()

    logging.debug(f"loop finished data: {data}")
    return data


def main():
    data = wait_for_publishing(15)
    hook_url = environ.get('discord_link')
    send_message(data, hook_url)


if __name__=='__main__':
    #logger data
    logger = logging.getLogger()
    fileConfig('logging_config.ini')

    logging.debug("I'm a message for debugging purposes.")
    logging.debug(get_utc_time())

    sched = BlockingScheduler()
    sched.add_job(
        main, 
        'cron', 
        minute =40,
        hour=19
    )
    sched.start()
