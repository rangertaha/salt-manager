#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals
import logging

from django.contrib import admin

from models import *

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated', 'username', 'password')
    list_display_links = ('id', 'created', 'updated')
    list_editable =  ('username', 'password')
    search_fields = ('id', 'username', 'password')
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


admin.site.register(Access, AccessAdmin)

