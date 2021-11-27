
from flask import Flask, request, json
import Data
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/user',methods = ['POST'])
def set_user():
    request_data = request.json
    user_data = Data.User(request_data)
    #mongodb 
    return {
        "msg" : "success"
    }

@app.route('/user',methods = ['GET'])
def get_user():
    data = None # 
    user_data = None
    userId = request.args.get("id")
    #resend
    #data from mongo

    return {
        "msg" : "success",
        "user" : json.dumps()
        "data" : data
    }



if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)