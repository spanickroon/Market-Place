from django.shortcuts import render
from django.views import View


class StocksView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class ProfileView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class NotificationsView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class PasswordView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class StockGrowthView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class ExchangeRatesView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')
