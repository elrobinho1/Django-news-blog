from django.contrib import admin
from .models import Article

# Customize how model items display on the admin panel
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("date", "author")

    # prepopluate slug field based on title
    # prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Article, ArticleAdmin)
