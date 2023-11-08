from django.contrib import admin

from plantation.models import Hectare, Batch


class BatchInline(admin.TabularInline):
    model = Batch
    extra = 1


@admin.register(Hectare)
class HectareAdmin(admin.ModelAdmin):
    inlines = [BatchInline]


