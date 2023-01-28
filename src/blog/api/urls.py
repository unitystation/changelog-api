from django.urls import path
from .views import AllPostsView

urlpatterns = [
    path('', AllPostsView.as_view(), name='blogs')
]