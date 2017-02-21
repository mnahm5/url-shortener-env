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
        context = {
            "title": "Submit URL",
            "form": form
        }
        template = "shortener/home.html"

        if form.is_valid():
            url = form.cleaned_data.get("url")
            obj, created = ShortenedUrl.objects.get_or_create(url=url)
            context = {
                "object": obj,
                'created': created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-e.html"

        return render(request, template, context)

class ShortenedUrlRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenedUrl, shortCode=shortcode)
        return HttpResponseRedirect(obj.url)