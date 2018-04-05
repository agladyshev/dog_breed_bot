import os
from telegram.ext import Updater, CommandHandler, MessageHandler, BaseFilter, Filters
import logging
import re
import json


# updater = Updater(token=os.environ.get('TOKEN'))
updater = Updater(token='579059922:AAHyb14wI8jf6Qxgx-4QqOyCKj6O_Xw2osQ')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

def whatBreed(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='got it')
    
handler = MessageHandler(Filters.photo, 
                         whatBreed)




dispatcher = updater.dispatcher

dispatcher.add_handler(handler)


updater.start_polling()
