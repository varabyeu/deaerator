from django.contrib import admin

from initial_data.models import InitialData


@admin.register(InitialData)
class InitialDataAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'productivity_max', 'water_temperature', 'notes']
    list_filter = ['productivity_max', 'date']
    actions_selection_counter = True
    date_hierarchy = 'date'

