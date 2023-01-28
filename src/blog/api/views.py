from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from .serializers import (
    PostSerializer
)
from ..models import Post

class AllPostsView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()