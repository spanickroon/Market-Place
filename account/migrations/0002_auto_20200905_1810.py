# Generated by Django 3.0.8 on 2020-09-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(blank=True, default=10000, null=True, verbose_name='Balance'),
        ),
        migrations.AddField(
            model_name='profile',
            name='deals_amount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Amount of deals'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dividend_income',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Dividend income'),
        ),
    ]