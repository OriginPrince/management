#coding=utf-8

#封装分类
class researchClass(object):
    def __init__(self,teamNumber,number,name,des):
        self.number=number
        self.name=name
        self.des=des
        self.teamNumber=teamNumber

    def cout(self):
        print self.name




