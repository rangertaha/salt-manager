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
from webapp.apps.pages.models import *

# Get an instance of a logger
logger = logging.getLogger(__name__)

class ArticleList(ListView):
    """
    """
    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 15

    def get_queryset(self):
        try:
            return Article.objects.filter(active=True, title__icontains=self.request.GET['q']).distinct()
        except:
            return Article.objects.filter(active=True).distinct()

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        #context['sections'] = Section.objects.filter(active=True).distinct()
        return context


class ArticleDetail(DetailView):
    """
    """
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        #context['sections'] = Section.objects.filter(active=True).distinct()
        return context



class ArticleUpdate(UpdateView):
    """
    """
    model = Article
    form_class = ArticleForm
    template_name = "articles/update.html"
    context_object_name = "update_form"
    #success_url = "/articles/{0}/".format(model.slug)




