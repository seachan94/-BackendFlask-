class User:
    
    UserId = None
    UserName = None
    UserNickName = None
    IntroduceText = None
    UserProfileImgUrl = None
    UserType = None
    DescribeWriter = None

    def __init__(self,data):
        self.UserId = data["userId"]
        self.UserName = data["userName"]
        self.UserNickName = data["userNickname"]
        self.IntroduceText = data["introduceText"]
        self.UserProfileImgUrl = data["img"]
        self.UserType = data["type"]
        self.DescribeWriter = data["descriveWriter"]
    

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
    


