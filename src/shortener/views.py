from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import ShortenedUrl

# Create your views here

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "title": "Submit URL",
            "form": form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        context = {
            "title": "Submit URL",
            "form": form
        }
        return render(request, "shortener/home.html", context)

class ShortenedUrlRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenedUrl, shortCode=shortcode)
        return HttpResponseRedirect(obj.url)