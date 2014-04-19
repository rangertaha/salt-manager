#!/usr/bin/env python
"""
"""
from django.conf.urls import patterns, include, url

from views import Index, Donations, Disclaimer

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^donations/$', Donations.as_view(), name='donations'),
    url(r'^disclaimer/$', Disclaimer.as_view(), name='disclaimer'),

	url(r'accounts/', include('webapp.apps.accounts.urls')),
    url(r'services/', include('webapp.apps.services.urls')),
    url(r'hosts/', include('webapp.apps.hosts.urls')),
	
    #url(r'^logs/', include('webapp.apps.logs.urls')),
    #url(r'lamson', include('webapp.apps.lamson.urls')),
    #url(r'graphs', include('webapp.apps.graphs.urls')),
    url(r'fabric/', include('webapp.apps.fabric.urls')),
    #url(r'health', include('webapp.apps.health.urls')),
    #url(r'stats', include('webapp.apps.stats.urls')),
    #url(r'alerts', include('webapp.apps.alerts.urls')),
    #url(r'activity', include('webapp.apps.activity.urls')),
)

