#coding=utf-8

#用于显示今日要闻，将内容和有格式的内容进行了封装
class News(object):
    def __init__(self,title,content,realContent,author,time):
        self.title=title
        self.content=content
        self.realContent=realContent
        self.author=author
        self.time=time

    def cout(self):
        print self.title+self.author+self.content+self.time


