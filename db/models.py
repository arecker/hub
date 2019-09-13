# flake8: noqa

import datetime
import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
        

class User(AbstractBaseUser):

    USERNAME_FIELD  = 'email'
    EMAIL_FIELD     = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    id           = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email        = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    last_login   = models.DateTimeField(blank=True, null=True, editable=True)
    date_joined  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.get_short_name()
    
    @property
    def is_active(self):
        return True

    def get_short_name(self):
        name, _ = self.email.split('@')
        return name.capitalize()

    def get_full_name(self):
        return self.get_short_name()


class ChoreQuerySet(models.QuerySet):
    def due_today(self):
        today = timezone.now().date()
        return self.filter(next_due_date__lte=today)

    def due_next_three_days(self):
        next_three_days = timezone.now().date() + timezone.timedelta(days=3)
        return self.filter(next_due_date__lte=next_three_days)


class Chore(models.Model):
    ordering = ['-next_due_date']

    objects = ChoreQuerySet.as_manager()

    id            = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name          = models.CharField(max_length=80)
    assignee      = models.ForeignKey(User, on_delete=models.CASCADE)
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
            pass
        else:
            return ValueError(f'unexpected cadence type {self.cadence}')
