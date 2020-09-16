'''This module contain functions for authentication.'''

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
from ..models import Stock, MyStock
from account.models import Profile

from django.core.paginator import Paginator


class MarketPlaceHandler:

    @staticmethod
    def get_stocks(page: int) -> object:
        return Paginator(Stock.objects.all(), 8).page(page)

    @staticmethod
    def get_stocks_pages() -> list:
        return [i + 1 for i in range(math.ceil(len(Stock.objects.all()) / 8))]

    @staticmethod
    def get_my_stocks(user: object) -> object:
        return MyStock.objects.filter(user=user)

    @staticmethod
    def buy_stock(request: object) -> str:
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
            profile.save()
        else:
            return 'Insufficient funds'

        return 'ok'

    @staticmethod
    def post_buy_stock(request):
        return JsonResponse({
            'message': MarketPlaceHandler.buy_stock(request),
            'profile': f'{request.user}, {request.user.profile.balance}$',
            'template': render_to_string(
                request=request, template_name='marketplace/stocks.html')})

    @staticmethod
    def post_display_stocks(request):
        page = request.POST['active_page']
        return JsonResponse({'message': 'ok', 'template': render_to_string(
                request=request, template_name='marketplace/stocks.html',
                context={
                    'stocks': MarketPlaceHandler.get_stocks(page),
                    'stocks_pages': MarketPlaceHandler.get_stocks_pages()})})
