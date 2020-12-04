from src.wall_steet_breakfast import get_today_link
from src.bot import send_message
from os import environ

if __name__=='__main__':
    send_message(get_today_link())