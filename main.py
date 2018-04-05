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

# updater = Updater(token=os.environ.get('TOKEN'))
updater = Updater(token='579059922:AAHyb14wI8jf6Qxgx-4QqOyCKj6O_Xw2osQ')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

dogDetector = DogDetector()

def whatBreed(bot, update):

    bot.getFile(update.message.photo[-1].file_id).download('input.jpg')
    image = open('input.jpg', 'rb')
    image = image.read()
    image = Image.open(io.BytesIO(image))
    # try:
    #   is_dog = dogDetector.detect(image=image)
    # except:
    #   sys.exit(1)
    is_dog = dogDetector.detect(image=image)
    print(is_dog)
  



    bot.send_message(chat_id=update.message.chat_id,
                     text=str(is_dog))

handler = MessageHandler(Filters.photo, 
                         whatBreed)


dispatcher = updater.dispatcher

dispatcher.add_handler(handler)


updater.start_polling()
