from django.conf.urls import url

from . import views

urlpatterns = [

    url('trending/keywords/history/', views.trending_keyword_history, name='trending-keywords-history'),
    url('trending/keywords/', views.trending_keywords, name='trending-keywords'),

    url('fake/', views.fake_data, name='fake-data'),
]