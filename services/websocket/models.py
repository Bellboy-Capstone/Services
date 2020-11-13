# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="logged_in_user", on_delete=CASCADE
    )
