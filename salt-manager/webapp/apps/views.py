#!/usr/bin/env python
"""
"""
import logging

from django.views.generic.base import TemplateView

from signals import *
from models import *
from settings import *


logger = logging.getLogger(__name__)


class Index(TemplateView):
    template_name = "index.html"


class Disclaimer(TemplateView):
    template_name = "disclaimer.html"


class Donations(TemplateView):
    template_name = "donations.html"
