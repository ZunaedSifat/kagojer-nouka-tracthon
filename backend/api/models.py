from django.db import models, transaction, IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from faker import Faker
from random import choice, uniform
from api.keyword import get_keywords
from api import cache
from itertools import permutations


faker = Faker('en_US')


MIN_DOCUMENT_COUNT_TO_FORM_A_CLUSTER = 2


def get_combinations(n, r):
    result = set()
    for perm in permutations(list(range(n))):
        result.add(tuple(sorted(perm[:r])))

    return result


class Content(models.Model):
    text = models.TextField('text')
    uploader_id = models.BigIntegerField('uploader_id', default=0, blank=True)
    upload_date = models.DateField('upload date')

    def save(self, *args, **kwargs):
        if not self.id and not self.upload_date:
            self.upload_date = timezone.now().date()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_fake(cls):
        try:
            with transaction.atomic():
                return cls.objects.create(
                    text=faker.paragraph(nb_sentences=30),
                    upload_date=faker.past_date(tzinfo=timezone.get_current_timezone()),
                )
        except IntegrityError:
            return cls.generate_fake()


class Keyword(models.Model):
    word = models.CharField('key word', max_length=128)
    content = models.ForeignKey(Content, related_name='keywords', on_delete=models.CASCADE)
    weight = models.DecimalField('unit price', decimal_places=3, max_digits=5)

    def __str__(self):
        return f'Keyword: {self.word}'

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


class Cluster(models.Model):
    name = models.CharField(max_length=100, default='Untitled Cluster')
    keywords = models.ManyToManyField(to=Keyword, related_name='clusters')

    def __str__(self):
        return f'Cluster: {self.name}'


def create_cluster_from_keywords(keyword_list):
    cluster = Cluster()
    cluster.save()
    for keyword in keyword_list:
        cluster.keywords.add(keyword)
    cluster.save()
    return cluster


@receiver(post_save, sender=Content)
def my_handler(sender, **kwargs):
    content = kwargs['instance']
    keywords = get_keywords(content.text)

    keyword_instances = [
        Keyword.objects.create(
            word=word,
            weight=weight,
            content=content
        ) for word, weight in keywords
    ]
    for instance in keyword_instances:
        cache.KeywordCache.get_instance().set(keyword=instance)

    for combination in get_combinations(len(keyword_instances), 3):
        keyword_list = [keyword_instances[idx] for idx in combination]
        if not cache.ClusterCache.get_instance().is_present(keywords=keyword_list) and \
                cache.KeywordCache.get_instance().count(keyword_list) > MIN_DOCUMENT_COUNT_TO_FORM_A_CLUSTER:
            cache.ClusterCache.get_instance().create(keywords=keyword_list)
