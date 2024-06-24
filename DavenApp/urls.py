
from django.contrib import admin
from django.urls import path
from DavenApp import views

urlpatterns = [
    path('', admin.site.urls),
    path('home/', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
]
