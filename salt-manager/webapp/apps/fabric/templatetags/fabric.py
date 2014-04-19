#!/usr/bin/env python
"""
"""
import logging

from django.template import Library

from .. models import *


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Get an instance of library
register = Library()


objs = []
def get_object(obj_id):
        obj = TreeObject.objects.get(pk=obj_id)
        if obj in objs:
            pass
        else:
            objs.append(obj)
            return objs


def serializable_object(node):
    "Recurse into tree to build a serializable object"
    try:
        obj = {
            'name': node.name,
            'children': [serializable_object(ch) for ch in node.children()]
        }
        return obj
    except:
        obj = {
            'name': node.name,
            'children': []
        }
        return obj


"""
@register.inclusion_tag('tree_object.html')
def tree_object(tid):
    tree = TreeObject.objects.get(pk=tid)
    type = TreeObject.OBJECT_TYPES
    return {'tree': tree
"""

@register.inclusion_tag('tree_object.html')
def tree_object(tid):
    tree = TreeObject.objects.get(pk=tid)
    type = TreeObject.OBJECT_TYPES
    return {'tree': tree}


@register.inclusion_tag('json_tree.html')
def json_tree_object(tid):
    tree = TreeObject.objects.get(pk=tid)
    type = TreeObject.OBJECT_TYPES
    return {'tree': tree}



@register.inclusion_tag('tree_typeahead.html')
def tree_typeahead(tid):
    trees = TreeObject.objects.all()
    return {'trees': trees}



