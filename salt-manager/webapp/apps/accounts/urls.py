#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from views import Index

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^profile/$', Index.as_view(), name='user_account'),
    #url(r'^registration/', include('webapp.apps.accounts.registration.urls')),
    url(r'^registration/', include('webapp.apps.accounts.registration.backends.simple.urls')),
)

