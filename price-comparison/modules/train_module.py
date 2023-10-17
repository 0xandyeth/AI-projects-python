#train_module.py
#import standard library
import numpy as np
import requests
import io
# import tensorflow library
import tensorflow as tf
import pandas as pd
from PIL import Image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input,decode_predictions
from scipy.spatial import distance
from load_module import LoadFile

class Train:
    brand_data=None
    model = None
    image = None
    def __init__(self,csvpath):
        # self.model = tf.keras.models.load_model(csvpath)
        self.brand_data = pd.read_csv(csvpath)
        self.model = MobileNetV2(input_shape=(224,224,3),include_top=False,weights='imagenet')
        self.image = Image.open("./assets/sample.png")
        self.image = self.image.convert("RGB")
     
    def on_train(self):

        user_image_feature = self.recognize_image(self.image)
        close_brand = self.find_closes_brand(user_image_feature)
        return close_brand
    def recognize_image(self,image):
        # if self.loadFile != None and self.model !=None:
            # image = self.loadFile.image
        if self.image != None:
            image = image.resize((224,224),3)
            # image_array = np.array(image)
            # image_array = image_array /255.0
            image = np.expand_dims(image,axis=0)
            image = preprocess_input(image)

            predictions = self.model.predict(image)

            decoded_predictions = decode_predictions(predictions,top=1)[0]

            # predictions = custom_predict(image_array,self.model)
            # results = self.custom_process_predictions(predictions)

            label = decoded_predictions[0][1]
        return label  
        # return results
        # print("recognize")
    def find_closes_brand(self, user_image_feature):
        close_brand = None
        close_distance = float('inf')
        for index,row in self.brand_data.iterrows():
            image_url = row['image_url']

            #Download the image from the url
            image_data = requests.get(image_url).content
            image = Image.open(io.BytesIO((image_data)))

            #Extract feature from the brand image
            brand_image_features = self.recognize_image(image)

            dist = distance.euclidean(user_image_feature, brand_image_features)

            if dist < close_distance:
                self.close_distance = dist
                close_brand = row['category']
        return close_brand

    def custom_predict(self,image,model):
        #implement custom prediction logic
        # Thi should involve applying the loaded weights and layers to the input image
        # and returning the predictions
        
        # assuming your csv file contains weights for a feedforward neural network
        input_size = 224 * 224 # adjust the size based on your input image size
        hidden_layer_size = 128 # adjust based on your model's architecture

        # load the weights from the model data
        weights 
        print("")

    def custom_process_predictions(self,predictions):
        #implement custom logic to process predictions and return results
        decoded_predictions = decoded_predictions(predictions,top=3)[0]

        results =[(label,label_description,score) for (_, label,label_description,score) in decoded_predictions]

        return results
    

