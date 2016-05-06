#coding:utf-8
#通用类
import os, sys, commands, re, time, json
append_path=os.path.abspath('/data/AppStore')
sys.path.append(append_path)
from django.shortcuts import render_to_response, get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.conf import settings
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Q
#models
from store.models import *

def get_app_class(request):
    if request.method == 'POST':
        get_dict=appclass.objects.all().values()
        return_list=[]
        for class_info in get_dict:
            perinfo={'id':class_info['classid'],'name':class_info['classname']}
            return_list.append(perinfo)
        return HttpResponse(json.dumps(return_list ,indent=4,ensure_ascii=False), 'application/javascript')

def get_app_base(request):
    if request.method == 'POST':
        classid=request.POST['id']
        get_dict=appclassinfo.objects.filter(classid=classid).order_by('-pk').values()
        return_list=[]
        for app_base in get_dict:
            perinfo={'id':app_base['appid'],'name':app_base['appname'],'pkg':app_base['appfolder'],'LogoUrl':app_base['applogo'],'Search':app_base['appsearch']}
            return_list.append(perinfo)
        return HttpResponse(json.dumps(return_list ,indent=4,ensure_ascii=False), 'application/javascript')

def get_app_info(request):
    if request.method == 'POST':
        appid=request.POST['id']
        get_dict=appinfo.objects.filter(appid=appid).values()
        app_info=get_dict[0]
        perinfo={'id':app_info['appid'],'ctime':app_info['uptime'],'detail':app_info['appdesc'],'ver':app_info['version'],'DownUrl':app_info['downloadurl'],'Size':app_info['appsize'],'level':app_info['level'],'PicUrl':app_info['mainpic'],'pkg':app_info['appfolder']}
        return HttpResponse(json.dumps(perinfo ,indent=4,ensure_ascii=False), 'application/javascript')

def search_app(request):
    if request.method == 'POST':
        skey=request.POST['key']
        return_list=[]
        if skey != "":
            get_dict=appclassinfo.objects.filter(appsearch__contains=skey.lower()).order_by('-pk').values()
            for app_base in get_dict:
                perinfo={'id':app_base['appid'],'name':app_base['appname'],'pkg':app_base['appfolder'],'LogoUrl':app_base['applogo'],'Search':app_base['appsearch']}
                return_list.append(perinfo)
            return HttpResponse(json.dumps(return_list ,indent=4,ensure_ascii=False), 'application/javascript')
        else:return HttpResponse(json.dumps(return_list ,indent=4,ensure_ascii=False), 'application/javascript')

