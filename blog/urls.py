from django.contrib import admin
from django.urls import path

from .views import ChapterList,ChapterDetail


app_name = 'blog'

urlpatterns = [
    path('', ChapterList.as_view(), name='chapters'),
    path('<str:slug>', ChapterDetail.as_view(), name='chapter_detail'),
]
