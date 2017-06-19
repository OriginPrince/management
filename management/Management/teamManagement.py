#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
import  management.bean.Team
from django.views.decorators.csrf import csrf_exempt
from management.models import team,researchClass,researchTeacher,researchUser,user
import management.bean.researchClass
import management.tools.MD5 as MD5
import os

def teamAdd(request):
    #判断username是否存在session中
    if "username" in request.session:
        username=request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        if username:
            return render(request, 'team/teamAdd.html', {'username': username,'userstatus': userstatus,'userteam':userteam})
    else:
        return render(request, 'team/teamAdd.html')

#渲染模板
def teamUpdate(request):
    #判断username是否存在session中
    if request.GET:
        number = request.GET['number']
        name = request.GET['name']
        des = request.GET['des']
        team1=management.bean.Team.Team(name,number,des)
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户",username
            if username:
                return render(request, 'team/teamUpdate.html', {'username': username,'userstatus': userstatus,'userteam':userteam, 'team':team1})
        else:
            return render(request, 'team/teamUpdate.html')
    else:
        return render(request, 'team/teamUpdate.html')

def teamList(request):
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        print "用户", username
        list=team.objects.all()
        if username:
            return render(request, 'team/teamList.html', {'username': username,'userstatus': userstatus, 'userteam':userteam,'List':list})
    else:
        return render(request, 'team/teamList.html')

@csrf_exempt
def teamAddPost(request):
    if request.POST:
        name = request.POST['Fname']
        number = request.POST['Fnumber']
        des = request.POST['Fdes']
        res=team.objects.filter(number=number)
        if res.exists():
            return HttpResponse("ID already")
        else:
            team1=team(number=number,name=name,describe=des)
            team1.save()
            return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

#修改数据
@csrf_exempt
def teamUpdatePost(request):
    if request.POST:
        name = request.POST['Fname']
        number = request.POST['Fnumber']
        des = request.POST['Fdes']
        team1=team.objects.get(number=number)
        team1.describe=des
        team1.name=name
        team1.save()
        return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

def teamUserDetail(request):
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            list = researchUser.objects.filter(teamNumber=userteam)
            List = []
            if list.exists():
                for i in list:
                    reClass1 = researchClass.objects.get(number=i.classNum, teamNumber=userteam)  # 进行分类名称查询
                    className = reClass1.name
                    picture = os.path.join("/", str(i.picture))
                    person1 = management.bean.rePerson.rePerson(pc.decrypt(i.number), i.teamNumber, picture, i.name,
                                                                pc.decrypt(i.phone), pc.decrypt(i.qqnumber), i.describe,
                                                                className)
                    List.append(person1)

            return render(request, 'team/teamUserList.html',
                          {'username': username, 'userstatus': userstatus, 'userteam': userteam, 'List': List,"type":"研究员"})
        else:
            return render(request, 'team/teamUserList.html')


def teamTeacherDetail(request):
    pc = MD5.prpcrypt('keyskeyskeyskeys')
    if "username" in request.session:
        username = request.session['username']
        userstatus = request.session['userstatus']
        userteam = request.session['userteam']
        list = researchTeacher.objects.filter(teamNumber=userteam)
        List = []
        if list.exists():
            for i in list:
                reClass1 = researchClass.objects.get(number=i.classNum, teamNumber=userteam)  # 进行分类名称查询
                className = reClass1.name
                picture = os.path.join("/", str(i.picture))
                person1 = management.bean.rePerson.rePerson(pc.decrypt(i.number), i.teamNumber, picture, i.name,
                                                            pc.decrypt(i.phone), pc.decrypt(i.qqnumber), i.describe,
                                                            className)
                List.append(person1)

        return render(request, 'team/teamUserList.html',
                      {'username': username, 'userstatus': userstatus, 'userteam': userteam, 'List': List,"type":"导师"})
    else:
        return render(request, 'team/teamUserList.html')

