from django.conf.urls import url, include
from .views import get_user, create_or_edit_user


urlpatterns = [
    url(r'^$', get_user, name='get_user'),
    url(r'^new/$', create_or_edit_user, name='new_user'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_user, name='edit_user'),
]