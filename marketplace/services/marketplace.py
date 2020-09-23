"""This module contain functions for marketplace."""

import json
import math

from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.loader import render_to_string
from ..models import Stock, MyStock, Notification
from account.models import Profile

from django.core.paginator import Paginator


class MarketPlaceHandler:
    """The class that handles the main processes of the site."""

    @staticmethod
    def get_stocks(page: int) -> object:
        """Getting specific promotions based on page number."""
        return Paginator(Stock.objects.all(), 8).page(page)

    @staticmethod
    def get_stocks_pages() -> list:
        """Getting pages depending on the number of promotions."""
        return [i + 1 for i in range(math.ceil(len(Stock.objects.all()) / 8))]

    @staticmethod
    def get_my_stocks(user: object) -> object:
        """A function that returns the user's stocks."""
        return MyStock.objects.filter(user=user)

    @staticmethod
    def buy_stock(request: object) -> str:
        """Stock purchase processing function."""
        user = request.user
        stock_id = request.POST['stock_id'].split('-')[-1]
        stock = Stock.objects.get(id=stock_id)
        profile = Profile.objects.get(user=user)

        if stock.cost <= profile.balance:
            profile.balance -= stock.cost

            if MyStock.objects.filter(stock=stock).exists():
                mystock = MyStock.objects.get(stock=stock)
                mystock.count += 1
            else:
                mystock = MyStock(user=user, stock=stock, count=1)

            mystock.save()
            profile.deals_amount += 1
            profile.save()
        else:
            notification = Notification(
                user=user, cost=stock.cost,
                message=f'Unsuccessful purchase {stock.name}')
            notification.save()
            return 'Insufficient funds'

        profile.dividend_income = sum([
            mystock.stock.dividend_income * mystock.count
            for mystock in MyStock.objects.filter(user=request.user)])

        profile.save()

        notification = Notification(
                user=user, cost=stock.cost,
                message=f'Buy {stock.name}')
        notification.save()

        return 'ok'

    @staticmethod
    def post_buy_stock(request: object) -> object:
        """Balance update after purchase."""
        return JsonResponse({
            'message': MarketPlaceHandler.buy_stock(request),
            'profile': f'{request.user}, {request.user.profile.balance:.2f}$',
            'template': render_to_string(
                request=request, template_name='marketplace/stocks.html')})

    @staticmethod
    def post_display_stocks(request: object) -> object:
        """Displaying stocks on the page."""
        page = request.POST['active_page']
        return JsonResponse({'message': 'ok', 'template': render_to_string(
                request=request, template_name='marketplace/stocks.html',
                context={
                    'stocks': MarketPlaceHandler.get_stocks(page),
                    'stocks_pages': MarketPlaceHandler.get_stocks_pages()})})

    @staticmethod
    def sell_stock(request: object) -> str:
        """Sale of stocks."""
        profile = Profile.objects.get(user=request.user)
        act, stock_id = request.POST['stock_id'].split('-')
        mystock = MyStock.objects.get(stock=stock_id)

        if act == 'sellall':
            profile.balance += (mystock.stock.cost * mystock.count)

            notification = Notification(
                user=request.user, cost=mystock.stock.cost * mystock.count,
                message=f'Sell {mystock.stock.name}. Count: {mystock.count}')

            mystock.delete()
        else:
            profile.balance += mystock.stock.cost

            notification = Notification(
                user=request.user, cost=mystock.stock.cost * mystock.count,
                message=f'Sell {mystock.stock.name}. Count: 1')

            mystock.count -= 1
            mystock.save()

            if mystock.count == 0:
                mystock.delete()

        profile.dividend_income = sum([
            mystock.stock.dividend_income * mystock.count
            for mystock in MyStock.objects.filter(user=request.user)])

        profile.deals_amount += 1
        profile.save()
        notification.save()

        return 'ok'

    @staticmethod
    def post_sell_stock(request: object) -> object:
        """Refreshing the page after purchase."""
        return JsonResponse({
            'message': MarketPlaceHandler.sell_stock(request),
            'template': render_to_string(
                request=request, template_name='marketplace/profile.html',
                context={'user': request.user, 'mystocks':
                            MarketPlaceHandler.get_my_stocks(request.user)})})

    @staticmethod
    def get_notifications(request: object) -> object:
        """Display notifications."""
        return Notification.objects.filter(
            user=request.user).order_by('-datetime')

    @staticmethod
    def get_values_stocks(request: object) -> list:
        """Getting information about stocks."""
        res = []
        for stock in Stock.objects.all():
            res.append({'name': stock.name, 'values': stock.string_to_json()})
        return res

    @staticmethod
    def post_request_stocks(request: object) -> object:
        """Displaying information about stocks on a profile."""
        return JsonResponse({
            'message': 'ok',
            'content': MarketPlaceHandler.get_values_stocks(request)})
