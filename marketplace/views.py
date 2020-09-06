from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


class StocksView(View):
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class ProfileView(View):
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        print(request.user.is_authenticated)
        return render(request, template_name='index.html')


class NotificationsView(View):
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class PasswordView(View):
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class StockGrowthView(View):
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')


class EditProfileView(View):
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        return render(request, template_name='index.html')
