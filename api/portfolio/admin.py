from django.contrib import admin

from portfolio import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(models.Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user__is_active',)
    ordering = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('user__username',)


class ImageInline(admin.StackedInline):
    extra = 1
    model = models.Image


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    filter_horizontal = ('tags', )
    list_display = ('title', 'developer', 'date')
    list_filter = ('developer__user__is_active', 'developer', 'tags', 'date')
    ordering = ('date', 'title')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'developer__user__username')
