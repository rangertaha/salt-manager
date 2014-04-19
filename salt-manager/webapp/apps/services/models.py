#!/usr/bin/env python
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


class Service(models.Model):
    """
    """
    name = models.CharField(max_length=512, blank=True, null=True)
    slug = models.SlugField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Related
    #stats = models.ManyToManyField('stats.Stat', blank=True, null=True)
    #alerts = models.ManyToManyField('alerts.Alert', blank=True, null=True)
    #logs = models.ManyToManyField('logs.Log', blank=True, null=True)

    # Metadata
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.name)

    class Meta:
        get_latest_by = 'created'


@receiver(pre_save, sender=Service)
def slugify_service_name(sender, **kwargs):
    service = kwargs['instance']
    service.slug = slugify(service.name)

