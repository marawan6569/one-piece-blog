# Generated by Django 3.2.4 on 2021-06-08 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210608_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='arc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_arc', to='blog.arc', verbose_name='arc'),
        ),
    ]
