#!/usr/bin/env python
"""
"""
import logging

import django.dispatch

# Get an instance of a logger
logger = logging.getLogger(__name__)


fabric_connection_stderr = django.dispatch.Signal(providing_args=["code", "host", "stderr"])
"""
    Usage:

"""


fabric_connection_stdout = django.dispatch.Signal(providing_args=["code", "host", "stdout"])
"""
    Usage:

"""