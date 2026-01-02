from django.contrib import admin

from .models import Post, Article


@admin.register(Post)
@admin.register(Article)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['id', 'content']

    readonly_fields = ['content', 'created_at', 'updated_at']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'likes', 'is_featured', 'published_at']
    list_filter = ['is_featured', 'published_at', 'author', 'tags']
    search_fields = ['title', 'content']
    list_editable = ['is_featured']
    filter_horizontal = ['tags']
    readonly_fields = ['views', 'likes']

    actions = ['make_featured', 'reset_views', 'export_titles']

    @admin.action(description='Make featured')
    def make_featured(self, queryset):
        queryset.update(is_featured=True)

    @admin.action(description='Reset views')
    def reset_views(self, queryset):
        queryset.update(views=0)

    @admin.action(description='Export titles to text file') # Тут допоміг ШІ
    def export_titles(self, queryset):
        from django.http import HttpResponse

        titles = "\n".join([article.title for article in queryset])
        
        response = HttpResponse(titles, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="articles.txt"'
        return response