# Generated by Django 3.2.4 on 2021-06-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210612_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.CharField(default='g', max_length=250, verbose_name='author_description'),
            preserve_default=False,
        ),
    ]