def teamDetail(request):
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            team1=team.objects.get(number=userteam)
            list = researchClass.objects.filter(teamNumber=userteam)
            List = []
            if list.exists():
                for i in list:
                    class1 = management.bean.researchClass.researchClass(userteam,i.number,i.name,i.describe)
                    List.append(class1)

            userList = researchUser.objects.filter(teamNumber=userteam)
            userList1 = []
            if userList.exists():
                for i in userList:
                    user1 = management.bean.rePerson.rePerson(pc.decrypt(i.number),userteam, i.picture, i.name,pc.decrypt(i.phone), pc.decrypt(i.qqnumber), i.describe,i.classNum)
                    userList1.append(user1)


            teacherList = researchTeacher.objects.filter(teamNumber=userteam)
            teacherList1 = []
            if teacherList.exists():
                for i in teacherList:
                    teacher1 = management.bean.rePerson.rePerson(pc.decrypt(i.number),userteam,  i.picture, i.name,
                                                                 pc.decrypt(i.phone), pc.decrypt(i.qqnumber),
                                                                 i.describe, i.classNum)
                    teacherList1.append(teacher1)



            return render(request, 'team/teamDetail.html',
                              {'username': username,'userstatus': userstatus,'userteam':userteam, 'team': team1, 'reUser': userList1, 'teacher': teacherList1, 'List': List})
        else:
            return render(request, 'team/teamDetail.html')

#删除团队签需要先看看是不是还有在该团队下的分类
def teamDelDataPost(request):
    if request.GET:
        teamNumber = request.GET['Fnumber']
        res1=researchClass.objects.filter(teamNumber=teamNumber)
        user1=user.objects.filter(teamNumber=teamNumber)
        if res1.exists():
            return HttpResponse("alreadyClass")
        elif user1.exists():
            return HttpResponse("alreadyUser")
        else:
            return HttpResponse("true")
    else:
        return HttpResponse("false")

#有问题
def teamDelPost(request):
    if request.GET:
        teamNumber = request.GET['Fnumber']
        team1 = team.objects.get(number=teamNumber)
        team1.delete()
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            print "用户", username
            list = team.objects.all()
            return render(request, 'team/teamList.html',
                          {'username': username, 'userstatus': userstatus, 'number': teamNumber, 'userteam': userteam,
                           'List': list})
        else:
            return render(request, 'team/teamList.html')


    else:
        return render(request, 'team/teamList.html')

def teamListDetail(request):
    if request.GET:
        teamNumber=request.GET['Fteam']
        pc = MD5.prpcrypt('keyskeyskeyskeys')
        if "username" in request.session:
            username = request.session['username']
            userstatus = request.session['userstatus']
            userteam = request.session['userteam']
            team1 = team.objects.get(number=teamNumber)
            list = researchClass.objects.filter(teamNumber=teamNumber)
            List = []
            if list.exists():
                for i in list:
                    class1 = management.bean.researchClass.researchClass(teamNumber, i.number, i.name, i.describe)
                    List.append(class1)

            userList = researchUser.objects.filter(teamNumber=teamNumber)
            userList1 = []
            if userList.exists():
                for i in userList:
                    user1 = management.bean.rePerson.rePerson(pc.decrypt(i.number), teamNumber, i.picture, i.name,
                                                              pc.decrypt(i.phone), pc.decrypt(i.qqnumber), i.describe,
                                                              i.classNum)
                    userList1.append(user1)

            teacherList = researchTeacher.objects.filter(teamNumber=teamNumber)
            teacherList1 = []
            if teacherList.exists():
                for i in teacherList:
                    teacher1 = management.bean.rePerson.rePerson(pc.decrypt(i.number), teamNumber, i.picture, i.name,
                                                                 pc.decrypt(i.phone), pc.decrypt(i.qqnumber),
                                                                 i.describe, i.classNum)
                    teacherList1.append(teacher1)

            return render(request, 'team/teamDetail.html',
                          {'username': username, 'userstatus': userstatus, 'userteam': userteam, 'team': team1,
                           'reUser': userList1, 'teacher': teacherList1, 'List': List})
        else:
            return render(request, 'team/teamDetail.html')
    else:
        return render(request, 'team/teamDetail.html')

