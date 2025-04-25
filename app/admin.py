from django.contrib import admin
from .models import *


admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(Tradition)
admin.site.register(TraditionImage)


@admin.register(MainPageContent)
class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return MainPageContent.objects.count() == 0

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Section)
class SingletonModelAdmin(admin.ModelAdmin):
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
