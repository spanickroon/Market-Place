from django.db import models


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
