import calendar
import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Chore(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, max_length=300)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    last_completed = models.DateField(auto_now_add=True, editable=False)
    next_due = models.DateField(null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, now=None, **kwargs):
        now = now or timezone.now()
        self.last_completed = now
        self.next_due = self.find_next_due_date(now=now)
        super(Chore, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class WeeklyChore(Chore):
    day_of_the_week = models.PositiveSmallIntegerField(
        verbose_name='Day of the Week',
        choices=[(i, calendar.day_name[i]) for i in range(7)]
    )

    def find_next_due_date(self, now=None):
        days_ahead = self.day_of_the_week - now.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return now + datetime.timedelta(days_ahead)


class MonthlyChore(Chore):
    day_of_the_month = models.PositiveSmallIntegerField(
        verbose_name='Day of the Month',
        choices=[(i, i) for i in range(1, 29)]
    )

    def find_next_due_date(self, now=None):
        if now.day > self.day_of_the_month:
            now_month, now_year = now.month, now.year

            if now_month == 12:
                now_month = 1
                now_year += 1
            else:
                now_month += 1

            return now.replace(
                day=self.day_of_the_month,
                month=now_month,
                year=now_year
            )

        return now + datetime.timedelta(self.day_of_the_month - now.day)
