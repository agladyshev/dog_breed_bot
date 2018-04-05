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
from breed_classifier import BreedClassifier


updater = Updater(token=os.environ.get('TOKEN'))

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

dogDetector = DogDetector()
humanDetector = HumanDetector()
breedClassifier = BreedClassifier()
img_path = 'input.jpg'

def whatBreed(bot, update):
    bot.getFile(update.message.photo[-1].file_id).download(img_path)
    image = open(img_path, 'rb')
    image = image.read()
    image = Image.open(io.BytesIO(image))

    if dogDetector.detect(image=image):
        bot.send_message(chat_id=update.message.chat_id,
                     text='This dog looks like {}'.format(breedClassifier.predict_breed(img_path)))
    elif humanDetector.detect('input.jpg'):
        bot.send_message(chat_id=update.message.chat_id,
                     text='This person looks like {}'.format(breedClassifier.predict_breed(img_path)))
    else:
        bot.send_message(chat_id=update.message.chat_id,
                     text='No dog or person found')

handler = MessageHandler(Filters.photo, 
                         whatBreed)

dispatcher = updater.dispatcher

dispatcher.add_handler(handler)

updater.start_polling()
