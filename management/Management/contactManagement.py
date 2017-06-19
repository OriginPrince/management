#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from HTMLParser import HTMLParser
from management.tools.eliminateHTML import filter_tags

import management.bean.contact
from management.models import contact
import time

#渲染模板
def contactAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'contact/contactAdd.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName})
    else:
        return render(request, 'contact/contactAdd.html')

#渲染模板
def contactUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']#带有标签，即带有格式的内容
        realContent = filter_tags(content)#realContent是将内容取出标签后得到的真实的内容
        contact1=management.bean.contact.contact(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'contact/contactUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'contact':contact1})
        else:
            return render(request, 'contact/contactUpdate.html', {'contact':contact1})
    else:
        return render(request, 'contact/contactUpdate.html')

#渲染模板
def contactDetail(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']
        p = HTMLParser()
        content = p.unescape(content)#GET获取到的带有标签的内容，标签被转码了，比如空格被转化成了&nbsp；这一步进行解码，content中存储的是带有标签的内容
        realContent = filter_tags(content)#不带有标签的真实的内容
        contact1=management.bean.contact.contact(title,content,realContent,author,time)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'contact/contactDetail.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName,'contact':contact1})
        else:
            return render(request, 'contact/contactDetail.html', {'contact':contact1})
    else:
        return render(request, 'contact/contactDetail.html')

def contactList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        print "用户",userteam
        list=contact.objects.filter(teamNumber=userteam)
        contactList=[]
        if list.exists():
            for i in list:
                p=HTMLParser()
                content=p.unescape(i.content)
                realContent=filter_tags(content)
                contact1=management.bean.contact.contact(i.title,content,realContent,i.author,str(i.time))
                contactList.append(contact1)
            return render(request, 'contact/contactList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'contactList': contactList})
        else:
            return render(request, 'contact/contactList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'contactList':None})
    else:
        return render(request, 'contact/contactList.html')

def contactAddGet(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        userteam = request.session['userteam']
        tempTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        contact1 = contact(title=title, content=content, author=author, time=tempTime,teamNumber=userteam)
        contact1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")


#修改数据

def contactUpdatePost(request):
    if request.GET:
        title = request.GET['Ftitle']
        content = request.GET['Fcontent']
        author = request.GET['Fauthor']
        tempTime=request.GET['Ftime']
        userteam = request.session['userteam']
        contact1 = contact.objects.get(time=tempTime,teamNumber=userteam)
        contact1.title = title
        contact1.content = content
        contact1.author = author
        contact1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def contactDel(request):
    if request.GET:
        time = request.GET['Ftime']
        userteam = request.session['userteam']
        contact1 = contact.objects.get(time=time,teamNumber=userteam)
        contact1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            list = contact.objects.filter(teamNumber=userteam)
            contactList = []
            if list.exists():#如果有数据的话
                for i in list:
                    p = HTMLParser()
                    content = p.unescape(i.content)
                    realContent = filter_tags(content)
                    contact1 = management.bean.contact.contact(i.title, content, realContent, i.author, str(i.time))
                    contactList.append(contact1)
                return render(request, 'contact/contactList.html',{'username': username,'userstatus': userstatus,'userteamName': userteamName, 'contactList': contactList})
            else:
                return render(request, 'contact/contactList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'contactList': None})
        else:
            return render(request, 'contact/contactList.html')
    else:
        return render(request, 'contact/contactList.html')