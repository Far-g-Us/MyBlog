from django.contrib import admin
from .models import Article

#admin.site.register(Arta)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
