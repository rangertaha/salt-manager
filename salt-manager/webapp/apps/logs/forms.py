#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
# import the logging library
import logging

from django.forms import ModelForm
from django.conf import settings

from models import *

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        #fields = ['']
        exclude = ['active', 'slug', 'rank']
    """
    def __init__(self, *args, **kwargs):
        super(ManPageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'span12'})
        self.fields['subtitle'].widget.attrs.update({'class' : 'span12'})
        self.fields['body'].widget.attrs.update({'class' : 'span12', 'style':'height:800px;'})
        self.fields['description'].widget.attrs.update({'class' : 'span12', 'rows':'4'})
    """