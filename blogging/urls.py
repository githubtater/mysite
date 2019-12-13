#!/usr/bin/env python3

from django.urls import path, include, re_path
from rest_framework import routers
from blogging.views import stub_view, list_view, detail_view
from blogging import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'post', views.PostViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('', include(router.urls)),
    re_path(r'^accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]