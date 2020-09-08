from django.urls import path
from .views import show, about, contact, page
urlpatterns = [
    path('', show),
    path('home', show),
    path('about', about),
    path('contact', contact),
    path('page/<slug:slug>', page)
]