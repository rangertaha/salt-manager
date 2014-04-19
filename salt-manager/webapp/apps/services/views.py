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

class ServiceList(ListView):
    """
    """
    model = Service
    template_name = "services/list.html"
    context_object_name = "services"
    paginate_by = 15

    def get_queryset(self):
        try:
            return Service.objects.filter(active=True, title__icontains=self.request.GET['q']).distinct()
        except:
            return Service.objects.filter(active=True).distinct()

    def get_context_data(self, **kwargs):
        context = super(ServiceList, self).get_context_data(**kwargs)
        #context['sections'] = Section.objects.filter(active=True).distinct()
        return context


class ServiceDetail(DetailView):
    """
    """
    model = Service
    template_name = "services/detail.html"
    context_object_name = "service"

    def get_context_data(self, **kwargs):
        context = super(ServiceDetail, self).get_context_data(**kwargs)
        #context['sections'] = Section.objects.filter(active=True).distinct()
        return context



class ServiceUpdate(UpdateView):
    """
    """
    model = Service
    form_class = ServiceForm
    template_name = "services/update.html"
    context_object_name = "update_form"
    #success_url = "/services/{0}/".format(model.slug)




