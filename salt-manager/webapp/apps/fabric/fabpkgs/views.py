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

"""
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

"""





class FabricPackagesList(ListView):
    """
    """
    model = FabricPackage
    template_name = "fabpkgs/list.html"
    context_object_name = "accesses"
    #paginate_by = 15

    def get_queryset(self):
        try:
            return FabricPackage.objects.filter(username__icontains=self.request.GET['q']).distinct()
        except:
            return FabricPackage.objects.all().distinct()

    def get_context_data(self, **kwargs):
        context = super(FabricPackagesList, self).get_context_data(**kwargs)
        context['section'] = 'access'
        return context


class FabricPackagesDetail(DetailView):
    """
    """
    model = FabricPackage
    template_name = "fabpkgs/detail.html"
    context_object_name = "fabric"

    def get_context_data(self, **kwargs):
        context = super(FabricPackagesDetail, self).get_context_data(**kwargs)
        return context


class FabricPackagesDelete(DeleteView):
    model = FabricPackage
    template_name = "fabpkgs/delete.html"
    success_message = "fabric_packages"
    success_url = reverse_lazy('fabric_packages_list')

    def get_queryset(self):
        qs = super(FabricPackagesDelete, self).get_queryset()
        return qs


class FabricPackagesCreate(CreateView):
    model = FabricPackage
    form_class = FabricPackageForm
    template_name = "fabpkgs/form.html"
    success_message = "fabric_packages"
    success_url = reverse_lazy('fabric_packages_list')

    def get_queryset(self):
        qs = super(FabricPackagesCreate, self).get_queryset()
        return qs


class FabricPackagesUpdate(UpdateView):
    model = FabricPackage
    form_class = FabricPackageForm
    template_name = "fabpkgs/form.html"
    success_message = "fabric_packages"
    success_url = reverse_lazy('fabric_packages_list')

    def get_queryset(self):
        qs = super(FabricPackagesUpdate, self).get_queryset()
        return qs











