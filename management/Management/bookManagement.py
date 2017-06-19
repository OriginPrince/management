#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time
from management.models import book
import os
import management.bean.book

#渲染模板
def bookAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName=request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'book/bookAdd.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'userteamName': userteamName})
    else:
        return render(request, 'book/bookAdd.html')

#渲染模板
def bookUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']
        number = request.GET['Fnumber']
        file = request.GET['Ffile']
        team = request.session['userteam']
        book1=management.bean.book.book(title,content,number,author,time,file,team)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'book/bookUpdate.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'userteamName': userteamName, 'book':book1})
        else:
            return render(request, 'book/bookUpdate.html')
    else:
        return render(request, 'book/bookUpdate.html')

#渲染模板
def bookDel(request):
    #判断username是否存在session中
    if request.GET:
        number = request.GET['Fnumber']
        team = request.session['userteam']
        book1=book.objects.get(number=number,teamNumber=team)
        book1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            userteamName = request.session['userteamName']
            list = book.objects.filter(teamNumber=userteam)
            return render(request, 'book/bookList.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'userteamName': userteamName, 'List': list})
        else:
            return render(request, 'book/bookList.html')
    else:
        return render(request, 'book/bookList.html')


def bookList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        teamNumber = userteam
        list = book.objects.filter(teamNumber=teamNumber)
        return render(request, 'book/bookList.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'userteamName': userteamName, 'List': list})
    else:
        return render(request, 'book/bookList.html')


@csrf_exempt
def bookAddPost(request):
    if request.POST:
        title = request.POST['title']
        number = request.POST['number']
        author = request.POST['author']
        file=request.FILES['file']#以这种方式获取文件
        content=request.POST['content']
        teamNumber = request.session['userteam']
        res = book.objects.filter(number=number,teamNumber=teamNumber)
        if res.exists():
            return HttpResponse("ID already")
        else:
            tempTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            book1=book(number=number,title=title,author=author,time=tempTime,file=file,content=content,teamNumber=teamNumber)
            book1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

@csrf_exempt
def bookUpdatePost(request):
    if request.POST:
        title = request.POST['title']
        number = request.POST['number']
        author = request.POST['author']
        file=request.FILES['file']
        content=request.POST['content']
        teamNumber = request.session['userteam']
        book1 = book.objects.get(number=number,teamNumber=teamNumber)
        book1.title = title
        book1.content = content
        book1.author = author
        book1.file=file
        book1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def bookFileDownLoad(request):
    if request.GET:
        file = request.GET['Ffile']
        file_name = os.path.join(os.getcwd(), file)
        #读取文件
        def readFile(fn, buf_size=512):  # 大文件下载，设定缓存大小
            f = open(fn, "rb")
            while True:  # 循环读取
                c = f.read(buf_size)
                if c:
                    yield c
                else:
                    break
            f.close()
        response = HttpResponse(readFile(file_name),content_type='APPLICATION/OCTET-STREAM')  # 设定文件头，这种设定可以让任意文件都能正确下载，而且已知文本文件不是本地打开
        file_name=file_name.encode('utf-8')
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        #response['Content-Length'] = os.path.getsize(file_name)  # 传输给客户端的文件大小
        return response
    else:
        print "未获取到数据"
        return HttpResponse("no data")