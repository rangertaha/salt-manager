#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('',
    url(r'^index/$', FabricIndex.as_view(), name='fabric_index'),


    url(r'^history/$', ExecutionHistoryList.as_view(), name='fabric_exe_history'),
    url(r'^history/(?P<pk>\d+)/$', ExecutionHistoryDetail.as_view(), name='fabric_exe_history_details'),




    #url(r'packages/', include('webapp.apps.fabpkgs.urls')),
    url(r'^access/', include('webapp.apps.fabric.access.urls')),
    url(r'^packages/', include('webapp.apps.fabric.fabpkgs.urls')),

    #url(r'^cmd/$', ExecutionHistoryList.as_view(), name='command'),
    #url(r'^cmd/(?P<pk>\d+)/$', ExecutionHistoryDetail.as_view(), name='command_details'),
)