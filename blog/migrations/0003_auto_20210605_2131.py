# Generated by Django 3.2.4 on 2021-06-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_chapter_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chapter',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
