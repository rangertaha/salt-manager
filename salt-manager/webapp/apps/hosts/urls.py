#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from views import HostList, HostDetail, HostUpdate

urlpatterns = patterns('',
    url(r'^list/$', HostList.as_view(), name='host_list'),
    url(r'^detail/(?P<pk>\d+)/$', HostDetail.as_view(), name='host_detail'),
    url(r'^update/(?P<pk>[\d+]+)/$', HostUpdate.as_view(), name='host_update'),
    #url(r'^update/(?P<slug>[\w-]+)/(?P<pk>[\d+]+)/$', HostUpdate.as_view(), name='host_delete'),

)