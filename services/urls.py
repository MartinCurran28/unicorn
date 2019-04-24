from django.conf.urls import url, include
from .views import all_services, homepage

urlpatterns = [
    url(r'^$', all_services, name = 'services'),
    url(r'^home/$', homepage, name = 'homepage'),
    ]