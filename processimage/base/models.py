import uuid

from django.db import models
from django.utils import timezone


class AbstractBaseModel(models.Model):

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    created_at = models.DateTimeField(default=timezone.now)
    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
