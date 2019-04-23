from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile, get_posts, post_detail, create_or_edit_post
from accounts import url_reset

urlpatterns = [
    url(r'^index/', index, name="index"),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="register"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^password-reset/', include(url_reset), name="password_reset")
]