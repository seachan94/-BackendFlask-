import json
class User:

    def __init__(self,data):
        self.id = data["userid"]
        self.name = data["username"]
        self.nickname = data["nickname"]
        self.introduceText = data["introducetext"]
        self.Img = data["img"]
        self.userType = data["usertype"]
        self.describeWriter = data["describewriter"]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
             indent=4)

class Article:

    def __init__(self,data):
        self.writerId = data["writerId"]
        self.text = data["text"]
        self.title = data["title"]
        self.date = data["date"]
        self.time = data['time']

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
             indent=4)
    
class WritersArticle:

    def __init__(self,data):
        self.Img = data['Img']
        self.nickName = data['nickName']
        self.article = data['article']

    def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__, 
                indent=4)