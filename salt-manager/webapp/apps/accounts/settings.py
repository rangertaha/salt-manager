#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from django.conf import settings
import os

DIRNAME = os.path.abspath(os.path.dirname(__file__))

REG_TEMPLATE_DIR = (
    os.path.join(DIRNAME, 'templates'),
    )

settings.TEMPLATE_DIRS += REG_TEMPLATE_DIR


settings.AUTH_PROFILE_MODULE = 'webapp.apps.accounts.UserAccount'

