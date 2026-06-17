from django.urls import path
from .views import AllPostsView, PostDetailView, RulesPostsView

urlpatterns = [
    path('', AllPostsView.as_view(), name='blog'),
    path('rules', RulesPostsView.as_view(), name='rules'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]