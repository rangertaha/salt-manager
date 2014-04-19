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


class ExecutionHistory(models.Model):
    """
    """
    user = models.ForeignKey(User)
    host = models.CharField(max_length=128, blank=True, null=True)
    ip = models.IPAddressField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    stdout = models.TextField(blank=True, null=True)
    stderr = models.TextField(blank=True, null=True)
    start = models.DateTimeField(auto_now=True, auto_now_add=False)
    end = models.DateTimeField(blank=True, null=True)
    exit = models.IntegerField(max_length=3, blank=True, null=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.ip)

    def status(self):
        if self.stderr != '':
            return 'error'
        if self.stdout != '':
            return 'success'

    def exe_time(self):
        pass


class Command(models.Model):
    """
    """
    name = models.CharField(max_length=512, blank=True, null=True)
    slug = models.SlugField(max_length=512, blank=True, null=True)
    icon = models.CharField(max_length=30, choices=ICON_CHOICES)
    description = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    history = models.ManyToManyField(ExecutionHistory, blank=True, null=True)

    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.name)

    def execute(self, *args):
        history = ExecutionHistory.objects.create(code=self.code)
        pass


@receiver(pre_save, sender=Command)
def slugify_host_name(sender, **kwargs):
    cmd = kwargs['instance']
    cmd.slug = slugify(cmd.name)
