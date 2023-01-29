from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import (
    PostSerializer
)
from ..models import Post

class AllPostsView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination

class PostDetailView(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

    def get(self, request, slug):
        post = self.get_object()
        serializer = self.serializer_class(post)
        return Response(serializer.data)
