from threading import Thread
import time

from marketplace.models import Stock, Notification
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
            time.sleep(3)
            Procesing.accrural_of_income()

    @staticmethod
    def accrural_of_income():
        print(time.time())

        for profile in Profile.objects.all():
            if profile.dividend_income != 0:
                notification = Notification(
                    user=profile.user,
                    cost=profile.dividend_income,
                    message='Deductions from dividends')

                profile.balance += profile.dividend_income
                profile.save()
                notification.save()
