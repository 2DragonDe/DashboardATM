from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    PostDeleteView,
    blogtest
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('blogwizard/', blogtest, name='blog-wizard'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]