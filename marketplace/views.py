from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string

from account.forms import ChangePasswordForm, EditProfileInfo
from account.services.authentication import AuthenticationHandler
from .services.marketplace import MarketPlaceHandler


class StocksView(View):

    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        return render(
            request, template_name='index.html',
            context={
                'stocks': MarketPlaceHandler.get_stocks(1),
                'stocks_pages': MarketPlaceHandler.get_stocks_pages()})

    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def post(self: object, request: object) -> object:
        if request.POST['message'] == 'buy':
            return MarketPlaceHandler.post_buy_stock(request)
        else:
            return MarketPlaceHandler.post_display_stocks(request)


class ProfileView(View):

    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def get(self: object, request: object) -> object:
        return render(
            request, template_name='index.html',
            context={
                'user': request.user,
                'mystocks': MarketPlaceHandler.get_my_stocks(request.user)})

    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def post(self: object, request: object) -> object:
        return MarketPlaceHandler.post_sell_stock(request)


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

    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def post(self: object, request: object) -> object:
        change_password_form = ChangePasswordForm(request.POST)

        if change_password_form.is_valid():
            return AuthenticationHandler.change_password_handler(
                request, change_password_form)

        return JsonResponse(
            {'message': AuthenticationHandler.form_erors(
                change_password_form)})


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

    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='login'))
    def post(self: object, request: object) -> object:

        edit_profile_info = EditProfileInfo(request.POST)

        if edit_profile_info.is_valid():
            return AuthenticationHandler.edit_pofile_handler(
                request, edit_profile_info)

        return JsonResponse(
            {'message': AuthenticationHandler.form_erors(
                edit_profile_info)})
