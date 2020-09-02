import os
import requests
from django.http import HttpResponse
from rest_framework.views import APIView
from messenger_bot.models import FacebookMessage


VERIFY_TOKEN = os.getenv('FACEBOOK_VERIFY_TOKEN')
PAGE_ACCESS_TOKEN = os.getenv('FACEBOOK_PAGE_ACCESS_TOKEN')
FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'


class MessengerWebhookAPIView(APIView):
    def verify_webhook(self):
        if self.request.query_params.get('hub.verify_token') == VERIFY_TOKEN:
            return HttpResponse(self.request.query_params.get('hub.challenge'))

        return HttpResponse("Incorrect verification token")

    @staticmethod
    def response_to_message(recipient_id, text):
        auth = {'access_token': PAGE_ACCESS_TOKEN}
        payload = {
            'message': {'text': text},
            'recipient': {'id': recipient_id},
            'notification_type': 'regular'
        }
        response = requests.post(
            FB_API_URL,
            params=auth,
            json=payload
        )

        return response.json()

    def get(self, request):
        return self.verify_webhook()

    @staticmethod
    def is_user_message(message):
        return (message.get('message') and
                message['message'].get('text') and
                not message['message'].get("is_echo"))

    @staticmethod
    def save_message_to_database(sender_id, timestamp, text):
        message = FacebookMessage(
            sender_id=sender_id,
            timestamp=timestamp,
            message=text
        )
        message.save()

    def post(self, *args, **kwargs):
        payload = self.request.data
        events = payload['entry'][0]['messaging']

        for event in events:
            if self.is_user_message(event):
                sender_id = event['sender']['id']
                timestamp = event['timestamp']
                text = event['message']['text']

                print(sender_id, timestamp, text)

                self.save_message_to_database(
                    sender_id=sender_id,
                    timestamp=timestamp,
                    text=text
                )

                self.response_to_message(
                    recipient_id=sender_id,
                    text=f'Reply to {text}'
                )

        return HttpResponse("OK")
