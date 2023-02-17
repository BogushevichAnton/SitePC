from django.contrib import admin

from .models import *

class PCAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content','price', 'cat_id')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')

admin.site.register(PC, PCAdmin)
