from django.db import models
from django.contrib.auth.models import User
from drfsite.settings import BASE_URL

import string
import random


def create_short_url():

    t = "".join(random.sample(string.ascii_letters, 13))
    # return f'http://127.0.0.1:8000/short/{t}'
    return f'{BASE_URL}/short/{t}'


class Url(models.Model):
    original = models.CharField(max_length=455, blank=False)
    short = models.CharField(max_length=455, blank=False, default=create_short_url)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.original

