from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ShortenedUrl

# Create your views here

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {

        })

class ShortenedUrlRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenedUrl, shortCode=shortcode)
        return HttpResponseRedirect(obj.url)