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



class FabricPackage(models.Model):
    """
    """
    user = models.ForeignKey(User)
    filename = models.CharField(max_length=128, blank=True, null=True)
    package = models.FileField(upload_to='packages/%Y/%m/%d')
    #remote_dir = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.filename)