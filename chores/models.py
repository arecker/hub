import uuid

from django.db import models
from django.contrib.auth.models import User


class Chore(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, max_length=300)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
