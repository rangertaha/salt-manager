#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
# import the logging library
from __future__ import unicode_literals
import logging

#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from django.db import models

# Get an instance of a logger
logger = logging.getLogger(__name__)


class UserAccount(models.Model):
    """
    """
    user = models.ForeignKey(User, unique=True)
    username = models.CharField(max_length=512, blank=True, null=True)
    slug = models.SlugField(max_length=512, blank=True, null=True)

    # Related

    # Metadata
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0}: {1}'.format(self.id, self.username)

    class Meta:
        get_latest_by = 'created'


@receiver(pre_save, sender=UserAccount)
def slugify_username(sender, **kwargs):
    user = kwargs['instance']
    user.slug = slugify(page.username)

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)