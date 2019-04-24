from django.conf.urls import url, include
from .views import get_form, create_or_edit_form


urlpatterns = [
    url(r'^$', get_form, name='get_form'),
    url(r'^new/$', create_or_edit_form, name='new_form'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_form, name='edit_form'),
]