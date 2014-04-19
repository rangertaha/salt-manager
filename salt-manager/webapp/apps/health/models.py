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


class Article(models.Model):
    """
    """
    title = models.CharField(max_length=512, blank=True, null=True)
    slug = models.SlugField(max_length=512, blank=True, null=True)
    subtitle = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    background = models.CharField(max_length=256, choices=settings.BACKGROUND, blank=True, null=True)

    # Related
    #videos = models.ManyToManyField('videos.Video', blank=True, null=True)
    manpages = models.ManyToManyField('manuals.ManPage', blank=True, null=True)

    # Metadata
    rank = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    public = models.BooleanField(default=False)
    fpage = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.title)

    class Meta:
        get_latest_by = 'created'


@receiver(pre_save, sender=Article)
def slugify_page_title(sender, **kwargs):
    article = kwargs['instance']
    article.slug = slugify(article.title)

