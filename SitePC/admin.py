from django.contrib import admin

from .models import *


class PCAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'price', 'cat_id')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


class CPUAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'socket')
    search_fields = ('title', 'socket')
    list_display_links = ('id', 'title')


class video_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')


class videoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    list_display_links = ('id', 'title')


class ramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type')
    search_fields = ('title', 'type')
    list_display_links = ('id', 'title')


class motherAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'socket')
    search_fields = ('title', 'socket')
    list_display_links = ('id', 'title')


class dataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'memory')
    search_fields = ('title', 'memory')
    list_display_links = ('id', 'title')


class OCAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    list_display_links = ('id', 'title')
class ItemInline(admin.StackedInline):
    model = Orders_PCs
    count = 0
    extra = count
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'user_first_name', 'user_last_name', 'user_phone')
    inlines = [ItemInline]

    search_fields = ('user__email', 'user__mobile',)
    list_display_links = ('id', 'user')
    readonly_fields = ['date',]

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

    def user_phone(self, obj):
        return obj.user.mobile

class orders_statusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')

admin.site.register(orders_status, orders_statusAdmin)
admin.site.register(PC, PCAdmin)
admin.site.register(Oper_System_type, OCAdmin)
admin.site.register(data_drives, dataAdmin)
admin.site.register(Motherboard, motherAdmin)
admin.site.register(Ram, ramAdmin)
admin.site.register(Video_Cards, videoAdmin)
admin.site.register(video_cards_type, video_typeAdmin)
admin.site.register(CPUs, CPUAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Orders, OrdersAdmin)
