from django.contrib import admin
from . import models


class BaseChoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignee', 'last_completed')


@admin.register(models.WeeklyChore)
class WeeklyChoreAdmin(BaseChoreAdmin):
    pass


@admin.register(models.MonthlyChore)
class MonthlyChoreAdmin(BaseChoreAdmin):
    pass
