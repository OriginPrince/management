#coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import management.tools.MD5 as MD5
import management.bean.rePerson,management.bean.researchClass
from management.models import researchUser,researchClass
import os

#渲染模板
def reUserAdd(request):
    if request.GET:
        teamNumber = request.GET['Fnumber']
    #判断username是否存在session中
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            list = researchClass.objects.filter(teamNumber=teamNumber)
            List = []
            if list.exists():
                for i in list:
                    researchClass1 = management.bean.researchClass.researchClass(teamNumber, i.number, i.name,
                                                                                 i.describe)
                    List.append(researchClass1)
            if username:
                return render(request, 'researchUser/reUserAdd.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'number':teamNumber,'List':List})
        else:
            return render(request, 'researchUser/reUserAdd.html')
    else:
        return render(request, 'researchUser/reUserAdd.html')

def reUserUpdate(request):
    #判断username是否存在session中
    if request.GET:
        name = request.GET['name']
        number = request.GET['number']
        tnumber = request.GET['tnumber']
        des = request.GET['des']
        picture = request.GET['picture']
        FclassNumber = request.GET['FclassNumber']
        qq = request.GET['qq']
        phone = request.GET['phone']
        print FclassNumber
        print "123"
        rePerson1=management.bean.rePerson.rePerson(number,tnumber,picture,name,phone,qq,des,FclassNumber)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            list=researchClass.objects.filter(teamNumber=tnumber)
            List = []
            if list.exists():
                for i in list:
                    researchClass1 = management.bean.researchClass.researchClass(tnumber, i.number, i.name,
                                                                                 i.describe)
                    List.append(researchClass1)
            print "用户",username
            if username:
                return render(request, 'researchUser/reUserUpdate.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'person':rePerson1, 'List':List})
        else:
            return render(request, 'researchUser/reUserUpdate.html')
    else:
        return render(request, 'researchUser/reUserUpdate.html')
#渲染模板
def reUserDetail(request):
    #判断username是否存在session中
    if request.GET:
        name = request.GET['name']
        number = request.GET['number']
        tnumber = request.GET['tnumber']
        des = request.GET['des']
        picture = request.GET['picture']
        FclassName = request.GET['FclassName']
        qq = request.GET['qq']
        phone = request.GET['phone']
        userteam = request.session['userteam']
        rePerson1=management.bean.rePerson.rePerson(number,tnumber,picture,name,phone,qq,des,FclassName)
        res=researchClass.objects.get(name=FclassName,teamNumber=userteam)
        classNumber=res.number
        print classNumber
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户",username
            if username:
                return render(request, 'researchUser/reUserDetail.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'classNumber':classNumber,'person':rePerson1})
        else:
            return render(request, 'researchUser/reUserDetail.html')
    else:
        return render(request, 'researchUser/reUserDetail.html')


def reUserList(request):
    if request.GET:
        pc=MD5.prpcrypt('keyskeyskeyskeys')
        teamNumber=request.GET['Fnumber']
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户",username
            list=researchUser.objects.filter(teamNumber=teamNumber)
            List=[]
            print list.exists()
            if list.exists():
                for i in list:
                    reClass1=researchClass.objects.get(number=i.classNum,teamNumber=userteam)#进行分类名称查询
                    className=reClass1.name
                    picture = os.path.join("/", str(i.picture))
                    print pc.decrypt(i.phone)
                    person1=management.bean.rePerson.rePerson(pc.decrypt(i.number),i.teamNumber,picture,i.name,pc.decrypt(i.phone),pc.decrypt(i.qqnumber),i.describe,className)
                    List.append(person1)
                    person1.cout()
                return render(request, 'researchUser/reUserList.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'number':teamNumber, 'List': List})
            else:
                return render(request, 'researchUser/reUserList.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'number':teamNumber, 'List':None})
        else:
            return render(request, 'researchUser/reUserList.html')
    else:
        return render(request, 'researchUser/reUserList.html')


@csrf_exempt
def reUserAddPost(request):
    print "123"
    if request.POST:
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        name = request.POST['name']
        number = request.POST['number']
        tnumber = request.POST['tnumber']
        des = request.POST['des']
        qq = request.POST['qq']
        Fclass = request.POST['Fclass']
        file=request.FILES['file']
        phone=request.POST['phone']
        res=researchUser.objects.filter(teamNumber=tnumber,number=pc.encrypt(number))
        if res.exists():
            return HttpResponse("ID already")
        else:
            reUser1 = researchUser(teamNumber=tnumber, number=pc.encrypt(number), name=name, describe=des,
                                         qqnumber=pc.encrypt(qq), classNum=Fclass, picture=file,
                                         phone=pc.encrypt(phone))
            reUser1.save()
            return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")


@csrf_exempt
def reUserUpdatePost(request):
    print "123"
    if request.POST:
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        name = request.POST['name']
        number = request.POST['number']
        des = request.POST['des']
        qq = request.POST['qq']
        Fclass = request.POST['Fclass']
        file=request.FILES['file']
        phone=request.POST['phone']
        userteam = request.session['userteam']
        reUser1=researchUser.objects.get(number=pc.encrypt(number),teamNumber=userteam)
        reUser1.name=name
        reUser1.describe=des
        reUser1.qqnumber=pc.encrypt(qq)
        reUser1.classNum=Fclass
        reUser1.picture=file
        reUser1.phone=pc.encrypt(phone)
        reUser1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def reUserDelPost(request):
    if request.GET:
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        number = request.GET['Fnumber']
        teamNumber = request.GET['Tnumber']
        print teamNumber
        person1 = researchUser.objects.filter(teamNumber=teamNumber,number=pc.encrypt(number))
        person1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户", username
            list = researchUser.objects.filter(teamNumber=teamNumber)
            List = []
            if list.exists():
                for i in list:
                    reClass1 = researchClass.objects.get(number=i.classNum,teamNumber=userteam)  # 进行分类名称查询
                    className = reClass1.name
                    picture = os.path.join("/", str(i.picture))
                    person1 = management.bean.rePerson.rePerson(pc.decrypt(i.number), i.teamNumber, picture, i.name,
                                                                pc.decrypt(i.phone), pc.decrypt(i.qqnumber), i.describe,
                                                                className)
                    List.append(person1)
                    person1.cout()
                return render(request, 'researchUser/reUserList.html',
                              {'username': username,'userstatus': userstatus,'userteam':userteam, 'number': teamNumber, 'List': List})
            else:
                return render(request, 'researchUser/reUserList.html',
                              {'username': username,'userstatus': userstatus,'userteam':userteam, 'number': teamNumber, 'List': None})
        else:
            return render(request, 'researchUser/reUserList.html')
    else:
        return render(request, 'researchUser/reUserList.html')
