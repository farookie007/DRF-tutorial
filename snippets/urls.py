from django.urls import path

from .views import (
    SnippetList,
    SnippetDetail,
    UserList,
    UserDetail,
    }


urlpatterns = [
    path("", SnippetList.as_view(), name="snippet_list"),
    path("<int:pk>/", SnippetDetail.as_view(), name="snippet_detail"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
]
