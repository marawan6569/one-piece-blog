from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

def slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str
# Create your models here.

class Chapter(models.Model):
    author = models.ForeignKey(User,related_name='chapter_author' ,verbose_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='chapter_title')
    en_name = models.CharField(max_length=50, verbose_name='en_name') # name to use in  url like chapter 1
    chapter = models.TextField(verbose_name='chapter')
    image = models.ImageField(upload_to='chapter_img', verbose_name='chapter_image')
    arc = models.ForeignKey('Arc',related_name='chapter_arc', verbose_name='arc',on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='chapter_number')
    published_at = models.DateTimeField(default=timezone.now, verbose_name='published_at')
    views = models.IntegerField(default=0, verbose_name='views')
    active = models.BooleanField(default=True, verbose_name='active')
    slug = models.SlugField(null=True, blank=True, unique=True, allow_unicode=True, verbose_name=('slug'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{self.arc.name}-' + slugify(self.en_name)
        super(Chapter, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("blog:chapter_detail", kwargs={"slug": self.slug})


    def add_view(self):
        if self.views is not None:
            self.views += 1
        else:
            self.views = 0

    def __str__(self):
        return self.title

class Arc(models.Model):
    name = models.CharField(max_length=30, verbose_name='arc_name')
    image = models.ImageField(upload_to='arc_img', verbose_name='arc_image')
    number = models.IntegerField(verbose_name='arc_number')

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.ForeignKey(User, related_name='author_user', on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name='author_name')
    description = models.CharField(max_length=250, verbose_name='author_description')
    image = models.ImageField(upload_to='author_img', verbose_name='author_img')
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE,related_name='comments')
    replies = models.ManyToManyField('self', related_name='replies')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Commented {self.body} by {self.name}'
