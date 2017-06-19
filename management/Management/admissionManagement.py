#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time
from management.models import admission
import os
import management.bean.admission

#渲染模板
def admissionAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'admission/admissionAdd.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName})
    else:
        return render(request, 'admission/admissionAdd.html')

#渲染模板
def admissionUpdate(request):
    #判断username是否存在session中
    if request.GET:
        title = request.GET['Ftitle']
        time = request.GET['Ftime']
        author = request.GET['Fauthor']
        file = request.GET['Ffile']
        admission1=management.bean.admission.admission(title,author,time,file)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            print "用户",username
            if username:
                return render(request, 'admission/admissionUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'admission':admission1})
        else:
            return render(request, 'admission/admissionUpdate.html')
    else:
        return render(request, 'admission/admissionUpdate.html')

#渲染模板
def admissionDel(request):
    #判断username是否存在session中
    if request.GET:
        userteam = request.session['userteam']
        time = request.GET['Ftime']
        admission1=admission.objects.get(time=time,teamNumber=userteam)
        admission1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            userteam = request.session['userteam']
            list = admission.objects.filter(teamNumber=userteam)
            return render(request, 'admission/admissionList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'List': list})
        else:
            return render(request, 'admission/admissionList.html')
    else:
        return render(request, 'admission/admissionList.html')


def admissionList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        list=admission.objects.filter(teamNumber=userteam)
        return render(request, 'admission/admissionList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'List': list})
    else:
        return render(request, 'admission/admissionList.html')


@csrf_exempt
def admissionAddPost(request):
    if request.POST:
        title = request.POST['title']
        author = request.POST['author']
        file=request.FILES['file']
        userteam = request.session['userteam']
        tempTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        admission1 = admission( title=title, author=author, time=tempTime, file=file,teamNumber=userteam)
        admission1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

@csrf_exempt
def admissionUpdatePost(request):
    if request.POST:
        title = request.POST['title']
        author = request.POST['author']
        file=request.FILES['file']
        time=request.POST['time']
        userteam = request.session['userteam']
        admission1 = admission.objects.get(time=time,teamNumber=userteam)
        admission1.title = title
        admission1.author = author
        admission1.file = file
        admission1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def admissionFileDownLoad(request):
    if request.GET:
        file = request.GET['Ffile']
        file_name = os.path.join(os.getcwd(), file)

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