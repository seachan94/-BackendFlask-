class User:
    
    UserId = None
    UserName = None
    UserNickName = None
    IntroduceText = None
    UserProfileImgUrl = None
    UserType = None
    DescribeWriter = None

    def __init__(self,userid= None,username = None,usernickname = None,intro = None,img = None,type = None,writer = None):
        self.UserId = userid
        self.UserName = username
        self.UserNickName = usernickname
        self.IntroduceText = intro
        self.UserProfileImgUrl = img
        self.UserType = type
        self.DescribeWriter = writer
    

class Article:

    WriterId = None
    TextTitle = None
    Text = None
    Date = None

    def __init__(self,id= None,title = None,text = None,date = None):
        self.WriterId = id
        self.TextTitle = text
        self.title = title
        self.Date = date

