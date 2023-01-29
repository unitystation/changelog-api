from django.urls import path
from .views import AllPostsView, PostDetailView

urlpatterns = [
    path('', AllPostsView.as_view(), name='blog'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]