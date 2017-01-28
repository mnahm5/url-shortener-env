from __future__ import unicode_literals
import random
import string

from django.db import models

class ShortenedUrl(models.Model):
    url = models.CharField(max_length=220)
    shortCode = models.CharField(max_length=20, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        print("something")
        self.shortCode = code_generated()
        super(ShortenedUrl, self).save(*args, **kwargs)


def code_generated(size=6, chars=string.ascii_lowercase + string.digits):
    code = ''
    for _ in range(size):
        code += random.choice(chars)
    return code



# Create your models here.
