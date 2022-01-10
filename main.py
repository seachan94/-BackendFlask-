
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
        "msg" : "SUCCESS"
    }

@app.route('/user',methods = ['GET'])
def get_user():
    id = request.args.get("id")
    usertype = request.args.get("type")
    datas = list(db.User.find({"id":id}))

    dic = {}
    for key in datas[0]:
        dic[key] = datas[0][key]
    
    CurrentUser.user = Data.User(dic)


    if(usertype != CurrentUser.user.userType):
        return {"result" : "TYPE DOESN'T CORRECT"}

    return { "result" : "SUCCESS","data" : json.loads(CurrentUser.user.toJSON()) }


@app.route('/user/duplicate/id', methods =['GET'])
def checkIsDuplicateId():
    
    id = request.args.get("id")
    isDuplicate = len(list(db.User.find({"id":id}))) != 0

    result = ""
    if not isDuplicate :
        result = "SUCCESS"
    
    return {"msg" : result}

@app.route('/user/duplicate/nickname', methods =['GET'])
def checkIsDuplicateNickName():
    
    nickname = request.args.get("nickname")
    isDuplicate = len(list(db.User.find({"nickname":nickname}))) != 0

    result = ""
    if not isDuplicate :
        result = "SUCCESS"
    
    return {"msg" : result}


@app.route('/articles',methods = ['GET'])
def get_articles():
    id = request.args.get("id")
    datas = list(db.User.find({"id":id}))[0]
    writers = datas["describeWriter"]
    get_article = []

    for writer in writers:
        writerInfoFromDb = list(db.User.find({"id":writer}))
        if len(writerInfoFromDb)== 0:
            continue
        writerInfo = list(db.User.find({"id":writer}))[0]
        writerArticle = list(db.Articles.find({"writerId":writer}))
        for data in writerArticle:
            article_dic = {}
            article_dic["writerId"] = data["writerId"]
            article_dic["title"] = data["title"]
            article_dic["text"] = data['text']
            article_dic["date"] = data["date"]
            article_dic["time"] = data["time"]
            
            dic = {}
            dic['Img'] = writerInfo["Img"]
            dic['nickName'] = writerInfo["nickname"]
           
            dic['article'] = json.loads(Data.Article(article_dic).toJSON())

            combine_data = json.loads(Data.WritersArticle(dic).toJSON())
            get_article.append(combine_data)
      

    return { "msg" : "SUCCESS","data" : get_article }
    

@app.route('/describe-writer',methods = ['GET'])
def get_describewriter():
    id = request.args.get("id")
    datas = list(db.User.find({"id":id}))[0]
    
    writers = datas["describeWriter"]
    
    get_writer = []
    
    for writer in writers:
        writerFromDb = list(db.User.find({"id":writer}))
        if len(writerFromDb) == 0:
            continue
        writerInfo = writerFromDb[0]
        get_writer.append(json.loads(Data.User(writerInfo).toJSON()))
   
    return { "msg" : "SUCCESS","data" : get_writer }

@app.route('/recommend-writer',methods = ['GET'])
def get_recommendwriter():
    id = request.args.get("id")
    datas = list(db.User.find({"id":id}))[0]
    
    writers = datas["describeWriter"]
    get_writers = list(db.User.find({"$and" :[ {'id':{'$nin':writers} },
                                    {'userType':'1'} ]}).limit(20))
    
    return_data = []
    for writer in get_writers:
        return_data.append(json.loads(Data.User(writer).toJSON()))

    print(return_data)
    return { "msg" : "SUCCESS","data" : return_data }


@app.route('/introuduceText', methods= ['GET'])
def change_introduceText():
    id = request.args.get("id")
    text = request.args.get("text")

    db.User.update_one({"id":id},{"$set" : {"introduceText": text}})
    
    return {"msg":"SUCCESS"}

@app.route('/Img', methods= ['GET'])
def change_profileImg():
    id = request.args.get("id")
    img = request.args.get("img")

    db.User.update_one({"id":id},{"$set" : {"Img": img}})
    
    return {"msg":"SUCCESS"}

@app.route('/get-article',methods = ['GET'])
def getArticles():
    id = request.args.get("id")


    writerInfo = list(db.User.find({"id":id}))[0]
    writerArticle = list(db.Articles.find({"writerId":id}))

    get_articles = []
    for data in writerArticle:
        article_dic = {}
        article_dic["writerId"] = data["writerId"]
        article_dic["title"] = data["title"]
        article_dic["text"] = data['text']
        article_dic["date"] = data["date"]
        article_dic["time"] = data["time"]
        
        dic = {}
        dic['Img'] = writerInfo["Img"]
        dic['nickName'] = writerInfo["nickname"]
        
        dic['article'] = json.loads(Data.Article(article_dic).toJSON())

        combine_data = json.loads(Data.WritersArticle(dic).toJSON())
        get_articles.append(combine_data)


    return {"msg" : "SUCCESS" , "data" : get_articles}


@app.route("/article",methods = ["DELETE"])
def deleterticle():

    id = request.args.get("id")
    text = request.args.get("text")
    
    db.Articles.delete_one({"text":text,'writerId':id})

    return {"msg" : "SUCCESS"}


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)
    