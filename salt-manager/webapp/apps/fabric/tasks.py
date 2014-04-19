#!/usr/bin/env python
"""
"""
import logging

from celery import task

from models import *
from signals import *
from forms import *

# Get an instance of a logger
logger = logging.getLogger(__name__)


@task()
def add(x, y):
    return x + y





