#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'^list/$', FabricPackagesList.as_view(), name='fabric_packages_list'),
    url(r'^create/$', FabricPackagesCreate.as_view(), name='fabric_packages_create'),
    url(r'^(?P<pk>\d+)/$', FabricPackagesDetail.as_view(), name='fabric_packages_details'),
    url(r'^delete/(?P<pk>\d+)/$', FabricPackagesDelete.as_view(), name='fabric_packages_delete'),
    url(r'^update/(?P<pk>\d+)/$', FabricPackagesUpdate.as_view(), name='fabric_packages_update'),
)