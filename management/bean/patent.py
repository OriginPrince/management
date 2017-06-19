#coding=utf-8

#封装专利成果类
class patent(object):
    def __init__(self,title,content,number,author,time,file,teamNumber):
        self.title=title
        self.content=content
        self.number=number
        self.author=author
        self.time=time
        self.file = file
        self.teamNumber = teamNumber


