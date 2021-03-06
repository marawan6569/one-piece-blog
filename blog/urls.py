from django.contrib import admin
from django.urls import path

from .views import ChapterList,ChapterDetail,add_comment,add_reply


app_name = 'blog'

urlpatterns = [
    path('', ChapterList.as_view(), name='chapters'),
    path('<str:slug>', ChapterDetail.as_view(), name='chapter_detail'),
    path('ajax/add-comment', add_comment, name='add_comment'),
    path('ajax/add-reply', add_reply, name='add_reply'),
]
