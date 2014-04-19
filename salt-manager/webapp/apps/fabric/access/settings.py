#!/usr/bin/env python
"""
"""
import os

from django.conf import settings


DIRNAME = os.path.abspath(os.path.dirname(__file__))

REG_TEMPLATE_DIR = (
os.path.join(DIRNAME, 'templates'),
os.path.join(DIRNAME, 'templatetags'),
    )

settings.TEMPLATE_DIRS += REG_TEMPLATE_DIR
