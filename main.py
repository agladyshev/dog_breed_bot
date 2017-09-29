import os
from telegram.ext import Updater, CommandHandler, MessageHandler, BaseFilter
import logging
import re
import pendulum
from datetime import datetime
import json


updater = Updater(token=os.environ.get('TOKEN'))


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


class FilterIgor(BaseFilter):

    def filter(self, message):
        if message.text:
            return re.search(u'Игор[^\s{1, 3}]', message.text, re.UNICODE)

filter_igor = FilterIgor()


def whatTime(bot, update):
    khabarovskh_time = "В Комсомольске-на-Амуре " + \
        pendulum.now('Asia/Vladivostok').format('%H:%M')
    bot.send_message(chat_id=update.message.chat_id,
                     text=khabarovskh_time)


time_handler = MessageHandler(filter_igor, whatTime)


dispatcher = updater.dispatcher
dispatcher.add_handler(time_handler)


updater.start_polling()
