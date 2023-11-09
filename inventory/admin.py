from django.contrib import admin

from inventory.models import Tool, StaffEquipment, Supplies


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'codigo']
    search_fields = ['name', 'codigo']
    autocomplete_fields = ['owner']


@admin.register(StaffEquipment)
class StaffEquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'codigo']
    search_fields = ['name', 'codigo']


@admin.register(Supplies)
class SuppliesAdmin(admin.ModelAdmin):
    list_display = ['name', 'codigo']
    search_fields = ['name', 'codigo']
