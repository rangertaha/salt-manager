#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'^list/$', FabricAccessList.as_view(), name='fabric_access_list'),
    url(r'^create/$', FabricAccessCreate.as_view(), name='fabric_access_create'),
    url(r'^(?P<pk>\d+)/$', FabricAccessDetail.as_view(), name='fabric_access_details'),
    url(r'^delete/(?P<pk>\d+)/$', FabricAccessDelete.as_view(), name='fabric_access_delete'),
    url(r'^update/(?P<pk>\d+)/$', FabricAccessUpdate.as_view(), name='fabric_access_update'),
)