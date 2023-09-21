from django.contrib import admin
from .models import Arta

#admin.site.register(Arta)
@admin.register(Arta)
class ArtaAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'desc')
