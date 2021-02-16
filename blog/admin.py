from blog.models import Article, Tag
from django.contrib import admin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published',)
    list_display_links = ('id', 'title',)
    list_filter = ('published','tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
