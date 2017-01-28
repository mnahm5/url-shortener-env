from __future__ import unicode_literals

from django.db import models

class ShortenedUrl(models.Model):
    url = models.CharField(max_length=220)
    shortCode = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return str(self.url)




# Create your models here.
