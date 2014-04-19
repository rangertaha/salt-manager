#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals
import logging

from django.contrib import admin

from models import Host

# Get an instance of a logger
logger = logging.getLogger(__name__)


class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'name', 'description')
    list_display_links = ('id', 'created', 'description')
    list_editable =  ('name',)
    search_fields = ('id', 'name', 'description')
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


admin.site.register(Host, HostAdmin)

