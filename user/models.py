from django.contrib.auth.models import AbstractUser
from django.db import models

from kingdom.models import Kingdom


class CustomUser(AbstractUser):
    kingdom = models.ForeignKey(
        Kingdom, on_delete=models.SET_NULL, null=True, blank=True
    )
