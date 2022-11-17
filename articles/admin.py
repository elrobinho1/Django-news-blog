from django.contrib import admin
from .models import Article, Comment

# Customize how Comment model's items display on the admin panel
class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "comment", "author")
    list_filter = ("author",)


# Customize how Comment model's items display on the admin panel
""" Note:
we could just replace TabularInline with StackedInline to
get each field in its own line"""


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # No extra comment rows


# Customize how Article model's items display on the admin panel
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("date", "author")
    inlines = [
        CommentInline,
    ]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
