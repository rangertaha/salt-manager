#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'^index/$', FabricIndex.as_view(), name='fabric_index'),

    # Users
    url(r'^access/$', FabricAccessList.as_view(), name='fabric_access'),
    url(r'^access/create/$', FabricAccessCreate.as_view(), name='fabric_access_create'),
    url(r'^access/(?P<pk>\d+)/$', FabricAccessDetail.as_view(), name='fabric_access_details'),
    url(r'^access/delete/(?P<pk>\d+)/$', FabricAccessDelete.as_view(), name='fabric_access_delete'),
    url(r'^access/update/(?P<pk>\d+)/$', FabricAccessUpdate.as_view(), name='fabric_access_update'),

    url(r'^history/$', ExecutionHistoryList.as_view(), name='fabric_exe_history'),
    url(r'^history/(?P<pk>\d+)/$', ExecutionHistoryDetail.as_view(), name='fabric_exe_history_details'),

    #url(r'^cmd/$', ExecutionHistoryList.as_view(), name='command'),
    #url(r'^cmd/(?P<pk>\d+)/$', ExecutionHistoryDetail.as_view(), name='command_details'),
)