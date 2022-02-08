from django.urls import path

from .api import PostListCreateAPI, PostRetrieveUpdateDestroyAPI

app_name = "posts"

urlpatterns = [
    path("", PostListCreateAPI.as_view(), name="list"),
    path("<int:id>/", PostRetrieveUpdateDestroyAPI.as_view(), name="retrieve"),
]
