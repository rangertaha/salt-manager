#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
from os import system

from django.core.management.base import NoArgsCommand









def install():
    system('python manage.py syncdb ')
    system('python manage.py dummy')
    system('python manage.py runserver')


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        install()
