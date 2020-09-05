from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        verbose_name="User")

    avatar_binary = models.BinaryField(
        verbose_name="Avatar binary", blank=True, editable=False)

    class Meta:
        """Meta data."""
        db_table = 'Users'
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        """Funtion for output info about this profile object."""
        return self.user.username
