from django.contrib import admin
from .models import Chapter, Arc, Author, Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'chapter', 'body', 'active', 'created_on']
    list_filter = ['chapter', 'created_on', 'active']
    search_fields = ['name', 'body', 'email']
    actions = ['enable_comments', 'disable_comments']

    def enable_comments(modeladmin, request, queryset):
        queryset.update(active=True)

    def disable_comments(modeladmin, request, queryset):
        queryset.update(active=False)


admin.site.register(Chapter)
admin.site.register(Arc)
admin.site.register(Author)

admin.site.register(Comment, CommentAdmin)
