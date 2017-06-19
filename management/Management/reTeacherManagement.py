#coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import management.tools.MD5 as MD5
import management.bean.rePerson,management.bean.researchClass
from management.models import researchTeacher,researchClass
import os

#渲染模板
def reTeacherAdd(request):
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
                return render(request, 'researchTeacher/reTeacherAdd.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'number':teamNumber,'List':List})
        else:
            return render(request, 'researchTeacher/reTeacherAdd.html')
    else:
        return render(request, 'researchTeacher/reTeacherAdd.html')

def reTeacherUpdate(request):
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
                return render(request, 'researchTeacher/reTeacherUpdate.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'person':rePerson1, 'List':List})
        else:
            return render(request, 'researchTeacher/reTeacherUpdate.html')
    else:
        return render(request, 'researchTeacher/reTeacherUpdate.html')
#渲染模板
def reTeacherDetail(request):
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
                return render(request, 'researchTeacher/reTeacherDetail.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'classNumber':classNumber,'person':rePerson1})
        else:
            return render(request, 'researchTeacher/reTeacherDetail.html')
    else:
        return render(request, 'researchTeacher/reTeacherDetail.html')


def reTeacherList(request):
    if request.GET:
        pc=MD5.prpcrypt('keyskeyskeyskeys')
        teamNumber=request.GET['Fnumber']
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户",username
            list=researchTeacher.objects.filter(teamNumber=teamNumber)
            List=[]
            print list.exists()
            if list.exists():
                for i in list:
                    reClass1=researchClass.objects.get(number=i.classNum,teamNumber=teamNumber)#进行分类名称查询
                    className=reClass1.name
                    #对照片的路径进行重新封装
                    picture = os.path.join("/", str(i.picture))
                    print pc.decrypt(i.phone)
                    person1=management.bean.rePerson.rePerson(pc.decrypt(i.number),i.teamNumber,picture,i.name,pc.decrypt(i.phone),pc.decrypt(i.qqnumber),i.describe,className)
                    List.append(person1)
                    person1.cout()
                return render(request, 'researchTeacher/reTeacherList.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'number':teamNumber, 'List': List})
            else:
                return render(request, 'researchTeacher/reTeacherList.html', {'username': username,'userstatus': userstatus,'userteam':userteam,'number':teamNumber, 'List':None})
        else:
            return render(request, 'researchTeacher/reTeacherList.html')
    else:
        return render(request, 'researchTeacher/reTeacherList.html')


@csrf_exempt
def reTeacherAddPost(request):
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
        res=researchTeacher.objects.filter(teamNumber=tnumber,number=pc.encrypt(number))
        if res.exists():
            return HttpResponse("ID already")
        else:
            reTeacher1 = researchTeacher(teamNumber=tnumber, number=pc.encrypt(number), name=name, describe=des,
                                         qqnumber=pc.encrypt(qq), classNum=Fclass, picture=file,
                                         phone=pc.encrypt(phone))
            reTeacher1.save()
            return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")


@csrf_exempt
def reTeacherUpdatePost(request):
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
        reTeacher1=researchTeacher.objects.get(number=pc.encrypt(number),teamNumber=userteam)
        reTeacher1.name=name
        reTeacher1.describe=des
        reTeacher1.qqnumber=pc.encrypt(qq)
        reTeacher1.classNum=Fclass
        reTeacher1.picture=file
        reTeacher1.phone=pc.encrypt(phone)
        reTeacher1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def reTeacherDelPost(request):
    if request.GET:
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        number = request.GET['Fnumber']
        teamNumber = request.GET['Tnumber']
        print teamNumber
        person1 = researchTeacher.objects.filter(teamNumber=teamNumber,number=pc.encrypt(number))
        person1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户", username
            list = researchTeacher.objects.filter(teamNumber=teamNumber)
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
                return render(request, 'researchTeacher/reTeacherList.html',
                              {'username': username,'userstatus': userstatus,'userteam':userteam,'number': teamNumber, 'List': List})
            else:
                return render(request, 'researchTeacher/reTeacherList.html',
                              {'username': username,'userstatus': userstatus,'userteam':userteam, 'number': teamNumber, 'List': None})
        else:
            return render(request, 'researchTeacher/reTeacherList.html')
    else:
        return render(request, 'researchTeacher/reTeacherList.html')
