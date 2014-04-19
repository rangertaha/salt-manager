#!/usr/bin/env python
"""
"""
from __future__ import unicode_literals
import logging

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models

from settings import *

# Get an instance of a logger
logger = logging.getLogger(__name__)



class Access(models.Model):
    """
    """
    username = models.CharField(max_length=512, blank=True, null=True)
    password = models.CharField(max_length=512, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    private_key = models.TextField(blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.name)

    def use_sudo(self):
        if self.username.strip() == 'root':
            return False
        else:
            return True

    def has_pub_key(self):
        if len(self.public_key) < 380 or self.public_key == None:
            return False
        else:
            return True

