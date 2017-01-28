from __future__ import unicode_literals

from django.db import models

from .utils import code_generated, create_shortcode

class ShortenedUrl(models.Model):
    url = models.CharField(max_length=220)
    shortCode = models.CharField(max_length=20, unique=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortCode is None or self.shortCode == "":
            self.shortCode = create_shortcode(self)
        super(ShortenedUrl, self).save(*args, **kwargs)



# Create your models here.
