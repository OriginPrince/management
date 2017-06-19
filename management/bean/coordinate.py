#coding=utf-8

#封装合作项目类
class coordinate(object):
    def __init__(self,title,content,realContent,author,time):
        self.title=title
        self.content=content
        self.realContent=realContent
        self.author=author
        self.time=time

    def cout(self):
        print self.title+self.author+self.content+self.time


