'''This module contain functions for authentication.'''

import json
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from ..models import Stock


class MarketPlaceHandler:

    @staticmethod
    def get_stocks() -> list:
        return [stock for stock in Stock.objects.all()]
