'''This module contain functions for authentication.'''

import json
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.loader import render_to_string
from ..models import Stock, MyStock

from django.core.paginator import Paginator

import math


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
    def buy_stock(user: object) -> object:
        pass

    @staticmethod
    def post_buy_stock(request):
        pass

    @staticmethod
    def post_display_stocks(request):
        page = request.POST['active_page']
        return JsonResponse({'message': 'ok', 'template': render_to_string(
                request=request, template_name='marketplace/stocks.html',
                context={
                    'stocks': MarketPlaceHandler.get_stocks(page),
                    'stocks_pages': MarketPlaceHandler.get_stocks_pages()})})
