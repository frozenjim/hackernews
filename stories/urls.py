"""
 stories.urls.py

"""

from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^$', 'stories.views.index')
]