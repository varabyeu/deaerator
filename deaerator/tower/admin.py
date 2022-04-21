from django.contrib import admin

from tower.models import InitialData


@admin.register(InitialData)
class InitialDataAdmin(admin.ModelAdmin):
    pass
# Register your models here.
