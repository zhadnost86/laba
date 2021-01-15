from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.posts_list, name='posts_list'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
]
