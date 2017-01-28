from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

def shortened_url_redirect_view(request, *args, **kwargs):
    return HttpResponse('Hello')

class ShortenedUrlRedirectView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')