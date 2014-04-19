#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
# import the logging library
import logging

from django.views.generic.base import TemplateView

from signals import *
from models import UserAccount


logger = logging.getLogger(__name__)


class Index(TemplateView):
    template_name = "accounts/index.html"

    def get_context_data(self, **kwargs):

        context = super(Index, self).get_context_data(**kwargs)


