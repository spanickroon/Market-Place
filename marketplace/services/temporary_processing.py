"""The module for executing processes in parallel with starting the server."""
from threading import Thread
import time
import datetime
import random

from marketplace.models import Stock, Notification, MyStock, StockGrowthRates
from account.models import Profile


def postpone(function):
    """Stream creation decorator function."""
    def decorator(*args, **kwargs):
        """Stream creation function."""
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


class Procesing:
    """Class for executing processes in parallel with starting the server."""

    @staticmethod
    @postpone
    def all_proccesing():
        """
        Function that launches parallel processes.

        With a clock cycle of 10 seconds.
        """
        while True:
            time.sleep(10)
            Procesing.accrural_of_income()
            Procesing.change_stock_prices()

    @staticmethod
    def change_stock_prices():
        """Stock price changes."""
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second

        for stock in Stock.objects.all():
            stock.cost = (stock.cost * random.uniform(
                StockGrowthRates.objects.all()[0].starting_multiplier,
                StockGrowthRates.objects.all()[0].finite_factor))
            stock.dividend_income = stock.cost * 0.001

            list_stoks = stock.string_to_json()
            if len(list_stoks) > 19:
                del list_stoks[0]

            list_stoks.append([f'{minute:02d}:{second:02d}', stock.cost])
            stock.json_to_string(list_stoks)
            stock.save()

    @staticmethod
    def accrural_of_income():
        """Foreign currency accruals of income."""
        for profile in Profile.objects.all():
            if profile.dividend_income != 0:
                notification = Notification(
                    user=profile.user,
                    cost=profile.dividend_income,
                    message='Deductions from dividends')

                profile.balance += profile.dividend_income
                profile.dividend_income = sum([
                    mystock.stock.dividend_income * mystock.count
                    for mystock in MyStock.objects.filter(user=profile.user)])
                profile.save()
                notification.save()
