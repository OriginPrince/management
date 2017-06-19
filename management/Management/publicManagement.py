#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from HTMLParser import HTMLParser
from management.tools.eliminateHTML import filter_tags

import management.bean.public
from management.models import public
import time

#渲染模板
def publicAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'public/publicAdd.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName})
    else:
        return render(request, 'public/publicAdd.html')


#渲染模板
def publicUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']#带有标签，即带有格式的内容
        realContent = filter_tags(content)#realContent是将内容取出标签后得到的真实的内容
        public1=management.bean.public.public(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'public/publicUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'public':public1})
        else:
            return render(request, 'public/publicUpdate.html', {'public':public1})
    else:
        return render(request, 'public/publicUpdate.html')

#渲染模板
def publicDetail(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']
        p = HTMLParser()
        content = p.unescape(content)#GET获取到的带有标签的内容，标签被转码了，比如空格被转化成了&nbsp；这一步进行解码，content中存储的是带有标签的内容
        realContent = filter_tags(content)#不带有标签的真实的内容
        public1=management.bean.public.public(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'public/publicDetail.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName,'public':public1,"tag":"公告信息"})
        else:
            return render(request, 'public/publicDetail.html', {'public':public1})
    else:
        return render(request, 'public/publicDetail.html')

def publicList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        print "用户",userteam
        list=public.objects.filter(teamNumber=userteam)
        publicList=[]
        if list.exists():
            for i in list:
                p=HTMLParser()
                content=p.unescape(i.content)
                realContent=filter_tags(content)
                public1=management.bean.public.public(i.title,content,realContent,i.author,str(i.time))
                publicList.append(public1)
            return render(request, 'public/publicList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'publicList': publicList})
        else:
            return render(request, 'public/publicList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'publicList':None})
    else:
        return render(request, 'public/publicList.html')

def publicAddGet(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        userteam = request.session['userteam']
        tempTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        public1 = public(title=title, content=content, author=author, time=tempTime,teamNumber=userteam)
        public1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")
#修改数据

def publicUpdatePost(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        tempTime=request.GET['Ftime']
        userteam = request.session['userteam']
        public1 = public.objects.get(time=tempTime,teamNumber=userteam)
        public1.title = title
        public1.content = content
        public1.author = author
        public1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def publicDel(request):
    if request.GET:
        time = request.GET['Ftime']
        userteam = request.session['userteam']
        public1 = public.objects.get(time=time,teamNumber=userteam)
        public1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            list = public.objects.filter(teamNumber=userteam)
            publicList = []
            if list.exists():#如果有数据的话
                for i in list:
                    p = HTMLParser()
                    content = p.unescape(i.content)
                    realContent = filter_tags(content)
                    public1 = management.bean.public.public(i.title, content, realContent, i.author, str(i.time))
                    publicList.append(public1)
                return render(request, 'public/publicList.html',{'username': username,'userstatus': userstatus,'userteamName': userteamName, 'publicList': publicList})
            else:
                return render(request, 'public/publicList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'publicList': None})
        else:
            return render(request, 'public/publicList.html')
    else:
        return render(request, 'public/publicList.html')


def publicNew(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        userteam = request.session['userteam']
        list=public.objects.filter(teamNumber=userteam).order_by('-time')[0:1]#逆向
        publicList = []
        if list.exists():
            for i in list:
                p = HTMLParser()
                content = p.unescape(i.content)
                realContent = filter_tags(content)
                public1 = management.bean.public.public(i.title, content, realContent, i.author, str(i.time))
                publicList.append(public1)
            if username:
                public2=publicList[0]
                print public2.content
                return render(request, 'public/publicDetail.html',
                              {'username': username, 'userstatus': userstatus, 'userteamName': userteamName,
                               'public': public1,"tag":"最新公告"})
        else:
            return render(request, 'public/publicList.html',
                          {'username': username, 'userstatus': userstatus, 'userteamName': userteamName,
                           'publicList': None})
    else:
        return render(request, 'public/publicDetail.html')