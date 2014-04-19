#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals
import logging

from django.contrib import admin

from webapp.apps.wymeditor.admin import RichTextAdmin
from models import Article

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ArticleAdmin(RichTextAdmin):
    list_display = ('id', 'created', 'title', 'subtitle', 'background', 'description')
    list_display_links = ('id', 'created', 'description')
    list_editable =  ('title', 'subtitle', 'background')
    search_fields = ('id', 'title', 'subtitle' )
    #prepopulated_fields = {'slug': ('title', )}
    """
    fieldsets = (
        (None, {
            'fields': ('title', 'body')
        }),
        ('Descriptions', {
            'classes': ('collapse',),
            'fields': ('active', 'subtitle', 'description')
        }),
        ('Media/Files/Graphics', {
            'classes': ('collapse',),
            'fields': ('manpages')
        }),

        )
    """
    #list_filter = ('menuitem__section','created',)
    #raw_id_fields = ('manpages', 'images', 'files', 'videos')


admin.site.register(Article, ArticleAdmin)

