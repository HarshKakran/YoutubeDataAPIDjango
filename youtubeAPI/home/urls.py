from django.urls import path
from django.urls.resolvers import URLPattern
from .views import search_results

app_name = 'home'

urlpatterns = [
    path('', search_results, name="search"),
]