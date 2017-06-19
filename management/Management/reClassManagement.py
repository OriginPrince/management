#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
import management.bean.researchClass
from django.views.decorators.csrf import csrf_exempt
from management.models import researchClass,researchTeacher,researchUser


def reClassAdd(request):
    #判断username是否存在session中
    if request.GET:
        teamnumber=request.GET['Tnumber']
        print "team",teamnumber
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            #查找所有队伍编号是teamNumber的分类
            list = researchClass.objects.filter(teamNumber=teamnumber)
            if list.exists():
                return render(request, 'researchClass/reClassAdd.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'List': list, 'number':teamnumber})
            else:
                return render(request, 'researchClass/reClassAdd.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'List':None, 'number':teamnumber})
        else:
            return render(request, 'researchClass/reClassAdd.html')
    else:
        return render(request, 'researchClass/reClassAdd.html')

#渲染模板
def reClassDetail(request):
    if request.GET:
        name = request.GET['Fname']
        number = request.GET['Fnumber']
        des = request.GET['Fdes']
        Tnumber=request.GET['Tnumber']
        print name+number+des
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            class1=management.bean.researchClass.researchClass(Tnumber,number,name,des)
            return render(request, 'researchClass/reClassDetail.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'class': class1})
        else:
            return render(request, 'researchClass/reClassDetail.html')
    else:
        return render(request, 'researchClass/reClassDetail.html')

def reClassList(request):
    if request.GET:
        teamNumber=request.GET['Tnumber']
        print "team", teamNumber
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户", username
            list=researchClass.objects.filter(teamNumber=teamNumber)
            if list.exists():
                return render(request, 'researchClass/reClassList.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'number':teamNumber,'List': list})
            else:
                return render(request, 'researchClass/reClassList.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'number':teamNumber,'List':None})
        else:
            return render(request, 'researchClass/reClassList.html')
    else:
        return render(request, 'researchClass/reClassList.html')

@csrf_exempt
def reClassAddPost(request):
    print "234"
    if request.POST:
        print "123"
        name = request.POST['Fname']
        number = request.POST['Fnumber']
        teamnumber = request.POST['Ftnumber']
        des = request.POST['Fdes']
        res = researchClass.objects.filter(teamNumber=teamnumber,number=number)
        if res.exists():
            return HttpResponse("ID already")
        else:
            researchClass1 = researchClass(teamNumber=teamnumber, number=number,name=name, describe=des)
            researchClass1.save()
            return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

#修改数据
@csrf_exempt
def reClassUpdatePost(request):
    if request.POST:
        name = request.POST['Fname']
        number = request.POST['Fnumber']
        des = request.POST['Fdes']
        print number+des+name
        user1=researchClass.objects.get(number=number)
        user1.name=name
        user1.describe=des
        user1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")
#渲染模板
def reClassUpdate(request):
    if request.GET:
        name = request.GET['Fname']
        number = request.GET['Fnumber']
        des = request.GET['Fdes']
        Tnumber=request.GET['Tnumber']
        print name+number+des
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            class1=management.bean.researchClass.researchClass(Tnumber,number,name,des)
            return render(request, 'researchClass/reClassUpdate.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'class': class1})
        else:
            return render(request, 'researchClass/reClassUpdate.html')
    else:
        return render(request, 'researchClass/reClassUpdate.html')

#删除分类前需要先查看是不是还有在该分类下的导师和研究员
def reClassDelDataPost(request):
    if request.GET:
        number = request.GET['Fnumber']
        teamNumber = request.GET['Tnumber']
        res1=researchTeacher.objects.filter(classNum=number,teamNumber=teamNumber)
        res2=researchUser.objects.filter(classNum=number,teamNumber=teamNumber)
        if res1.exists():
            return HttpResponse("already")
        elif res2.exists():
            return HttpResponse("already")
        else:
            return HttpResponse("true")
    else:
        return HttpResponse("false")

def reClassDelPost(request):
    if request.GET:
        number = request.GET['Fnumber']
        teamNumber = request.GET['Tnumber']
        user1 = researchClass.objects.get(number=number, teamNumber=teamNumber)
        user1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户", username
            list = researchClass.objects.filter(teamNumber=teamNumber)
            if list.exists():
                return render(request, 'researchClass/reClassList.html',
                              {'username': username,'userstatus': userstatus,'userteam':userteam, 'number': teamNumber, 'List': list})
            else:
                return render(request, 'researchClass/reClassList.html',
                              {'username': username,'userstatus': userstatus,'userteam':userteam, 'number': None, 'List': None})
        else:
            return render(request, 'researchClass/reClassList.html' )

    else:
        return render(request, 'researchClass/reClassList.html')