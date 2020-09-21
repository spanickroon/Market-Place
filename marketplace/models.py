"""Module with models."""
import json

from django.db import models
from account.models import User
from django.contrib.postgres.fields import ArrayField


class Stock(models.Model):
    """Stock model."""

    name = models.CharField(
        max_length=20, blank=True,
        null=True, verbose_name='Name')

    avatar = models.ImageField(
        default='img/stocks/stock.png',
        verbose_name='Avatar',
        upload_to='img/stocks', null=True, blank=True)

    cost = models.FloatField(
        default=0, blank=True,
        null=True, verbose_name='Cost')

    dividend_income = models.FloatField(
        default=0, blank=True,
        null=True, verbose_name='Dividend income')

    list_costs = models.TextField(
        default='[]',
        blank=False, null=True, verbose_name='List costs')

    def json_to_string(self, json_value):
        """String to json method."""
        self.list_costs = json.dumps(json_value)

    def string_to_json(self):
        """Json to string method."""
        return json.loads(self.list_costs)

    class Meta:
        """Meta data."""

        db_table = 'Stock'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

    def __str__(self) -> str:
        """Funtion for output info about this profile object."""
        return self.name


class MyStock(models.Model):
    """MyStock class with function output and meta data."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='User')

    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name='ID Stock')

    count = models.IntegerField(
        default=1, blank=True,
        null=False, verbose_name='Count')

    class Meta:
        """Meta data."""

        db_table = 'MyStock'
        verbose_name = 'MyStock'
        verbose_name_plural = 'MyStocks'

    def __str__(self):
        """Funtion for output info about this mystock object."""
        return f'{self.user.username} - {self.stock.name} - {self.count}'


class Notification(models.Model):
    """Stock model."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='User')

    datetime = models.DateTimeField(
        auto_now_add=True,
        blank=True, null=True, verbose_name='Time')

    cost = models.FloatField(
        default=0, blank=True,
        null=True, verbose_name='Cost')

    message = models.CharField(
        blank=True, null=True, verbose_name='Message',
        max_length=100)

    class Meta:
        """Meta data."""

        db_table = 'Notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self) -> str:
        """Funtion for output info about this profile object."""
        return f'{self.user} - {self.message}'


class StockGrowthRates(models.Model):
    """Stock model."""

    starting_multiplier = models.FloatField(
        default=1, blank=True,
        null=True, verbose_name='Starting multiplier')

    finite_factor = models.FloatField(
        default=1, blank=True,
        null=True, verbose_name='Finite factor')

    class Meta:
        """Meta data."""

        db_table = 'StockGrowthRates'
        verbose_name = 'StockGrowthRates'
        verbose_name_plural = 'StockGrowthRates'

    def __str__(self) -> str:
        """Funtion for output info about this profile object."""
        return f'{self.starting_multiplier} - {self.finite_factor}'
