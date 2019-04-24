from django.conf.urls import url, include
from .views import all_services, service_like, homepage

urlpatterns = [
    url(r'^$', all_services, name = 'services'),
    url(r'^/(?P<pk>[0-9]+)/like/$', service_like, name='service_like'),
    url(r'^home/$', homepage, name = 'homepage'),
    ]