# Generated by Django 3.2.4 on 2021-06-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_chapter_chapter_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='en_name',
            field=models.CharField(default='c', max_length=50, verbose_name='en_name'),
            preserve_default=False,
        ),
    ]
