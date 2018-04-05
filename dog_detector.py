from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from helpers import image_to_tensor

import logging

class DogDetector:
    def __init__(self):
        self.ResNet50_model = ResNet50(weights='imagenet')
        logging.info('Initialize dog detector')

    def ResNet50_predict_labels(image):
        # returns prediction vector for image located at img_path
        img = preprocess_input(image_to_tensor(image))
        return np.argmax(self.ResNet50_model.predict(img))

    ### returns "True" if a dog is detected in the image stored at img_path
    def detect(image):
        logging.info('process image')
        prediction = ResNet50_predict_labels(image)
        return ((prediction <= 268) & (prediction >= 151))