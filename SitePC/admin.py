from django.contrib import admin

from .models import *



class PCAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content','price', 'cat_id')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    prepopulated_fields = {"slug":("title",)}
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug":("name",)}



admin.site.register(PC, PCAdmin)
admin.site.register(Category, CategoryAdmin)
