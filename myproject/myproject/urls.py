#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.conf.urls import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = patterns('myproject.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", "month", name='month'),
    url(r"^month/(\d+)/(\d+)/$", "month", name='month'),
    url(r"^month$", "month", name='month'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", "day", name='day'),
    url(r"^settings/$", "settings", name='settings'),
    (r'^register/$', 'signup'),
    url(r"^(\d+)/$", "month", name='month'),
    url(r"^$", "month", name='month'), 
)

urlpatterns += patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'cal/login.html'}),
)

urlpatterns += staticfiles_urlpatterns()
