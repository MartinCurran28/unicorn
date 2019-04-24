from django.conf.urls import url, include
from .views import get_app, create_or_edit_app


urlpatterns = [
    url(r'^$', get_app, name='get_app'),
    url(r'^new/$', create_or_edit_app, name='new_app'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_app, name='edit_app'),
]