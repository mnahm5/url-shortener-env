from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

def shortened_url_redirect_view(request, shortcode=None, *args, **kwargs):
    return HttpResponse('Hello {shortcode}'.format(shortcode=shortcode))

class ShortenedUrlRedirectView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse('Hello World {shortcode}'.format(shortcode=shortcode))