from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def check(request):
    data = {"Hello": "World!"}
    return JsonResponse(data)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health-check/", check),
    path("posts/", include("posts.urls")),
]
