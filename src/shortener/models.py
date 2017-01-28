from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from .utils import code_generated, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortenedUrlManager(models.Manager):

    def all(self, *args, **kwargs):
        qs = super(ShortenedUrlManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_short_codes(self):
        qs = ShortenedUrl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shorCode = create_shortcode(q)
            print(q.shorCode)
            q.save()
            new_codes += 1
        return "New Codes made : {i}".format(i=new_codes)

class ShortenedUrl(models.Model):
    url = models.CharField(max_length=220)
    shortCode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = ShortenedUrlManager()

    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortCode is None or self.shortCode == "":
            self.shortCode = create_shortcode(self)
        super(ShortenedUrl, self).save(*args, **kwargs)

# Create your models here.
