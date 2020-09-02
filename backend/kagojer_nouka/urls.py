from django.contrib import admin
from django.urls import path
from kagojer_nouka.views import ping


urlpatterns = [
    path('admin/', admin.site.urls),

    # endpoint for testing the state of the server
    path('ping/', ping, name='ping_test')
]
