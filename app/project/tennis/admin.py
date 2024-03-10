from django.contrib import admin
from .models import TennisSession, Resource, ArticleSection, Tag

# Register your models here.


class TennisSessionAdmin(admin.ModelAdmin):
    """"""
    list_display = ["title", "user", "category", "date", "is_completed"]
    list_filter = ["is_completed", "user", "category"]
    search_fields = ["title"]


admin.site.register(TennisSession, TennisSessionAdmin)
admin.site.register(Tag)
admin.site.register(Resource)
admin.site.register(ArticleSection)
