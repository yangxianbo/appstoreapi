#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-05-03 15:32:59
#FILENAME: urls.py
#DESCRIPTION: 
#===============================================================


from django.conf.urls import include, url, patterns
urlpatterns = patterns('api.views',
    url(r'^LeftMenu$', 'get_app_class', name='get_app_class'),
    url(r'^AppMenu$', 'get_app_base', name='get_app_base'),
    url(r'^AppInfo$', 'get_app_info', name='get_app_info'),
    url(r'^AppSearch$', 'search_app', name='search_app'),
)

