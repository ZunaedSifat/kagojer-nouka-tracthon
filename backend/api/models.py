from django.db import models, transaction, IntegrityError
from django.utils import timezone
from faker import Faker
from random import choice, randint, uniform

faker = Faker('en_US')


class Content(models.Model):

    text = models.TextField('text')
    upload_datetime = models.DateTimeField('upload datetime')

    def save(self, *args, **kwargs):
        if not self.id and not self.upload_datetime:
            self.upload_datetime = timezone.now()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_fake(cls):
        try:
            with transaction.atomic():
                return cls.objects.create(
                    text=faker.paragraph(nb_sentences=30),
                    upload_datetime=faker.past_datetime(tzinfo=timezone.get_current_timezone()),
                )
        except IntegrityError:
            return cls.generate_fake()


class Keyword(models.Model):

    word = models.CharField('key word', max_length=128)
    content = models.ForeignKey(Content, related_name='keywords', on_delete=models.CASCADE)
    weight = models.DecimalField('unit price', decimal_places=3, max_digits=5)

    @classmethod
    def generate_fake(cls, cont=None):
        try:
            with transaction.atomic():
                return cls.objects.create(
                    word=faker.word(),
                    weight=uniform(0, 1),
                    content=cont or choice(Content.objects.all())
                )
        except IntegrityError:
            return cls.generate_fake()
        except IndexError:
            Content.generate_fake()
            return cls.generate_fake(cont)
