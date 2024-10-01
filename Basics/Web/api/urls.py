from Home.views import home,people
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/',home),
    path('person/',people)
]
