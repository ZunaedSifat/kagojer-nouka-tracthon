from django.contrib import admin
from django.urls import path, include
from kagojer_nouka.views import ping


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework_social_oauth2.urls')),

    # endpoint for testing the state of the server
    path('ping/', ping, name='ping_test')
]
