import calendar
import uuid

from django.db import models
from django.contrib.auth.models import User


class Chore(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, max_length=300)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    last_completed = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class WeeklyChore(Chore):
    day_of_the_week = models.PositiveSmallIntegerField(
        verbose_name='Day of the Week',
        choices=[(i, calendar.day_name[i]) for i in range(7)]
    )


class MonthlyChore(Chore):
    day_of_the_month = models.PositiveSmallIntegerField(
        verbose_name='Day of the Month',
        choices=[(i, i) for i in range(1, 29)]
    )
