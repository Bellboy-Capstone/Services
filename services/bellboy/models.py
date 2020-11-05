import uuid

from django.contrib.postgres.fields import JSONField
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, UUIDField
from django.db.models.fields.related import ForeignKey


class BellboyDevice(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = DateTimeField(auto_now_add=True, editable=False)

    # Generate a unique key for the Bellboy unit to keep.
    # Better not to use the model's ID for this.
    identifier = UUIDField(default=uuid.uuid4, editable=False)


class StatusUpdate(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bellboy = ForeignKey(
        BellboyDevice, related_name="status_updates", on_delete=CASCADE
    )
    created = DateTimeField(auto_now_add=True, editable=False)

    # Stores the update content as a JSON blob.
    body = JSONField(default=dict)
