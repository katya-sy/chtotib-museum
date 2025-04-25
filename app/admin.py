from django.contrib import admin
from .models import *

admin.site.register(Tradition)
admin.site.register(TraditionImage)


@admin.register(MainPageContent)
class SingletonModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview')
    readonly_fields = ('preview',)

    def has_add_permission(self, request):
        return MainPageContent.objects.count() == 0

    def has_delete_permission(self, request, obj=None):
        return False

    def preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" height="100" />', obj.image.url)
        return "-"
    preview.short_description = "Превью"


@admin.register(Section)
class SingletonModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.pk <= 4:
            return False
        return super().has_delete_permission(request, obj)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.pk <= 4:
            return super().get_readonly_fields(request, obj) + ('slug', "icon")
        return super().get_readonly_fields(request, obj)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        from django import forms
        if db_field.name == "icon":
            kwargs['widget'] = forms.ClearableFileInput(attrs={'accept': '.svg'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(TimePeriod)
class SingletonModelAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if 'slug' in fields:
            fields.remove('slug')
        return fields


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1
    fields = ('image', 'cover')
    readonly_fields = ('article',)

    def preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" height="100" />', obj.image.url)
        return "-"
    preview.short_description = "Превью"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline]
    list_display = ('title', 'section', 'time_period')
    list_filter = ('section', 'time_period')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('article', 'preview', 'cover')
    list_filter = ('article', 'cover')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" height="100" />', obj.image.url)
        return "-"
    preview.short_description = "Превью"

