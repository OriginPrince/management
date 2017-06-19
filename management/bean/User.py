#coding=utf-8

#用于显示列表的用户类，
class User(object):
    def __init__(self,number,status,name,phone,teamNumber):
        self.number=number
        self.status=status
        self.name=name
        self.phone=phone
        self.teamNumber = teamNumber

#显示用户更新信息的用户类
class UserUpdate(object):
    def __init__(self,number,pwd,status,name,phone,teamNumber):
        self.number = number
        self.pwd=pwd
        self.status = status
        self.name = name
        self.phone = phone
        self.teamNumber = teamNumber

