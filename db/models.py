# flake8: noqa

import datetime
import uuid

from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class ChoreQuerySet(models.QuerySet):
    def due_today(self):
        today = timezone.now().date()
        return self.filter(next_due_date__lte=today)

    def due_next_three_days(self):
        next_three_days = timezone.now().date() + timezone.timedelta(days=3)
        return self.filter(next_due_date__lte=next_three_days)


class Chore(models.Model):
    ordering = ['-next_due_date']
    assignees = [
        (0, 'Alex'),
        (1, 'Marissa')
    ]

    objects = ChoreQuerySet.as_manager()

    id            = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name          = models.CharField(max_length=80)
    assignee      = models.IntegerField(choices=assignees)
    cadence       = models.PositiveSmallIntegerField(choices=[(0, 'Weekly'), (1, 'Monthly')])
    next_due_date = models.DateField()

    def __str__(self):
        return self.name

    @property
    def is_overdue(self):
        today = timezone.now().date()
        return self.next_due_date < today

    def find_next_due_date(self):
        if self.cadence == 0:
            return self.next_due_date + timezone.timedelta(days=7)
        elif self.cadence == 1:
            return self.next_due_date + relativedelta(months=+1)
        else:
            return ValueError(f'unexpected cadence type {self.cadence}')


class Campaign(models.Model):
    id      = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name    = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Contact(models.Model):

    id            = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name          = models.CharField(max_length=120)
    address       = models.TextField(blank=True)
    mailing_lists = models.ManyToManyField(Campaign)

    def __str__(self):
        return self.name
