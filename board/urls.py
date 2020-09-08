from django.urls import path
from .views import show, about, contact
urlpatterns = [
    path('', show),
    path('home', show),
    path('about', about),
    path('contact', contact),
]