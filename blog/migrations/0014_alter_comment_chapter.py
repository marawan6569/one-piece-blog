# Generated by Django 3.2.4 on 2021-06-16 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comment_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='chapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.chapter'),
        ),
    ]
