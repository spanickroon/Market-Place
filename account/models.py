from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        verbose_name='User')

    avatar = models.ImageField(
        default='img/profiles/profile.png',
        verbose_name='Avatar',
        upload_to='img/profiles', null=True, blank=True)

    balance = models.FloatField(
        default=5000, blank=True,
        null=True, verbose_name='Balance')

    deals_amount = models.IntegerField(
        default=0, blank=True,
        null=True, verbose_name='Amount of deals')

    dividend_income = models.FloatField(
        default=0, blank=True,
        null=True, verbose_name='Dividend income')

    class Meta:
        """Meta data."""
        db_table = 'Profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        """Funtion for output info about this profile object."""
        return self.user.username
