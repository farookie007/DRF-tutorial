from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    api_root,
    SnippetList,
    SnippetDetail,
    SnippetHighlight,
    UserList,
    UserDetail,
)


urlpatterns = [
    path("", api_root, name="api_root"),
    path("snippets/", SnippetList.as_view(), name="snippet_list"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet_detail"),
    path("snippets/<int:pk>/highlight", SnippetHighlight.as_view(), name="snippet_highlight"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
