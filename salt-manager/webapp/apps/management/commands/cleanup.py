#!/bin/python
"""
"""
from django.core.management.base import NoArgsCommand

import os

def cleanup_files():
	os.system('rm -vf `find ./ | grep .*.pyc`')
	os.system('rm -vf `find ./ | grep .*.py~`')
	os.system('rm -vf `find ./ | grep .*.html~`')
	os.system('rm -vf `find ./ | grep .*.txt~`')



class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		cleanup_files()



