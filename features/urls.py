from django.conf.urls import url
from .views import all_debug, bug_details, free_debug

urlpatterns = [
    url(r'^$', all_debug, name='all_debug'),
    url(r'^(?P<pk>\d+)/$', bug_details, name='bug_details'),
    url(r'^(?P<pk>\d+)/$', free_debug, name='free_debug'),
    ]    