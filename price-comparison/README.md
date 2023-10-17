# Price Comparison App #

Goal: 
- The app allows users to upload a picture of item they want to buy. 
- Then , the app will scan through many online stores and find the lowest price for the item
- Finally, the app gives user a link to go to the online store to buy the item through the app.

Principle: Transfer Modeling 
Train new model with previous existing data 

Steps :
- Upload picture (upload module/load image module)
- Identify the picture ( transfer learning) – pre-existing database
Train model (train module)
- Once the model is built, give a choice to specify additional information about item 
- Algorithm that idenfies online store based on provide brand
- Create Automated tool that open sites and scrapes pricing information (tool module)
- Return site name and pricing information to user  

- Train process
   - Data collection
   - Image Recognition model ( pytorch - train a deep learning model for image recognition)
   - App development ( result of recognition)
   - Model Integration
