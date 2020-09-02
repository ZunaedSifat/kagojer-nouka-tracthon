import os
import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


VERIFY_TOKEN = os.getenv('FACEBOOK_VERIFY_TOKEN')
PAGE_ACCESS_TOKEN = os.getenv('FACEBOOK_PAGE_ACCESS_TOKEN')
FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'


class MessengerWebhookAPIView(APIView):
    def verify_webhook(self):
        print(self.request.query_params.get('hub.verify_token'))
        print(self.request.query_params.get('hub.challenge'))
        print(VERIFY_TOKEN)
        print(PAGE_ACCESS_TOKEN)

        if self.request.query_params.get('hub.verify_token') == VERIFY_TOKEN:
            return Response(
                data=self.request.query_params.get('hub.challenge'),
                status=status.HTTP_200_OK
            )

        return Response(
            data="Incorrect",
            status=status.HTTP_400_BAD_REQUEST
        )

    @staticmethod
    def send_messages(recipient_id, text):
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

    def post(self):
        print(self.request.data)
        return Response(
            data='OK',
            status=status.HTTP_200_OK
        )
