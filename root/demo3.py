from flask import Flask
from flask import jsonify
import random


app = Flask(__name__)



 
@app.route("/getcar")
def getcar():
    cars = ['DeLorean DMC-12', '1946 Ford Super De Luxe', 'Toyota Xtra Cab 4x4', 'BMW 733i', 'Volkswagen Bus']
    return jsonify(random.choice(cars))


@app.route("/")
def test():
    f = open('demo3.html', 'r')
    return f.read()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
            

