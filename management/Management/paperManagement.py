#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time
from management.models import paper
import os
import management.bean.Paper

#渲染模板
def paperAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName=request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'paper/paperAdd.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName})
    else:
        return render(request, 'paper/paperAdd.html')

#渲染模板
def paperUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        content = request.GET['Fcontent']
        number = request.GET['Fnumber']
        file = request.GET['Ffile']
        team = request.session['userteam']
        paper1=management.bean.Paper.Paper(title,content,number,author,time,file,team)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'paper/paperUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'paper':paper1})
        else:
            return render(request, 'paper/paperUpdate.html')
    else:
        return render(request, 'paper/paperUpdate.html')

#渲染模板
def paperDel(request):
    #判断username是否存在session中
    if request.GET:
        number = request.GET['Fnumber']
        team = request.session['userteam']
        paper1=paper.objects.get(number=number,teamNumber=team)
        paper1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            userteamName = request.session['userteamName']
            list = paper.objects.all()
            return render(request, 'paper/paperList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'List': list})
        else:
            return render(request, 'paper/paperList.html')
    else:
        return render(request, 'paper/paperList.html')


def paperList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        list=paper.objects.filter(teamNumber=userteam)
        return render(request, 'paper/paperList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'List': list})
    else:
        return render(request, 'paper/paperList.html')


@csrf_exempt
def paperAddPost(request):
    if request.POST:
        title = request.POST['title']
        number = request.POST['number']
        author = request.POST['author']
        file=request.FILES['file']#以这种方式获取文件
        content=request.POST['content']
        teamNumber = request.session['userteam']
        res = paper.objects.filter(number=number,teamNumber=teamNumber)
        if res.exists():
            return HttpResponse("ID already")
        else:
            tempTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            paper1=paper(number=number,title=title,author=author,time=tempTime,file=file,content=content,teamNumber=teamNumber)
            paper1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

@csrf_exempt
def paperUpdatePost(request):
    if request.POST:
        title = request.POST['title']
        number = request.POST['number']
        author = request.POST['author']
        file=request.FILES['file']
        content=request.POST['content']
        teamNumber = request.session['userteam']
        paper1 = paper.objects.get(number=number,teamNumber=teamNumber)
        paper1.title = title
        paper1.content = content
        paper1.author = author
        paper1.file=file
        paper1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def paperFileDownLoad(request):
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