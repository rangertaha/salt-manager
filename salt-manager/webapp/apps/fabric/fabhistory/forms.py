#!/bin/env python
"""
"""
# import the logging library
import logging

from django.forms import ModelForm
from django.conf import settings

from models import *

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AccessForm(ModelForm):
    class Meta:
        model = Access
        #fields = ['']
        exclude = ['active', 'private_key']

    def __init__(self, *args, **kwargs):
        super(AccessForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'span4 inline'})
        self.fields['password'].widget.attrs.update({'class' : 'span4 inline'})
        self.fields['note'].widget.attrs.update({'class' : 'span12', 'style':'height:100px;'})
        #self.fields['private_key'].widget.attrs.update({'class' : 'span12', 'rows':'4'})
        self.fields['public_key'].widget.attrs.update({'class' : 'span12', 'rows':'4'})

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )