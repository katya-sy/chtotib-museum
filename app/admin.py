from django.contrib import admin
from .models import *


admin.site.register(Section)
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
