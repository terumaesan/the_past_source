from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}),
    url(r'^profile/$', views.user_profile, name='user_profile'),
]
