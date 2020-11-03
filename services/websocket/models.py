from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.base.AUTH_USER_MODEL, related_name='logged_in_user')