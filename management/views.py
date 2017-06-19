#coding=utf-8
from django.shortcuts import render
import management.bean.User

# Create your views here.
def login(request):
    #判断username是否存在session中
    if "username" in request.session:
        del request.session['username']
    return render(request,'login.html')

