from django.db.models import UUIDField

import uuid


class UUIDPKField(UUIDField):
    def __init__(self, *args, **kwargs):
        super(UUIDPKField, self).__init__(
            *args,
            primary_key=True,
            default=uuid.uuid4,
            editable=False
        )
