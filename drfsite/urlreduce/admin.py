from django.contrib import admin
from .models import Url


class AdminModel(admin.ModelAdmin):
    list_display = ('id', 'user', 'views', 'short')
    list_display_links = ('id', 'user',  'short')
    list_filter = ('user', 'original',)
    readonly_fields = ('views', )
    save_on_top = True


admin.site.register(Url, AdminModel)
