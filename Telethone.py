import datetime
import schedule
import calendar
import telethon
from telethon import TelegramClient
from datetime import date


api_id = 7662574
api_hash = 'cb741f79a828bdda5d39ac46a7843720'
bot_token = '1870162930:AAH9nuNI5LZMTwN4p_O3Rblr2wkJmieCJNE'


c = datetime.date.today()
my_date = datetime.date.today().weekday()
d = calendar.day_name[my_date]

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# The first parameter is the .session file name (absolute paths allowed)
def send_day():
    with bot:
        bot.loop.run_until_complete(bot.send_message('PYRPYRNUY_BOBER', str(c)))
        bot.loop.run_until_complete(bot.send_message('PYRPYRNUY_BOBER', str(d)))
        bot.loop.run_until_complete(bot.send_message('PYRPYRNUY_BOBER', 'Доброе утро! Напоминаю тебе про: спорт для oculus quest 2, про меня и Рэм тоже не забудь) Удачного дня! Встретимся завтра!'))

schedule.every().day.at("10:30").do(send_day)

while True:
    schedule.run_pending()