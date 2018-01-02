import math
from flask import Flask
from flask import request
import json
from keras.models import model_from_json
from sklearn.preprocessing import MinMaxScaler
from keras.layers.noise import GaussianNoise
import numpy as np



app = Flask(__name__)



def load_model():
        global model
        with open('lsci_cars.json', 'r') as json_file:

                print("file loaded")
                loaded_model_json = json_file.read()
                print("loading model")
                model = model_from_json(loaded_model_json)
                print("model loaded")
                model.load_weights("lsci_cars.h5")
                print("Loaded model from disk")
                json_file.close()





 
@app.route("/predictprice")
def preictprice():
    global model
    
# Year                                 
# Engine HP                            
# Engine Cylinders                     
# Number of Doors                      
# Popularity                           
# MSRP                                 
# Vehicle Size_Compact                 
# Vehicle Size_Large                   
# Vehicle Size_Midsize                 
# Vehicle Style_2dr Hatchback          
# Vehicle Style_2dr SUV                
# Vehicle Style_4dr Hatchback          
# Vehicle Style_4dr SUV                
# Vehicle Style_Cargo Minivan          
# Vehicle Style_Cargo Van              
# Vehicle Style_Convertible            
# Vehicle Style_Convertible SUV        
# Vehicle Style_Coupe                  
# Vehicle Style_Crew Cab Pickup        
# Vehicle Style_Extended Cab Pickup    
# Vehicle Style_Passenger Minivan      
# Vehicle Style_Passenger Van          
# Vehicle Style_Regular Cab Pickup     
# Vehicle Style_Sedan                  
# Vehicle Style_Wagon                  
# Driven_Wheels_all wheel drive        
# Driven_Wheels_four wheel drive       
# Driven_Wheels_front wheel drive      
# Driven_Wheels_rear wheel drive       
# Country_England                      
# Country_Germany                      
# Country_Great Britain                
# Country_Italy                        
# Country_Japan                        
# Country_S. Korea                     
# Country_Sweden                       
# Country_USA                          
# Market_luxury                        
# Market_luxury sport                  
# Market_mainstream                    
# Market_midrange                      
    
    year = 2018 - year
    
    
    
    return model.predict(inputVector)


@app.route("/")
def test():
    f = open('demo4.html', 'r')
    return f.read()
    
if __name__ == '__main__':
    #load_model()
    app.run(host='0.0.0.0')
            

