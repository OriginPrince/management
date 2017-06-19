#coding=utf-8

#导师和研究员类,需要对照片的路径进行重新封装
class rePerson(object):
    def __init__(self,number,teamNumber,picture,name,phone,qqnumber,describe,className):
        self.number=number
        self.teamNumber=teamNumber
        self.picture=picture
        self.name=name
        self.phone=phone
        self.qqnumber = qqnumber
        self.describe = describe
        self.name = name
        self.className = className

    def cout(self):
        print "bean  "+self.phone


