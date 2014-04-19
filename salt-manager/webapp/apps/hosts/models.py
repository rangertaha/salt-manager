#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
# import the logging library
from __future__ import unicode_literals
import logging

#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Location(models.Model):
    title = models.CharField(max_length=512, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    city = models.CharField(max_length=512, blank=True, null=True)
    state = models.CharField(max_length=512, blank=True, null=True)
    phone = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.title)


class Group(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.name)


class OS(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.name)

class Host(models.Model):
    """
    """
    name = models.CharField(max_length=512, blank=True, null=True)
    slug = models.SlugField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Properties
    ip = models.CharField(max_length=512, blank=True, null=True)
    mac = models.CharField(max_length=512, blank=True, null=True)
    os = models.ForeignKey(OS, blank=True, null=True)
    cpu = models.CharField(max_length=512, blank=True, null=True)
    mem  = models.CharField(max_length=512, blank=True, null=True)

    # Related
    location = models.ForeignKey(Location, blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)
    #stats = models.ManyToManyField('stats.Stat', blank=True, null=True)
    ssh_keys = models.ManyToManyField('access.Access', blank=True, null=True)
    services = models.ManyToManyField('services.Service', blank=True, null=True)

    # Metadata
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.name)

    class Meta:
        get_latest_by = 'created'


@receiver(pre_save, sender=Host)
def slugify_host_name(sender, **kwargs):
    host = kwargs['instance']
    host.slug = slugify(host.name)

