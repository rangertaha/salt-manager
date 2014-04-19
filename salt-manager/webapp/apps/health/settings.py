#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
import os

from django.conf import settings


DIRNAME = os.path.abspath(os.path.dirname(__file__))

REG_TEMPLATE_DIR = (
os.path.join(DIRNAME, 'templates'),
    )

settings.TEMPLATE_DIRS += REG_TEMPLATE_DIR
