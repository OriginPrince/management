#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from HTMLParser import HTMLParser
from management.tools.eliminateHTML import filter_tags

import management.bean.coordinate
from management.models import coordinate
import time

#渲染模板
def coordinateAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'coordinate/coordinateAdd.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName})
    else:
        return render(request, 'coordinate/coordinateAdd.html')

#渲染模板
def coordinateUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']#带有标签，即带有格式的内容
        realContent = filter_tags(content)#realContent是将内容取出标签后得到的真实的内容
        coordinate1=management.bean.coordinate.coordinate(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'coordinate/coordinateUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'coordinate':coordinate1})
        else:
            return render(request, 'coordinate/coordinateUpdate.html', {'coordinate':coordinate1})
    else:
        return render(request, 'coordinate/coordinateUpdate.html')

#渲染模板
def coordinateDetail(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']
        p = HTMLParser()
        content = p.unescape(content)#GET获取到的带有标签的内容，标签被转码了，比如空格被转化成了&nbsp；这一步进行解码，content中存储的是带有标签的内容
        realContent = filter_tags(content)#不带有标签的真实的内容
        coordinate1=management.bean.coordinate.coordinate(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'coordinate/coordinateDetail.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName,'coordinate':coordinate1})
        else:
            return render(request, 'coordinate/coordinateDetail.html', {'coordinate':coordinate1})
    else:
        return render(request, 'coordinate/coordinateDetail.html')

def coordinateList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        print "用户",userteam
        list=coordinate.objects.filter(teamNumber=userteam)
        coordinateList=[]
        if list.exists():
            for i in list:
                p=HTMLParser()
                content=p.unescape(i.content)
                realContent=filter_tags(content)
                coordinate1=management.bean.coordinate.coordinate(i.title,content,realContent,i.author,str(i.time))
                coordinateList.append(coordinate1)
            return render(request, 'coordinate/coordinateList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'coordinateList': coordinateList})
        else:
            return render(request, 'coordinate/coordinateList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'coordinateList':None})
    else:
        return render(request, 'coordinate/coordinateList.html')

def coordinateAddGet(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        userteam = request.session['userteam']
        tempTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        coordinate1 = coordinate(title=title, content=content, author=author, time=tempTime,teamNumber=userteam)
        coordinate1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")


#修改数据

def coordinateUpdatePost(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        tempTime=request.GET['Ftime']
        userteam = request.session['userteam']
        coordinate1 = coordinate.objects.get(time=tempTime,teamNumber=userteam)
        coordinate1.title = title
        coordinate1.content = content
        coordinate1.author = author
        coordinate1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def coordinateDel(request):
    if request.GET:
        time = request.GET['Ftime']
        userteam = request.session['userteam']
        coordinate1 = coordinate.objects.get(time=time,teamNumber=userteam)
        coordinate1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            list = coordinate.objects.filter(teamNumber=userteam)
            coordinateList = []
            if list.exists():#如果有数据的话
                for i in list:
                    p = HTMLParser()
                    content = p.unescape(i.content)
                    realContent = filter_tags(content)
                    coordinate1 = management.bean.coordinate.coordinate(i.title, content, realContent, i.author, str(i.time))
                    coordinateList.append(coordinate1)
                return render(request, 'coordinate/coordinateList.html',{'username': username,'userstatus': userstatus,'userteamName': userteamName, 'coordinateList': coordinateList})
            else:
                return render(request, 'coordinate/coordinateList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'coordinateList': None})
        else:
            return render(request, 'coordinate/coordinateList.html')
    else:
        return render(request, 'coordinate/coordinateList.html')