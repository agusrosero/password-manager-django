from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Entry(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
