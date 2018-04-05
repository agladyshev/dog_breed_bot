import os
import sys
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, BaseFilter, Filters
import logging
import re
import json



from keras.applications.resnet50 import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import tensorflow as tf
import io


def load_model():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    global ResNet50_model
    ResNet50_model = ResNet50(weights="imagenet")
    global graph
    graph = tf.get_default_graph()
    print('load model')


def prepare_image(image, target):

    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    # image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image

def ResNet50_predict_labels(image):
    # returns prediction vector for image located at img_path
    img = prepare_image(image, target=(224, 224))
    return np.argmax(ResNet50_model.predict(img))

### returns "True" if a dog is detected in the image stored at img_path
def detect(image):
    prediction = ResNet50_predict_labels(image)
    print(prediction)
    return ((prediction <= 268) & (prediction >= 151))






# updater = Updater(token=os.environ.get('TOKEN'))
updater = Updater(token='579059922:AAHyb14wI8jf6Qxgx-4QqOyCKj6O_Xw2osQ')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

# dogDetector = DogDetector()

def whatBreed(bot, update):

    bot.getFile(update.message.photo[-1].file_id).download('input.jpg')
    image = open('input.jpg', 'rb')
    image = image.read()
    image = Image.open(io.BytesIO(image))

    global graph
    with graph.as_default():
        is_dog = detect(image)
    print(is_dog)
  



    bot.send_message(chat_id=update.message.chat_id,
                     text=str(is_dog))

handler = MessageHandler(Filters.photo, 
                         whatBreed)

load_model()

dispatcher = updater.dispatcher

dispatcher.add_handler(handler)


updater.start_polling()
