from django.contrib import admin

from inventory.models import Tool, StaffEquipment, Supplies


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']


@admin.register(StaffEquipment)
class StaffEquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplies)
class SuppliesAdmin(admin.ModelAdmin):
    pass
