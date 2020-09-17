from django.db import models
from account.models import User


class Stock(models.Model):
    name = models.CharField(
        max_length=20, blank=True,
        null=True, verbose_name='Name')

    avatar = models.ImageField(
        default='img/stocks/stock.png',
        verbose_name='Avatar',
        upload_to='img/stocks', null=True, blank=True)

    cost = models.IntegerField(
        default=0, blank=True,
        null=True, verbose_name='Cost')

    dividend_income = models.FloatField(
        default=0, blank=True,
        null=True, verbose_name='Dividend income')

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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='User')

    date = models.DateField(
        blank=True, null=True, verbose_name='Date')

    time = models.DateTimeField(
        blank=True, null=True, verbose_name='Time')

    cost = models.IntegerField(
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
