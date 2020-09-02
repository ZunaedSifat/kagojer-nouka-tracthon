from django.db import models
from django.utils import timezone
from faker import Faker
from random import choice, randint

faker = Faker('en_US')


class Content(models.Model):

    text = models.TextField('text')
    upload_datetime = models.DateTimeField('upload datetime')

    def save(self, *args, **kwargs):
        if not self.id and not self.upload_datetime:
            self.upload_datetime = timezone.now()
        return super().save(*args, **kwargs)


class Keyword(models.Model):

    word = models.CharField('key word', max_length=128)
    content = models.ForeignKey(Content, related_name='keywords', on_delete=models.CASCADE)
    weight = models.DecimalField('unit price', decimal_places=3, max_digits=5)
