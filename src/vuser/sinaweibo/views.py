# -*- coding: utf-8 -*-
'''
Created on 2013-1-15

@author: tonycao
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from vuser.sinaweibo import forms
from vuser.sinaweibo.models import UserInfo
from vuser.sinaweibo.models import UserDetailinfo
from vuser.sinaweibo.models import UserId

from vuser.weiboapi.weibo import APIClient

APP_KEY = '1279033890' # app key
APP_SECRET = '392001a59101bc9bee428429247f6251' # app secret
CALLBACK_URL = 'http://127.0.0.1:8000/login_check' # callback url

def index(request):
    return render_to_response("weibo/login.html",{},context_instance=RequestContext(request))

def login(request):

    
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    return HttpResponseRedirect(url)

def login_check(request):
    code=request.GET.get('code',None)
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    r=client.request_access_token(code)
    access_token=r.access_token
    expires_in=r.expires_in
    
    request.session['access_token']=access_token
    request.session['expires_in']=expires_in
    
    return render_to_response("weibo/operation.html",{'userForm':forms.UserForm()},context_instance=RequestContext(request))

def get_fans(request):
    access_token=request.session['access_token']
    expires_in=request.session['expires_in']
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(access_token, expires_in)
    
    if request.method=="POST":
        form=forms.UserForm(request.POST.copy())
        if form.is_valid():
            username=form.cleaned_data['username']
            user_info=client.users__show(screen_name=username)
            user_id=user_info.id
            #获取用户粉丝
            '''next_cursor=1
            while next_cursor>0:
                fans=client.friendships__followers(screen_name=username,count=200,cursor=next_cursor)
                #fans=client.friendships__followers__active(uid=user_id,count=200)
                next_cursor=fans.next_cursor
                print next_cursor
                for fan in fans.users:
                    userinfo=UserInfo(uname=username,fansid=fan.id,username=fan.screen_name,province=fan.province,city=fan.province,location=fan.location,gender=fan.gender,verified=fan.verified)
                    userinfo.save()'''
                    
            #获取优质粉丝
            user_info=client.users__show(screen_name=username)
            user_id=user_info.id
            active_fans=client.friendships__followers__active(uid=user_id,count=200)
            for active_fan in active_fans.users:
                print active_fan.screen_name
                userinfo=UserInfo(fansid=active_fan.id,username=active_fan.screen_name,province=active_fan.province,city=active_fan.province,location=active_fan.location,gender=active_fan.gender,verified=active_fan.verified)
                userinfo.save()          
    return render_to_response("weibo/operation.html",{'userForm':forms.UserForm()},context_instance=RequestContext(request))
def get_userinfo(request):
    print 'hello'
    access_token=request.session['access_token']
    expires_in=request.session['expires_in']
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(access_token, expires_in)
    
    #从数据库中读取用户id
    uid_list=UserInfo.objects.filter(verified='True')
    #uid_list=UserId.objects.all()
    for userid in uid_list:
        print userid.fansid
        userinfo=client.users__show(uid=userid.fansid)
        userdetailinfo=UserDetailinfo(uid=userinfo.id,username=userinfo.screen_name,location=userinfo.location,profileurl=userinfo.profile_url,gender=userinfo.gender,followerscount=userinfo.followers_count,friendscount=userinfo.friends_count,statuescount=userinfo.statuses_count,createdat=userinfo.created_at,verified=userinfo.verified,verifiedreason=userinfo.verified_reason,bifollowerscount=userinfo.bi_followers_count)
        userdetailinfo.save()
    return render_to_response("weibo/operation.html",{'userForm':forms.UserForm()},context_instance=RequestContext(request))

    
