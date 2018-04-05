from extract_bottleneck_features import extract_InceptionV3
from helpers import path_to_tensor
from keras.layers import GlobalAveragePooling2D
from keras.layers import Dense
from keras.models import Sequential
import tensorflow as tf
import numpy as np
from dog_names import dog_names 


class BreedClassifier:
    def __init__(self):
        self.InceptionV3_model = Sequential()
        self.InceptionV3_model.add(GlobalAveragePooling2D(input_shape=(5, 5, 2048)))
        self.InceptionV3_model.add(Dense(133, activation='softmax'))
        self.InceptionV3_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        self.InceptionV3_model.load_weights('saved_models/weights.best.InceptionV3.hdf5')
        self.InceptionV3_model._make_predict_function()
        self.graph = tf.get_default_graph()

        print('Breed classifier ready')

    def predict_breed(self, img_path):
        with self.graph.as_default():
            bottleneck_feature = extract_InceptionV3(path_to_tensor(img_path))
            predicted_vector = self.InceptionV3_model.predict(bottleneck_feature)
        return ' '.join(dog_names[np.argmax(predicted_vector)].lower().split('_'))
