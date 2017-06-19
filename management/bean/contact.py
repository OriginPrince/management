#coding=utf-8

#封装交流活动类
class contact(object):
    def __init__(self,title,content,realContent,author,time):
        self.title=title
        self.content=content
        self.realContent=realContent
        self.author=author
        self.time=time

    def cout(self):
        print self.title+self.author+self.content+self.time


