#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from views import ServiceList, ServiceDetail, ServiceUpdate

urlpatterns = patterns('',
    url(r'^list/$', ServiceList.as_view(), name='services'),
    url(r'^detail/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ServiceDetail.as_view(), name='service_detail'),
    url(r'^update/(?P<slug>[\w-]+)/(?P<pk>[\d+]+)/$', ServiceUpdate.as_view(), name='service_update'),
    #url(r'^update/(?P<slug>[\w-]+)/(?P<pk>[\d+]+)/$', ServiceUpdate.as_view(), name='service_delete'),
)