#coding=utf-8
"""UniversityService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf.urls import url
from django.contrib import admin

import management.Login.login as ml
import management.Management.newsManagement as un
import management.Management.publicManagement as pu
import management.Management.contactManagement as uc
import management.Management.coordinateManagement as uo
import management.Management.paperManagement as up
import management.Management.bookManagement as ub
import management.Management.patentManagement as pa
import management.Management.softwareManagement as so
import management.Management.userManagement as ur
import management.Management.teamManagement as ut
import management.Management.reClassManagement as rc
import management.Management.reTeacherManagement as rt
import management.Management.reUserManagement as ru
import management.Management.admissionManagement as ad
import management.Management.aboutManagement as ab
import management.Management.personalInfoManagement as pe
import management.views as mv
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', mv.login),
    url(r'^login_post/$', ml.login_post),
    url(r'^logout/$', ml.logout),
    url(r'^userList/$', ur.userList),
    url(r'^userAdd/$', ur.userAdd),
    url(r'^userAdd_post/$', ur.userAddPost),
    url(r'^userUpdate/$', ur.userUpdate),
    url(r'^userUpdateData/$', ur.userUpdateData),
    url(r'^userUpdate_post/$', ur.userUpdatePost),
    url(r'^userDel/$', ur.userDel),
    url(r'^personalInfoUpdate/$', pe.personalInfoUpdate),
    url(r'^personalInfoDetail/$', pe.personalInfoDetail),
    url(r'^personalInfoUpdate_post/$', pe.personalInfoUpdatePost),
    url(r'^newsList/$', un.newsList),
    url(r'^newsAdd/$', un.newsAdd),
    url(r'^newsAdd_get/$', un.newsAddGet),
    url(r'^newsDetail/$', un.newsDetail),
    url(r'^newsUpdate/$', un.newsUpdate),
    url(r'^newsUpdate_post/$', un.newsUpdatePost),
    url(r'^newsDel/$', un.newsDel),
    url(r'^publicList/$', pu.publicList),
    url(r'^publicAdd/$', pu.publicAdd),
    url(r'^publicAdd_get/$', pu.publicAddGet),
    url(r'^publicDetail/$', pu.publicDetail),
    url(r'^publicUpdate/$', pu.publicUpdate),
    url(r'^publicUpdate_post/$', pu.publicUpdatePost),
    url(r'^publicDel/$', pu.publicDel),
    url(r'^publicNew/$', pu.publicNew),
    url(r'^contactList/$', uc.contactList),
    url(r'^contactAdd/$', uc.contactAdd),
    url(r'^contactAdd_get/$', uc.contactAddGet),
    url(r'^contactDetail/$', uc.contactDetail),
    url(r'^contactUpdate/$', uc.contactUpdate),
    url(r'^contactUpdate_post/$', uc.contactUpdatePost),
    url(r'^contactDel/$', uc.contactDel),
    url(r'^coordinateList/$', uo.coordinateList),
    url(r'^coordinateAdd/$', uo.coordinateAdd),
    url(r'^coordinateAdd_get/$', uo.coordinateAddGet),
    url(r'^coordinateDetail/$', uo.coordinateDetail),
    url(r'^coordinateUpdate/$', uo.coordinateUpdate),
    url(r'^coordinateUpdate_post/$', uo.coordinateUpdatePost),
    url(r'^coordinateDel/$', uo.coordinateDel),
    url(r'^paperAdd/$', up.paperAdd),
    url(r'^paperAdd_post/$', up.paperAddPost),
    url(r'^paperFile/$', up.paperFileDownLoad),
    url(r'^paperList/$', up.paperList),
    url(r'^paperUpdate/$', up.paperUpdate),
    url(r'^paperUpdate_post/$', up.paperUpdatePost),
    url(r'^paperDel/$', up.paperDel),
    url(r'^patentAdd/$', pa.patentAdd),
    url(r'^patentAdd_post/$', pa.patentAddPost),
    url(r'^patentFile/$', pa.patentFileDownLoad),
    url(r'^patentList/$', pa.patentList),
    url(r'^patentUpdate/$', pa.patentUpdate),
    url(r'^patentUpdate_post/$', pa.patentUpdatePost),
    url(r'^patentDel/$', pa.patentDel),
    url(r'^softwareAdd/$', so.softwareAdd),
    url(r'^softwareAdd_post/$', so.softwareAddPost),
    url(r'^softwareFile/$', so.softwareFileDownLoad),
    url(r'^softwareList/$', so.softwareList),
    url(r'^softwareUpdate/$', so.softwareUpdate),
    url(r'^softwareUpdate_post/$', so.softwareUpdatePost),
    url(r'^softwareDel/$', so.softwareDel),
    url(r'^admissionAdd/$', ad.admissionAdd),
    url(r'^admissionAdd_post/$', ad.admissionAddPost),
    url(r'^admissionFile/$', ad.admissionFileDownLoad),
    url(r'^admissionList/$', ad.admissionList),
    url(r'^admissionUpdate/$', ad.admissionUpdate),
    url(r'^admissionUpdate_post/$', ad.admissionUpdatePost),
    url(r'^admissionDel/$', ad.admissionDel),
    url(r'^teamUserDetail/$', ut.teamUserDetail),
    url(r'^teamTeacherDetail/$', ut.teamTeacherDetail),
    url(r'^teamAdd/$', ut.teamAdd),
    url(r'^teamAdd_post/$', ut.teamAddPost),
    url(r'^teamList/$', ut.teamList),
    url(r'^teamListDetail/$', ut.teamListDetail),
    url(r'^teamDetail/$', ut.teamDetail),
    url(r'^teamUpdate/$', ut.teamUpdate),
    url(r'^teamUpdate_post/$', ut.teamUpdatePost),
    url(r'^teamDelData/$', ut.teamDelDataPost),
    url(r'^teamDel_post/$', ut.teamDelPost),
    url(r'^bookAdd/$', ub.bookAdd),
    url(r'^bookAdd_post/$', ub.bookAddPost),
    url(r'^bookFile/$', ub.bookFileDownLoad),
    url(r'^bookList/$', ub.bookList),
    url(r'^bookUpdate/$', ub.bookUpdate),
    url(r'^bookUpdate_post/$', ub.bookUpdatePost),
    url(r'^bookDel/$', ub.bookDel),
    url(r'^aboutAdd/$', ab.aboutAdd),
    url(r'^aboutAdd_post/$', ab.aboutAddPost),
    url(r'^aboutUpdate/$', ab.aboutUpdate),
    url(r'^aboutList/$', ab.aboutList),
    url(r'^aboutUpdate_post/$', ab.aboutUpdatePost),
    url(r'^aboutDetail/$', ab.aboutDetail),
    url(r'^aboutDel/$', ab.aboutDel),
    url(r'^reClassList/$', rc.reClassList),
    url(r'^reClassDel/$', rc.reClassDelPost),
    url(r'^reClassDelData/$', rc.reClassDelDataPost),
    url(r'^reClassDetail/$', rc.reClassDetail),
    url(r'^reClassUpdate/$', rc.reClassUpdate),
    url(r'^reClassUpdate_post/$', rc.reClassUpdatePost),
    url(r'^reClassAdd/$', rc.reClassAdd),
    url(r'^reClassAdd_post/$', rc.reClassAddPost),
    url(r'^reTeacherAdd/$', rt.reTeacherAdd),
    url(r'^reTeacherAdd_post/$', rt.reTeacherAddPost),
    url(r'^reTeacherList/$', rt.reTeacherList),
    url(r'^reTeacherDetail/$', rt.reTeacherDetail),
    url(r'^reTeacherUpdate/$', rt.reTeacherUpdate),
    url(r'^reTeacherUpdate_post/$', rt.reTeacherUpdatePost),
    url(r'^reTeacherDel/$', rt.reTeacherDelPost),
    url(r'^reUserAdd/$', ru.reUserAdd),
    url(r'^reUserAdd_post/$', ru.reUserAddPost),
    url(r'^reUserList/$', ru.reUserList),
    url(r'^reUserDetail/$', ru.reUserDetail),
    url(r'^reUserUpdate/$', ru.reUserUpdate),
    url(r'^reUserUpdate_post/$', ru.reUserUpdatePost),
    url(r'^reUserDel/$', ru.reUserDelPost),
    #设置以static开头的静态文件的路径
url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATICFILES_DIRS,'show_indexes': True}),
    #设置以PictureFiles开头的静态文件的路径
url(r'^PictureFiles/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.UPLOADIMGS_DIRS,'show_indexes': True}),
]
