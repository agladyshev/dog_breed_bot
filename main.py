import os
import sys
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, BaseFilter, Filters
import logging
import re
import json
import io
from PIL import Image
from dog_detector import DogDetector
from human_detector import HumanDetector


# updater = Updater(token=os.environ.get('TOKEN'))
updater = Updater(token='579059922:AAHyb14wI8jf6Qxgx-4QqOyCKj6O_Xw2osQ')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

dogDetector = DogDetector()
humanDetector = HumanDetector()

def whatBreed(bot, update):

    bot.getFile(update.message.photo[-1].file_id).download('input.jpg')
    image = open('input.jpg', 'rb')
    image = image.read()
    image = Image.open(io.BytesIO(image))

    if dogDetector.detect(image=image):
        bot.send_message(chat_id=update.message.chat_id,
                     text='This is a dog')
    elif humanDetector.detect('input.jpg'):
        bot.send_message(chat_id=update.message.chat_id,
                     text='This is a person')
    else:
        bot.send_message(chat_id=update.message.chat_id,
                     text='No dog or person found')


handler = MessageHandler(Filters.photo, 
                         whatBreed)


dispatcher = updater.dispatcher

dispatcher.add_handler(handler)


updater.start_polling()
