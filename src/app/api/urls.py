from django.urls import path
from .views import (
    GetAllChangesView, GetChangesByVersionView, PostUnversionedChangeView, PostBuildVersionView, GetWhatsNewView,
    GetAliveView, PostVersionedChangeView, GetAllBuildsView, GetStableBuildsView, GetLatestStableBuildView,
)


urlpatterns = [
    path("", GetAliveView.as_view(), name="root"),
    path("whats-new", GetWhatsNewView.as_view(), name="whats-new"),
    path("all-changes", GetAllChangesView.as_view(), name="all-changes"),
    path("builds", GetAllBuildsView.as_view(), name="builds"),
    path("builds/stable", GetStableBuildsView.as_view(), name="stable-builds"),
    path("builds/stable/latest", GetLatestStableBuildView.as_view(), name="latest-stable-build"),
    path("all-builds", GetAllBuildsView.as_view(), name="all-builds"),
    path("changes", GetAllChangesView.as_view(), name="changes"),
    path("changes/<str:version>", GetChangesByVersionView.as_view(), name="changes-by-version"),
    path("register-change", PostUnversionedChangeView.as_view(), name="register-change"),
    path("register-build", PostBuildVersionView.as_view(), name="register-build"),
    path("register-change-with-build", PostVersionedChangeView.as_view(), name="register-change-with-build"),
]