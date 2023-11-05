from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, SnippetViewSet



# setting up the router
router = DefaultRouter()
router.register(r"users", CustomUserViewSet, basename="customuser")
router.register(r"snippets", SnippetViewSet, basename="snippet")


urlpatterns = [
    path("", include(router.urls)),
]
