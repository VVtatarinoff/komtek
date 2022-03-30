from django.contrib import admin

# Register your models here.
from references.models import RefTitles, RefVersions, Elements


class RefTitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'description')


class ElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ref_version', 'code', 'value')


class RefVersionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'version', 'init_date')


admin.site.register(RefTitles, RefTitlesAdmin)
admin.site.register(RefVersions, RefVersionsAdmin)
admin.site.register(Elements, ElementsAdmin)

admin.site.site_title = 'Админ-панель справочников'
