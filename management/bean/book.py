#coding=utf-8

#封装专著类
class book(object):
    def __init__(self,title,content,number,author,time,file,teamNumber):
        self.title=title
        self.content=content
        self.number=number
        self.author=author
        self.time=time
        self.file = file
        self.teamNumber = teamNumber


