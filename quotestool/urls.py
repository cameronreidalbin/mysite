from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.input, name='input'),
    path('results/', views.results, name='results')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)