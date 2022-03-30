from django.contrib import admin

# Register your models here.
from references.models import RefTitles, RefVersions, Elements


class RefTitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'description')


admin.site.register(RefTitles, RefTitlesAdmin)
admin.site.register(RefVersions)
admin.site.register(Elements)

admin.site.site_title = 'Админ-панель справочников'
