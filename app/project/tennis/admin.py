from django.contrib import admin
from .models import TennisSession, Resource, ArticleSection, Tag

# Register your models here.


class TennisSessionAdmin(admin.ModelAdmin):
    """"""
    list_display = ["title", "display_users",
                    "category", "date", "is_completed"]
    list_filter = ["is_completed", "users", "category"]
    search_fields = ["title"]

    def display_users(self, obj):
        return ', '.join([user.username for user in obj.users.all()])

    display_users.short_description = 'Users'


admin.site.register(TennisSession, TennisSessionAdmin)
admin.site.register(Tag)
admin.site.register(Resource)
admin.site.register(ArticleSection)
