#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render
import management.bean.User
from django.views.decorators.csrf import csrf_exempt
import management.tools.MD5 as MD5
from management.models import user

#渲染模板
def personalInfoUpdate(request):
    if "username" in request.session:
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        usernumber = request.session['usernumber']
        res = user.objects.get(number=pc.encrypt(usernumber))
        person = management.bean.User.UserUpdate(pc.decrypt(res.number),pc.decrypt(res.password), res.status, res.name, pc.decrypt(res.phone),res.teamNumber)
        return render(request, 'personalInfo/personalInfoUpdate.html',{'username': username,'userstatus': userstatus,'userteamName': userteamName, 'person': person})
    else:
        return render(request, 'personalInfo/personalInfoUpdate.html')


def personalInfoDetail(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteamName = request.session['userteamName']
        usernumber = request.session['usernumber']
        print "用户", username
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        res=user.objects.get(number=pc.encrypt(usernumber))
        person=management.bean.User.User(pc.decrypt(res.number),res.status,res.name,pc.decrypt(res.phone),res.teamNumber)
        return render(request, 'personalInfo/personalInfoDetail.html', {'username': username,'userstatus': userstatus,'userteamName': userteamName,'person': person})
    else:
        return render(request, 'personalInfo/personalInfoDetail.html')

#修改数据
@csrf_exempt
def personalInfoUpdatePost(request):
    if request.POST:
        pc=MD5.prpcrypt('keyskeyskeyskeys')
        name = request.POST['Fname']
        psd = request.POST['Fpsd']
        phone = request.POST['Fphone']
        number = request.POST['Fnumber']
        user1=user.objects.get(number=pc.encrypt(number))
        user1.name=name
        user1.password=pc.encrypt(psd)
        user1.phone=pc.encrypt(phone)
        user1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")