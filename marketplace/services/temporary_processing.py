from threading import Thread
import time
import datetime
import random

from marketplace.models import Stock, Notification, MyStock
from account.models import Profile


def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


class Procesing:

    @staticmethod
    @postpone
    def all_proccesing():
        while True:
            time.sleep(10)
            Procesing.accrural_of_income()
            Procesing.change_stock_prices()

    @staticmethod
    def change_stock_prices():
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second

        for stock in Stock.objects.all():
            stock.cost = (stock.cost * random.uniform(0.4, 2))
            stock.dividend_income = stock.cost * 0.01

            list_stoks = stock.string_to_json()
            if len(list_stoks) > 19:
                del list_stoks[0]
            list_stoks.append([f'{minute:02d}:{second:02d}', stock.cost])
            stock.json_to_string(list_stoks)
            stock.save()

    @staticmethod
    def accrural_of_income():
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
            print(profile.dividend_income)
