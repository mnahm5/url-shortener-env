from django.conf.urls import url
from .views import wild_card_redirect

urlpatterns = [
    url(r'^(?P<path>,*)', wild_card_redirect)
]
