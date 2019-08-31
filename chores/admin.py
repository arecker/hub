from django.contrib import admin
from . import models


@admin.register(models.WeeklyChore)
class WeeklyChoreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MonthlyChore)
class MonthlyChoreAdmin(admin.ModelAdmin):
    pass
