# -*- coding: utf-8 -*-
'''
Created on 2013-1-15

@author: tonycao
'''
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(max_length=100)
    fansid=models.CharField(max_length=20)
    username=models.CharField(max_length=30)
    province=models.CharField(max_length=10,blank=True)
    city=models.CharField(max_length=10,blank=True)
    location=models.CharField(max_length=60,blank=True)
    gender=models.CharField(max_length=5,blank=True)
    verified=models.CharField(max_length=5,blank=True)
    
    def __unicode__(self):       
        return self.fansid
    
    class Meta:
        ordering=['username']
    
    class Admin:
        pass
    
class UserDetailinfo(models.Model):
    uid=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    profileurl=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    followerscount=models.CharField(max_length=100)
    friendscount=models.CharField(max_length=100)
    statuescount=models.CharField(max_length=100)
    createdat=models.CharField(max_length=100)
    verified=models.CharField(max_length=10)
    verifiedreason=models.CharField(max_length=500)
    bifollowerscount=models.CharField(max_length=10)
    
    def __unicode__(self):       
        return self.username
    
    class Meta:
        ordering=['username']
    
    class Admin:
        pass
    
class UserId(models.Model):
    fansid=models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.fansid 
    class Meta:
        ordering=['fansid']
    class Admin:
        pass
    