# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import post_list, post_detail

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        post_detail, name='post_detail')
]
