#!/bin/env python
#-*- coding:utf-8 -*-
"""
"""
# import the logging library
import logging

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from models import *
from signals import *
from forms import *


# Get an instance of a logger
logger = logging.getLogger(__name__)

class HostList(ListView):
    """
    """
    model = Host
    template_name = "hosts/list.html"
    context_object_name = "hosts"
    #paginate_by = 15

    def get_queryset(self):
        try:
            return Host.objects.filter(active=True, name__icontains=self.request.GET['q']).distinct()
        except:
            return Host.objects.filter(active=True).distinct()

    def get_context_data(self, **kwargs):
        context = super(HostList, self).get_context_data(**kwargs)
        return context


class HostDetail(DetailView):
    """
    """
    model = Host
    template_name = "hosts/detail.html"
    context_object_name = "host"

    def get_context_data(self, **kwargs):
        context = super(HostDetail, self).get_context_data(**kwargs)
        return context



class HostUpdate(UpdateView):
    """
    """
    model = Host
    form_class = HostForm
    template_name = "hosts/update.html"
    context_object_name = "update_form"
    #success_url = "/hosts/{0}/".format(model.slug)




