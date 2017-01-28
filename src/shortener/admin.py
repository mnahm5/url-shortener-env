from django.contrib import admin

# Register your models here.
from .models import ShortenedUrl

admin.site.register(ShortenedUrl)
