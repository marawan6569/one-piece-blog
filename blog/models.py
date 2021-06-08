from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Chapter(models.Model):
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='chapter_title')
    chapter = models.TextField(verbose_name='chapter')
    image = models.ImageField(upload_to='chapter_img', verbose_name='chapter_image')
    arc = models.ForeignKey('Arc', verbose_name='arc',on_delete=models.CASCADE)
    number = models.IntegerField()
    published_at = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("blog:chapter_detail", kwargs={"pk": self.pk})


    def add_view(self):
        if self.views is not None:
            self.views += 1
        else:
            self.views = 0

    def __str__(self):
        return self.title

class Arc(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='arc_img', verbose_name='arc_image')
    number = models.IntegerField()

    def __str__(self):
        return self.name
