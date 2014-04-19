#!/usr/bin/env python
"""
"""
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
