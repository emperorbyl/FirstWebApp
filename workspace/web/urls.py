from django.conf.urls import url

from . import views
app_name = 'web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /blog
    url(r'^View All Blogs/$', views.bloglist, name='bloglist'),
    url(r'^View All Blogs/blog/(?P<blog_id>[0-9]+)/$', views.blog, name='blog'),
    url(r'^Add a new blog/$', views.new, name='new'),
    ]