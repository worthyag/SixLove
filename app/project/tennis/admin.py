from django.contrib import admin
from .models import TennisSession, Resource, ArticleSection

# Register your models here.


class TennisSessionAdmin(admin.ModelAdmin):
    """"""
    list_display = ["title", "user", "date", "is_completed"]
    list_filter = ["is_completed", "user"]
    search_fields = ["title"]


admin.site.register(TennisSession, TennisSessionAdmin)
admin.site.register(Resource)
admin.site.register(ArticleSection)
