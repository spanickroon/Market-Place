from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from .forms import LoginForm, SignupForm
from .services.authentication import AuthenticationHandler


class LoginView(View):

    @method_decorator(csrf_protect)
    def get(self: object, request: object) -> object:
        logout(request)
        return render(request, template_name='index.html')

    @method_decorator(csrf_protect)
    def post(self: object, request: object) -> object:
        login_form = LoginForm(request.POST)
        print('USER POST')
        print(login_form.is_valid())
        print(login_form.errors)

        if login_form.is_valid():
            return AuthenticationHandler.login_handler(request, login_form)

        return JsonResponse(
            {'message': AuthenticationHandler.form_erors(login_form)})


class SingupView(View):

    @method_decorator(csrf_protect)
    def get(self: object, request: object) -> object:
        logout(request)
        return render(request, template_name='index.html')

    @method_decorator(csrf_protect)
    def post(self: object, request: object) -> object:
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            return AuthenticationHandler.signup_handler(request, signup_form)

        return JsonResponse(
            {'message': AuthenticationHandler.form_erors(signup_form)})
