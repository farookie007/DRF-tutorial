from django.urls import path

from .views import (
    api_root,
    SnippetList,
    SnippetDetail,
    UserList,
    UserDetail,
)


urlpatterns = [
    path("", api_root, name="api_root"),
    path("snippets/", SnippetList.as_view(), name="snippet_list"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet_detail"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
]
