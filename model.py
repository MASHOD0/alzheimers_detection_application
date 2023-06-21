import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os
import cv2
import tensorflow as tf



# input_image_path = os.path.join(os.getcwd(), 'UPLOADS')

# classes = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
# def load_image(image_path):
#     return cv2.imread(image_path)

# def resize_image(image, size):
#     return cv2.resize(image, size)

"""
Import the xceptionmodel.h5 and use it to predict if the image is dimentiated or not
"""

# def predict_image(image):
    # """
    # input : image
    # Import the xceptionmodel.h5 and use it to predict if the image is dimentiated or not
    # """
    # model = tf.keras.models.load_model('xceptionmodel.h5')
    # image = np.expand_dims(image, axis=0)
    # image = image/255.0
    # prediction = model.predict(image, batch_size=1)
    # for i in range(len(classes)):
    #     print(classes[i], ':', prediction[0][i])
    # prediction = classes[np.argmax(prediction)]
    
    # return prediction

def predict_image(image_path):
    """
    input : image
    Import the xceptionmodel.h5 and use it to predict if the image is dimentiated or not
    """
    
    input_image_path = os.path.join(os.getcwd(), image_path)

    classes = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

    def load_image(image_path):
        return cv2.imread(image_path)

    def resize_image(image, size):
        return cv2.resize(image, size)
    image = load_image(input_image_path)
    image = resize_image(image, (224, 224))
    model = tf.keras.models.load_model('xceptionmodel.h5')
    image = np.expand_dims(image, axis=0)
    image = image/255.0
    prediction = model.predict(image, batch_size=1)
    for i in range(len(classes)):
        print(classes[i], ':', prediction[0][i])
    prediction = classes[np.argmax(prediction)]
    
    return prediction
if __name__ == '__main__':

    print(predict_image('UPLOADS/test.jpg'))