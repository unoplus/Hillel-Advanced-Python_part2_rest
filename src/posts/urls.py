from django.urls import path

from posts.api import PostListCreateAPI, PostRetrieveUpdateDestroyAPI

app_name = "posts"

urlpatterns = [
    path("posts/", PostListCreateAPI.as_view(), name="list"),
    path("<int:id>/", PostRetrieveUpdateDestroyAPI.as_view(), name="retrieve"),
]
