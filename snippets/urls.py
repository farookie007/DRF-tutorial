from django.urls import path

from .views import SnippetList, SnippetDetail


urlpatterns = [
    path("", SnippetList.as_view(), name="snippet_list"),
    path("<int: pk>/", SnippetDetail.as_view(), name="snippet_detail"),
]
