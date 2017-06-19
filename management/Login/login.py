#coding=utf-8
from django.http import HttpResponse
import management.tools.MD5 as MD5
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from management.models import user,team


@csrf_exempt
def login_post(request):
    if request.POST:
        #删除session中的登录信息
        if "username" in request.session:
            del request.session['username']
        if "userstatus" in request.session:
            del request.session['userstatus']
        if "usernumber" in request.session:
            del request.session['usernumber']
        if "userteam" in request.session:
            del request.session['userteam']
        #生成加密信息
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        psd = request.POST['Fpwd']
        number = request.POST['Fnumber']
        #在数据库中查找是否有number和password符合的数据
        res = user.objects.filter(number=pc.encrypt(number), password=pc.encrypt(psd))
        if res.exists():
            #如果有的话，获取该用户的信息添加到session登录信息中
            user1=user.objects.get(number=pc.encrypt(number), password=pc.encrypt(psd))
            request.session['username']=user1.name
            request.session['userstatus']=user1.status
            request.session['usernumber']=pc.decrypt(user1.number)
            request.session['userteam']=user1.teamNumber
            if user1.teamNumber=="os":
                request.session['userteamName'] = "系统管理员"
            else:
                team1=team.objects.get(number=user1.teamNumber)
                request.session['userteamName']=team1.name
            return HttpResponse(user1.status)
        else:
            return HttpResponse('wrong')

    else:
        print "未获取到数据"
        return HttpResponse('NoData')


def logout(request):
    print "登出",request.session['username']
    if "username" in request.session:
        del request.session['username']
    if "userstatus" in request.session:
        del request.session['userstatus']
    if "usernumber" in request.session:
        del request.session['usernumber']
    if "userteam" in request.session:
        del request.session['userteam']
    return render(request, 'login.html')