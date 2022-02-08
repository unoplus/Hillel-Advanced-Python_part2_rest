from django.conf import settings
from django.db import models

from posts.utils import TimeStampMixin


class Post(TimeStampMixin):
    title = models.CharField(max_length=100)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODULE, null=True, blank=False, on_delete=models.SET_NULL)
    status = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.title
