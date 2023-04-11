from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import (
    PostSerializer
)
from ..models import Post

class PostsPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 2

class AllPostsView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(state='published').order_by('-date_created')
    pagination_class = PostsPagination

class PostDetailView(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

    def get(self, request, slug):
        post = self.get_object()
        serializer = self.serializer_class(post)
        return Response(serializer.data)
