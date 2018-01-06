from django.contrib import admin

from .models import Menu, MenuEntry

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ('name', 'update_time', 'created', 'updated')


class MenuEntryAdmin(admin.ModelAdmin):
    model = MenuEntry
    list_display = ('name', 'price', 'created')
    ordering = ('-created', )


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuEntry, MenuEntryAdmin)