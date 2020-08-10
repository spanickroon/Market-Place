from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class LoginView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='authentication/login.html')


class SingupView(View):
    def get(self: object, request: object) -> object:
        return render(request, template_name='authentication/singup.html')
