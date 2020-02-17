# flake8: noqa

import copy
import datetime
import os
import uuid

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField


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

    @property
    def next_due_delta(self):
        if self.cadence == 0:
            return timezone.timedelta(days=7)
        elif self.cadence == 1:
            return relativedelta(months=+1)
        else:
            raise ValueError(f'unexpected cadence type {self.cadence}')

    def find_next_due_date(self):
        today = timezone.now().date()
        next_due = copy.copy(self.next_due_date)

        if next_due > today:  # eager beaver, advance into future
            return next_due + self.next_due_delta
        else:  # slacker, keep advancing until caught up
            while not (next_due > today):
                next_due += self.next_due_delta

            return next_due


class Wallpaper(models.Model):
    id   = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=80, unique=True)
    image = ImageField(upload_to='wallpapers')

    def clean_fields(self, exclude=None):
        self.name = os.path.basename(self.image.path)
        return super(Wallpaper, self).clean_fields(exclude=exclude)

    def validate_unique(self, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        if Wallpaper.objects.filter(name=self.name).exists():
            raise ValidationError(f'{self.name} already exists')
        return super(Wallpaper, self).validate_unique(*args, **kwargs)

    def __str__(self):
        return self.name
