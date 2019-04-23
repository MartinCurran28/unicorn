from django.conf.urls import url
from .views import all_debug, bug_details, bug_like, free_debug, form_view, join_us

urlpatterns = [
    url(r'^$', all_debug, name='all_debug'),
    url(r'^(?P<pk>\d+)/$', bug_details, name='bug_details'),
    url(r'^/(?P<pk>[0-9]+)/like/$', bug_like, name='bug_like'),
    url(r'^(?P<pk>\d+)/$', free_debug, name='free_debug'),
    url(r'^form/', form_view, name='form_view'),
    url(r'^join_us/', join_us, name='join_us')
    ]    