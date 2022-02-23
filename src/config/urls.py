from time import sleep

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from config.celery import app, health_check
from posts.models import HealthCheck


@app.task
def update_counter():
    sleep(3)
    instance = HealthCheck.objects.first()
    instance.counter += 1
    instance.save()
    print(f"Counter was updated: {instance.counter}")


def check(request):
    data = {"Hello": "World!"}

    update_counter.delay()

    health_check.delay()

    return JsonResponse(data)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health-check/", check),
    path("", include("posts.urls")),
]
