from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        verbose_name='User')

    avatar_binary = models.BinaryField(
        verbose_name='Avatar binary', blank=True, editable=False)

    balance = models.IntegerField(
        default=10000, blank=True,
        null=True, verbose_name='Balance')

    deals_amount = models.IntegerField(
        default=0, blank=True,
        null=True, verbose_name='Amount of deals')

    dividend_income = models.IntegerField(
        default=0, blank=True,
        null=True, verbose_name='Dividend income')

    class Meta:
        """Meta data."""
        db_table = 'Users'
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        """Funtion for output info about this profile object."""
        return self.user.username
