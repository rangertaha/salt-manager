#!/usr/bin/env python
"""
"""
import logging

import django.dispatch

# Get an instance of a logger
logger = logging.getLogger(__name__)


fabric_cmd_stderr = django.dispatch.Signal(providing_args=["code", "host", "stderr"])
"""
    Usage:

"""


fabric_cmd_stdout = django.dispatch.Signal(providing_args=["code", "host", "stdout"])
"""
    Usage:

"""