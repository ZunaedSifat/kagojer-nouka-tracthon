from django.urls import path
from messenger_bot.views import MessengerWebhookAPIView


urlpatterns = [
    path('webhook/', MessengerWebhookAPIView.as_view(), name='messenger_bot_webhook'),
]
