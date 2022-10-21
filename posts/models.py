from email.policy import default
from operator import truediv
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
        