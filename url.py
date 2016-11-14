from django.conf.urls import include,url
from django.contrib import admin

# urlpatterns = [
#     url(r'^create/$', "posts.views.posts_create"),
#     url(r'^update/$', "posts.views.posts_update"),
#     url(r'^$', "posts.views.posts_list"),
#     url(r'^delete/$', "posts.views.posts_delete"),
#     url(r'^detail/$', "posts.views.posts_detail"),
# ]
from .views import (
	posts_create,
	posts_update,
	posts_list,
	post_detail,
	posts_delete)

urlpatterns = [
    url(r'^create/$', posts_create),
    url(r'^(?P<id>\d+)/edit/$', posts_update),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^$', posts_list),
    url(r'^delete/$', posts_delete),
    # url(r'^(?P<id>\d+)/$', posts_detail),
]