# Generated by Django 3.2.4 on 2021-06-18 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210618_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='replaying_to',
        ),
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(related_name='_blog_comment_replies_+', to='blog.Comment'),
        ),
    ]
