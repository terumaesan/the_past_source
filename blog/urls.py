from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', 'blog.views.index', name='index'),
  url(r'^view/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),
  url(r'^category/(?P<slug>[^\.]+).html', 'blog.views.view_category', name='view_blog_category'),
]
