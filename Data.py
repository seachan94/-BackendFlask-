import json
class User:


    def __init__(self,data):
        self.UserId = data["userid"]
        self.UserName = data["username"]
        self.UserNickName = data["nickname"]
        self.IntroduceText = data["introducetext"]
        self.UserProfileImgUrl = data["img"]
        self.UserType = data["usertype"]
        self.DescribeWriter = data["describewriter"]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
             indent=4)

class Article:

    WriterId = None
    TextTitle = None
    Text = None
    Date = None
    time= None
    def __init__(self,data):
        self.WriterId = data["id"]
        self.TextTitle = data["text"]
        self.title = data["title"]
        self.Date = data["date"]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
             indent=4)
    


