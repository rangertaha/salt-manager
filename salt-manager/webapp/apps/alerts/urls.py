#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from views import ArticleList, ArticleDetail, ArticleUpdate

urlpatterns = patterns('',
    url(r'^$', ArticleList.as_view(), name='articles'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetail.as_view(), name='article_details'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article_details_pk'),
    url(r'^update/(?P<slug>[\w-]+)/$', ArticleUpdate.as_view(), name='man_update'),
    url(r'^update/(?P<slug>[\w-]+)/(?P<pk>[\d+]+)/$', ArticleUpdate.as_view(), name='man_update_pk'),
)