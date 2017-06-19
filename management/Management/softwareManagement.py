#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time
from management.models import software
import os
import management.bean.software

#渲染模板
def softwareAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName=request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'software/softwareAdd.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName})
    else:
        return render(request, 'software/softwareAdd.html')

#渲染模板
def softwareUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']
        number = request.GET['Fnumber']
        file = request.GET['Ffile']
        team = request.session['userteam']
        software1=management.bean.software.software(title,content,number,author,time,file,team)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'software/softwareUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'software':software1})
        else:
            return render(request, 'software/softwareUpdate.html')
    else:
        return render(request, 'software/softwareUpdate.html')

#渲染模板
def softwareDel(request):
    #判断username是否存在session中
    if request.GET:
        number = request.GET['Fnumber']
        team = request.session['userteam']
        software1=software.objects.get(number=number,teamNumber=team)
        software1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            list = software.objects.all()
            return render(request, 'software/softwareList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'List': list})
        else:
            return render(request, 'software/softwareList.html')
    else:
        return render(request, 'software/softwareList.html')


def softwareList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        list = software.objects.filter(teamNumber=userteam)
        return render(request, 'software/softwareList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'List': list})
    else:
        return render(request, 'software/softwareList.html')


@csrf_exempt
def softwareAddPost(request):
    if request.POST:
        title = request.POST['title']
        number = request.POST['number']
        author = request.POST['author']
        file=request.FILES['file']#以这种方式获取文件
        content=request.POST['content']
        teamNumber = request.session['userteam']
        res = software.objects.filter(number=number,teamNumber=teamNumber)
        if res.exists():
            return HttpResponse("ID already")
        else:
            tempTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            software1=software(number=number,title=title,author=author,time=tempTime,file=file,content=content,teamNumber=teamNumber)
            software1.save()
        return HttpResponse("true")
    else:
        return HttpResponse("no data")

@csrf_exempt
def softwareUpdatePost(request):
    if request.POST:
        title = request.POST['title']
        number = request.POST['number']
        author = request.POST['author']
        file=request.FILES['file']
        content=request.POST['content']
        teamNumber = request.session['userteam']
        software1 = software.objects.get(number=number,teamNumber=teamNumber)
        software1.title = title
        software1.content = content
        software1.author = author
        software1.file=file
        software1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def softwareFileDownLoad(request):
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