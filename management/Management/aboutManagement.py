#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time,json
from management.models import about

#渲染模板
def aboutAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName=request.session['userteamName']
        print "用户",username
        if username:
            return render(request, 'about/aboutAdd.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'userteamName': userteamName})
    else:
        return render(request, 'about/aboutAdd.html')

#渲染模板
def aboutDetail(request):
    if request.GET:
        className = request.GET['FclassName']
        #判断username是否存在session中
        userteam = request.session['userteam']
        about1=about.objects.get(teamNumber=userteam,className=className)
        about2={"className":about1.className,"author":about1.author,"content":about1.content}
        about3=json.dumps(about2)
        return HttpResponse(about3)
    else:
        return HttpResponse("false")

#渲染模板
def aboutUpdate(request):
    className = request.GET['FclassName']
    #判断username是否存在session中
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        userteam = request.session['userteam']
        about1 = about.objects.get(teamNumber=userteam,className=className)
        print "用户", username
        if username:
            return render(request, 'about/aboutUpdate.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'about': about1})
    else:
        return render(request, 'about/aboutUpdate.html')

@csrf_exempt
def aboutAddPost(request):
    if request.POST:
        className = request.POST['className']
        author = request.POST['author']
        content=request.POST['content']
        userteam = request.session['userteam']
        tempTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        about1 = about(author=author, time=tempTime, content=content,teamNumber=userteam,className=className)
        about1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

@csrf_exempt
def aboutUpdatePost(request):
    if request.POST:
        className = request.POST['className']
        author = request.POST['author']
        content = request.POST['content']
        userteam = request.session['userteam']
        time=request.POST['time']
        about1 = about.objects.get(teamNumber=userteam,time=time)
        about1.className = className
        about1.author = author
        about1.content = content
        about1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")


def aboutList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        userteamName = request.session['userteamName']
        teamNumber = userteam
        list = about.objects.filter(teamNumber=teamNumber)
        return render(request, 'about/aboutList.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName, 'List': list})
    else:
        return render(request, 'about/aboutList.html')


#渲染模板
def aboutDel(request):
    className = request.GET['FclassName']
    #判断username是否存在session中
    if request.GET:
        userteam = request.session['userteam']
        about1=about.objects.get(teamNumber=userteam,className=className)
        about1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteamName = request.session['userteamName']
            list = about.objects.filter(teamNumber=userteam)
            return render(request, 'about/aboutList.html',
                          {'username': username, 'userstatus': userstatus, 'userteamName': userteamName, 'List': list})
        else:
            return render(request, 'about/aboutList.html')
    else:
        return render(request, 'about/aboutList.html')
