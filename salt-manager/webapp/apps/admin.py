#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals
import logging

from django.contrib import admin

#from models import Section, MenuItem

# Get an instance of a logger
logger = logging.getLogger(__name__)

"""
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description' )
    prepopulated_fields = {'slug': ('name', )}
    #exclude = ('slug',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'order', 'section', 'parent', 'page', 'name', )
    #search_fields = ('id', 'name', )
    #ordering = ['order']

    #list_display_links = ('id', 'created', 'description')
    list_editable =  ('active','order', 'section', 'parent','page', 'name')
    search_fields = ('order', 'name')
    #prepopulated_fields = {'slug': ('title', )}

    list_filter = ('section__name','created',)
    #raw_id_fields = ('images', 'files', 'videos')




admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Section, SectionAdmin)
"""

