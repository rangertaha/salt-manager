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
from fab_tasks import  *


# Get an instance of a logger
logger = logging.getLogger(__name__)


class FabricIndex(TemplateView):
    template_name = "fabric/index.html"

    def get_context_data(self, **kwargs):
        context = super(FabricIndex, self).get_context_data(**kwargs)
        context['accesses'] = Access.objects.filter(active=True).distinct()
        return context


class ExecutionHistoryList(ListView):
    """
    """
    model = ExecutionHistory
    template_name = "fabric/list.html"
    context_object_name = "fabrics"
    paginate_by = 15

    def get_queryset(self):
        try:
            return ExecutionHistory.objects.filter(host__icontains=self.request.GET['q']).distinct()
        except:
            return ExecutionHistory.objects.all().distinct()

    def get_context_data(self, **kwargs):
        context = super(ExecutionHistoryList, self).get_context_data(**kwargs)
        return context


class ExecutionHistoryDetail(DetailView):
    """
    """
    model = ExecutionHistory
    template_name = "fabric/detail.html"
    context_object_name = "fabric"

    def get_context_data(self, **kwargs):
        context = super(ExecutionHistoryDetail, self).get_context_data(**kwargs)
        return context


