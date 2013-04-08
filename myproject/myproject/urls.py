#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('myproject.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", "month", name='month'),
    url(r"^month/(\d+)/(\d+)/$", "month", name='month'),
    url(r"^month$", "month", name='month'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", "day", name='day'),
    url(r"^settings/$", "settings", name='settings'),
    url(r"^(\d+)/$", "main", name='main'),
    url(r"", "main", name='main'), 
)
