from keras.applications.resnet50 import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import tensorflow as tf


class DogDetector:
    def __init__(self):
        # global ResNet50_model
        self.ResNet50_model = ResNet50(weights="imagenet")
        # global graph
        self.graph = tf.get_default_graph()
        print('Dog detector ready')

    def prepare_image(self, image, target):

        # if the image mode is not RGB, convert it
        if image.mode != "RGB":
            image = image.convert("RGB")

        # resize the input image and preprocess it
        image = image.resize(target)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        # return the processed image
        return image

    def ResNet50_predict_labels(self, image):
        # returns prediction vector for image located at img_path
        img = self.prepare_image(image, target=(224, 224))
        return np.argmax(self.ResNet50_model.predict(img))

    ### returns "True" if a dog is detected in the image stored at img_path
    def detect(self, image):
        with self.graph.as_default():
            prediction = self.ResNet50_predict_labels(image)
        return ((prediction <= 268) & (prediction >= 151))
