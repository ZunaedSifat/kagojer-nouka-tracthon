# Generated by Django 3.1.1 on 2020-09-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200903_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='uploader_id',
            field=models.BigIntegerField(blank=True, default=0, verbose_name='uploader_id'),
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Cluster', max_length=100)),
                ('keywords', models.ManyToManyField(related_name='clusters', to='api.Keyword')),
            ],
        ),
    ]
