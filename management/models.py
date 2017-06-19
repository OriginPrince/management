from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    number=models.CharField(max_length=50)
    status=models.IntegerField()
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    teamNumber = models.CharField(max_length=20)

class team(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=300)

class news(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    teamNumber = models.CharField(max_length=20)

class public(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    teamNumber = models.CharField(max_length=20)

class contact(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    teamNumber = models.CharField(max_length=20)

class coordinate(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    teamNumber = models.CharField(max_length=20)

class researchClass(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=300)
    teamNumber=models.CharField(max_length=20)

class researchTeacher(models.Model):
    number=models.CharField(max_length=50)
    teamNumber = models.CharField(max_length=20)
    picture=models.ImageField(upload_to='PictureFiles/%Y%m%d')
    name=models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    qqnumber = models.CharField(max_length=50)
    describe = models.CharField(max_length=300)
    classNum=models.CharField(max_length=20)

class researchUser(models.Model):
    number = models.CharField(max_length=50)
    teamNumber = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='PictureFiles/%Y%m%d')
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    qqnumber = models.CharField(max_length=50)
    describe = models.CharField(max_length=300)
    classNum=models.CharField(max_length=20)

class paper(models.Model):
    number = models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    file=models.FileField(upload_to='uploadFiles/%Y%m%d')
    teamNumber = models.CharField(max_length=20)

class book(models.Model):
    number = models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    file=models.FileField(upload_to='uploadFiles/%Y%m%d')
    teamNumber = models.CharField(max_length=20)

class patent(models.Model):
    number = models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    file=models.FileField(upload_to='uploadFiles/%Y%m%d')
    teamNumber = models.CharField(max_length=20)

class software(models.Model):
    number = models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    file=models.FileField(upload_to='uploadFiles/%Y%m%d')
    teamNumber = models.CharField(max_length=20)

class admission(models.Model):
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    file=models.FileField(upload_to='uploadFiles/%Y%m%d')
    teamNumber = models.CharField(max_length=20)

class about(models.Model):
    content=models.CharField(max_length=2000)
    author = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    className = models.CharField(max_length=20)
    teamNumber = models.CharField(max_length=20)
