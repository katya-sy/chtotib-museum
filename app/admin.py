from django.contrib import admin
from .models import *


admin.site.register(TimePeriod)
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
