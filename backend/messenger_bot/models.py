from django.db import models


class FacebookMessage(models.Model):
    sender_id = models.BigIntegerField()
    timestamp = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return f'{self.sender_id} at {self.timestamp}: {self.message}'
