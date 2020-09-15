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
from ..models import Stock

from django.core.paginator import Paginator

import math


class MarketPlaceHandler:

    @staticmethod
    def get_stocks(page: int) -> object:
        return Paginator(Stock.objects.all(), 8).page(page)

    @staticmethod
    def get_stocks_pages() -> list:
        return [i + 1 for i in range(math.ceil(len(Stock.objects.all()) / 8))]
