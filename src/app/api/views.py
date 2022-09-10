from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import (
    PostBuildVersionSerializer, PostChangeSerializer,
    GetChangeSerializer, PostChangeWithBuildSerialiazer,
    GetBuildSerializer
)
from ..models import Change, BuildVersion
from ..versioner import add_version_to_unversioned_changes



class PostBuildVersionView(GenericAPIView):
    serializer_class = PostBuildVersionSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        add_version_to_unversioned_changes()

        return Response(serializer.data)


class PostUnversionedChangeView(GenericAPIView):
    serializer_class = PostChangeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class PostVersionedChangeView(GenericAPIView):
    serializer_class = PostChangeWithBuildSerialiazer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class GetChangesByVersionView(ListAPIView):
    serializer_class = GetChangeSerializer
    pagination_class = None

    def get_queryset(self):
        version = self.kwargs['version']
        return Change.objects.filter(build__version_number=version)


class GetAllChangesView(ListAPIView):
    serializer_class = GetChangeSerializer
    queryset = Change.objects.all().exclude(build=None)


class GetAllBuildsView(ListAPIView):
    serializer_class = GetBuildSerializer
    queryset = BuildVersion.objects.all()
    pagination_class = None


class GetWhatsNewView(ListAPIView):
    serializer_class = GetChangeSerializer
    pagination_class = None

    def get_queryset(self):
        return Change.objects.filter(build=self.get_latest_build())

    def get_latest_build(self) -> BuildVersion | None:
        return BuildVersion.objects.last()

    def get(self, request, *args, **kwargs):
        data = {
            "build": self.get_latest_build().version_number if self.get_latest_build() else None,
            "changes": self.list(request, *args, **kwargs).data,
        }
        return Response(data)


class GetAliveView(GenericAPIView):

    def get(self, request):
        response = {"message": "It's alive!"}
        return Response(response)
