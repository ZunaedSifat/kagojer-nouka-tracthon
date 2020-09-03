from django.urls import path

from . import views

urlpatterns = [
    path('trending/keywords/', views.trending_keywords, name='trending-keywords'),
]