#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render
import management.bean.User
from django.views.decorators.csrf import csrf_exempt
import management.tools.MD5 as MD5
import json
from management.models import user,team


def userAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username=request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        print "用户",username
        if username:
            team1=team.objects.all()
            return render(request, 'user/userAdd.html', {'username': username,'userstatus': userstatus,'userteam': userteam,'teamList':team1})
    else:
        return render(request, 'user/userAdd.html')

#渲染模板
def userUpdate(request):
    #判断username是否存在session中
    if request.GET:
        number = request.GET['number']
        pwd = request.GET['pwd']
        status = request.GET['status']
        phone = request.GET['phone']
        name = request.GET['name']
        teamNumber = request.GET['teamNumber']
        print "渲染",number+pwd+status+phone+name
        person=management.bean.User.UserUpdate(number,pwd,status,name,phone,teamNumber)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            if username:
                team1 = team.objects.all()
                return render(request, 'user/userUpdate.html', {'username': username,'userstatus': userstatus, 'userteam':userteam,'person':person,'teamList':team1})
    else:
        return render(request, 'user/userUpdate.html')

def userList(request):
    if "username" in request.session:
        username=request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        personList = []
        print userstatus
        if userstatus==0:
            list=user.objects.all()
            if list.exists():
                for i in list:
                    person = management.bean.User.User(pc.decrypt(i.number), i.status, i.name, pc.decrypt(i.phone),
                                                       i.teamNumber)
                    personList.append(person)
                print "person", personList

                return render(request, 'user/userList.html',
                              {'username': username, 'userstatus': userstatus, 'userteam': userteam,
                               'personList': personList})
        elif userstatus==1:
            list=user.objects.filter(teamNumber=userteam)
            if list.exists():
                for i in list:
                    person = management.bean.User.User(pc.decrypt(i.number), i.status, i.name, pc.decrypt(i.phone),
                                                       i.teamNumber)
                    personList.append(person)
                print "person", personList

                return render(request, 'user/userList.html',
                              {'username': username, 'userstatus': userstatus, 'userteam': userteam,
                               'personList': personList})


        else:
        #if username:
            return render(request, 'user/userList.html', {'username': username,'userstatus': userstatus,'personList':None})
    else:
        return render(request, 'user/userList.html')

@csrf_exempt
def userAddPost(request):
    if request.POST:
        pc=MD5.prpcrypt('keyskeyskeyskeys')
        name = request.POST['Fname']
        psd = request.POST['Fpsd']
        phone = request.POST['Fphone']
        number = request.POST['Fnumber']
        status = request.POST['Fstatus']
        teamnumber = request.POST['Fteam']
        print name+str(psd)+str(number)+str(status)
        res=user.objects.filter(number=pc.encrypt(number))
        if res.exists():
            return HttpResponse("ID already")
        else:
            user1=user(number=pc.encrypt(number),name=name,phone=pc.encrypt(phone),password=pc.encrypt(psd),status=status,teamNumber=teamnumber)
            user1.save()
            return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

#由前端传过来的number进行查询，获取到该user的全部属性数据，将其封装成一个json对象，返回给前端界面
def userUpdateData(request):
    pc = MD5.prpcrypt('keyskeyskeyskeys')
    if request.GET:
        number=request.GET['Fnumber']
        teamNumber=request.GET['Fteam']
        res=user.objects.get(number=pc.encrypt(number),teamNumber=teamNumber)
        print res
        person = {'number': pc.decrypt(res.number), 'pwd': pc.decrypt(res.password), 'status': res.status,
                  'name': res.name, 'phone': pc.decrypt(res.phone),'teamNumber':res.teamNumber}
        person = json.dumps(person)
        print person
        return HttpResponse(person)
    else:
        return HttpResponse("false")

#修改数据
@csrf_exempt
def userUpdatePost(request):
    if request.POST:
        pc=MD5.prpcrypt('keyskeyskeyskeys')
        name = request.POST['Fname']
        psd = request.POST['Fpsd']
        phone = request.POST['Fphone']
        number = request.POST['Fnumber']
        status = request.POST['Fstatus']
        team = request.POST['Fteam']
        user1=user.objects.get(number=pc.encrypt(number))
        user1.name=name
        user1.password=pc.encrypt(psd)
        user1.status=status
        user1.phone=pc.encrypt(phone)
        user1.teamNumber=team
        user1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def userDel(request):
    #判断username是否存在session中
    if request.GET:
        pc=MD5.prpcrypt('keyskeyskeyskeys')
        number = request.GET['Fnumber']
        user1=user.objects.get(number=pc.encrypt(number))
        user1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            list = user.objects.all()
            personList = []
            if list.exists():
                for i in list:
                    person = management.bean.User.User(pc.decrypt(i.number), i.status, i.name, pc.decrypt(i.phone),i.teamNumber)
                    personList.append(person)
                print "person", personList
                return render(request, 'user/userList.html',{'username': username,'userstatus': userstatus, 'userteam':userteam,'personList': personList})
            else:
                # if username:
                return render(request, 'user/userList.html',{'username': username,'userstatus': userstatus, 'personList': None})
    else:
        return render(request, 'user/userList.html')