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
    filter_horizontal = ('skills',)
    list_display = ('user', 'phone_number')
    list_filter = ('user__is_active',)
    ordering = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('user__username',)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'email')


class ImageInline(admin.StackedInline):
    extra = 1
    model = models.Image


class TestimonyInline(admin.StackedInline):
    extra = 1
    model = models.Testimony


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    inlines = (ImageInline, TestimonyInline)
    filter_horizontal = ('tags',)
    list_display = ('title', 'developer', 'customer', 'start_date', 'end_date')
    list_filter = ('developer__user__is_active', 'developer', 'tags', 'start_date', 'end_date')
    ordering = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'developer__user__username')
