# load_module.py
#import standard library
import csv
# import extneral library
from PIL import Image
# load a image and csv file
class LoadFile:
    image = None
    pre_trained_data =[]
    def __init__(self):
        print("load file")
    def loadImage(self):
        #open an image file
        self.image = Image.open("./assets/sample.png")
        # format and size
        print(f"{self.image.format},{self.image.size}")
    def showImage(self):
        self.loadImage()
        self.image.show()
    def loadCSV(self):
        #open the csv file
        with open("./assets/dress.csv",newline='') as csvfile:
            #Create a CSV reader object
            csvreader = csv.reader(csvfile)

            #Iterate through the rows in the CSV file
            for i, row in csvreader:
                self.pre_trained_data.insert(i, row)
        return self.pre_trained_data
