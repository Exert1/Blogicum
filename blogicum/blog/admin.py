from django.contrib import admin

from . import models

admin.site.empty_value_display = 'Не задано'


class PostInline(admin.TabularInline):
    model = models.Post
    extra = 0


class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 0


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    list_filter = ('is_published',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    list_filter = ('is_published',)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
    )
    list_display = (
        'title',
        'is_published',
        'pub_date',
        'author',
        'location',
        'category'
    )
    list_editable = (
        'is_published',
        'pub_date',
        'category',
        'location',
    )
    list_filter = ('is_published', 'category', 'location')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'post',
        'created_at',
        'author'
    )
    list_filter = ('post', 'author')
