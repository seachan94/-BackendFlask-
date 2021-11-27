
from flask import Flask, request, json
import Data
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('127.0.0.1',27017)

db = client["ReadApp"]

@app.route('/user',methods = ['POST'])
def set_user():
    request_data = request.json

    #mongodb 
    db.User.insert_one(request_data)
    return {
        "msg" : "success"
    }

@app.route('/user',methods = ['GET'])
def get_user():
    id = request.args.get("id")
    datas = list(db.User.find({"userid":id}))
    dic = {}
    for key in datas[0]:
        dic[key] = datas[0][key]
    
    return_data = Data.User(dic)
    return { "result" : "get ok","data" : json.loads(return_data.toJSON()) }
    





if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)