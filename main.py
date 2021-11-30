
from flask import Flask, request, json
import Data,CurrentUser
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('127.0.0.1',27017)

db = client["ReadApp"]

global user

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
    usertype = request.args.get("type")
    datas = list(db.User.find({"userid":id}))

    dic = {}
    for key in datas[0]:
        dic[key] = datas[0][key]
    
    CurrentUser.user = Data.User(dic)


    if(usertype != CurrentUser.user.userType):
        return {"result" : "TYPE DOESN'T CORRECT"}

    return { "result" : "SUCCESS","data" : json.loads(CurrentUser.user.toJSON()) }


@app.route('/articles',methods = ['GET'])
def get_articles():
    writers = CurrentUser.user.describeWriter

    get_article = []
    
    for writer in writers:
        writerInfo = list(db.User.find({"userid":writer}))[0]
        writerArticle = list(db.Articles.find({"userid":writer}))
        for data in writerArticle:
            article_dic = {}
            article_dic["writerId"] = data["userid"]
            article_dic["title"] = data["title"]
            article_dic["text"] = data['text']
            article_dic["date"] = data["date"]
            article_dic["time"] = data["time"]
            
            dic = {}
            dic['Img'] = writerInfo["img"]
            dic['nickName'] = writerInfo["nickname"]
            if 'article' in dic.keys():

                dic['article'].append(json.loads(Data.Article(article_dic).toJSON()))
            else:
                dic['article'] = [json.loads(Data.Article(article_dic).toJSON())]

            combine_data = json.loads(Data.WritersArticle(dic).toJSON())
            get_article.append(combine_data)


    return { "result" : "get ok","data" : get_article }
    





if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)
    