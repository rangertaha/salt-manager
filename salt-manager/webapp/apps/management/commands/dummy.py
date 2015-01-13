#!/bin/env python
#-*- coding:utf-8 -*-
"""
Load testing
"""
from os import system
from django.core.management.base import NoArgsCommand
from webapp.apps.hosts.models import *
from webapp.apps.fabric.access.models import *


def load_hosts():
    for n in range(1000):
        Host.objects.get_or_create(name='web{0}.dev4ops.com'.format(n), ip='192.168.101.123:{0}'.format(n), description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.")


def load_access():
    for n in range(1000):
        Access.objects.get_or_create(username='User{0}'.format(n), password='#############')


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        load_hosts()
        load_access()
