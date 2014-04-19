#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
"""
import logging

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from models import *
from signals import *
from forms import *
from tasks import *



# Get an instance of a logger
logger = logging.getLogger(__name__)


class FabricAccessList(ListView):
    """
    """
    model = Access
    template_name = "access/list.html"
    context_object_name = "accesses"
    #paginate_by = 15

    def get_queryset(self):
        try:
            return Access.objects.filter(username__icontains=self.request.GET['q']).distinct()
        except:
            return Access.objects.all().distinct()

    def get_context_data(self, **kwargs):
        context = super(FabricAccessList, self).get_context_data(**kwargs)
        context['section'] = 'access'
        return context


class FabricAccessDetail(DetailView):
    """
    """
    model = Access
    template_name = "access/detail.html"
    context_object_name = "fabric"

    def get_context_data(self, **kwargs):
        context = super(FabricAccessDetail, self).get_context_data(**kwargs)
        return context


class FabricAccessDelete(DeleteView):
    model = Access
    template_name = "access/delete.html"
    success_message = "fabric_access"
    success_url = reverse_lazy('fabric_access')

    def get_queryset(self):
        qs = super(FabricAccessDelete, self).get_queryset()
        return qs


class FabricAccessCreate(CreateView):
    model = Access
    form_class = AccessForm
    template_name = "access/form.html"
    success_message = "fabric_access"
    success_url = reverse_lazy('fabric_access')

    def get_queryset(self):
        qs = super(FabricAccessCreate, self).get_queryset()
        return qs


class FabricAccessUpdate(UpdateView):
    model = Access
    form_class = AccessForm
    template_name = "access/form.html"
    success_message = "fabric_access"
    success_url = reverse_lazy('fabric_access')

    def get_queryset(self):
        qs = super(FabricAccessUpdate, self).get_queryset()
        return qs







