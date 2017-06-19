#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from HTMLParser import HTMLParser
from management.tools.eliminateHTML import filter_tags

import management.bean.News
from management.models import news
import time

#渲染模板
def newsAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'news/newsAdd.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName})
    else:
        return render(request, 'news/newsAdd.html')

#渲染模板
def newsUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']#带有标签，即带有格式的内容
        realContent = filter_tags(content)#realContent是将内容取出标签后得到的真实的内容
        news1=management.bean.News.News(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'news/newsUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'news':news1})
        else:
            return render(request, 'news/newsUpdate.html', {'news':news1})
    else:
        return render(request, 'news/newsUpdate.html')

#渲染模板
def newsDetail(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']
        p = HTMLParser()
        content = p.unescape(content)#GET获取到的带有标签的内容，标签被转码了，比如空格被转化成了&nbsp；这一步进行解码，content中存储的是带有标签的内容
        realContent = filter_tags(content)#不带有标签的真实的内容
        news1=management.bean.News.News(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'news/newsDetail.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName,'news':news1})
        else:
            return render(request, 'news/newsDetail.html', {'news':news1})
    else:
        return render(request, 'news/newsDetail.html')

def newsList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        print "用户",userteam
        list=news.objects.filter(teamNumber=userteam)
        newsList=[]
        if list.exists():
            for i in list:
                p=HTMLParser()
                content=p.unescape(i.content)
                realContent=filter_tags(content)
                news1=management.bean.News.News(i.title,content,realContent,i.author,str(i.time))
                newsList.append(news1)
            return render(request, 'news/newsList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'newsList': newsList})
        else:
            return render(request, 'news/newsList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'newsList':None})
    else:
        return render(request, 'news/newsList.html')

def newsAddGet(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        userteam = request.session['userteam']
        tempTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        news1 = news(title=title, content=content, author=author, time=tempTime,teamNumber=userteam)
        news1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")


#修改数据

def newsUpdatePost(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        tempTime=request.GET['Ftime']
        userteam = request.session['userteam']
        news1 = news.objects.get(time=tempTime,teamNumber=userteam)
        news1.title = title
        news1.content = content
        news1.author = author
        news1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def newsDel(request):
    if request.GET:
        time = request.GET['Ftime']
        userteam = request.session['userteam']
        news1 = news.objects.get(time=time,teamNumber=userteam)
        news1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            list = news.objects.filter(teamNumber=userteam)
            newsList = []
            if list.exists():#如果有数据的话
                for i in list:
                    p = HTMLParser()
                    content = p.unescape(i.content)
                    realContent = filter_tags(content)
                    news1 = management.bean.News.News(i.title, content, realContent, i.author, str(i.time))
                    newsList.append(news1)
                return render(request, 'news/newsList.html',{'username': username,'userstatus': userstatus,'userteamName': userteamName, 'newsList': newsList})
            else:
                return render(request, 'news/newsList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'newsList': None})
        else:
            return render(request, 'news/newsList.html')
    else:
        return render(request, 'news/newsList.html')