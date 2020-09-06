'''This module contain functions for authentication.'''

import json
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse

from ..models import Profile


class AuthenticationHandler:

    @staticmethod
    def form_erors(signup_form: object) -> str:
        res = []
        for k, v in json.loads(signup_form.errors.as_json()).items():
            res.append(v[0]['message'])
        return ' '.join(res)

    @staticmethod
    def login_handler(request: object, login_form: object) -> object:
        request_username = login_form.cleaned_data['username']

        if not User.objects.filter(username=request_username).exists():
            return JsonResponse({'message': 'User not found'})

        user = User.objects.get(username=request_username)

        if not check_password(
                login_form.cleaned_data['password'],
                user.password):
            return JsonResponse({'message': 'Incorrect password'})

        login(request, user)

        return JsonResponse({'message': 'ok'})

    @staticmethod
    def signup_handler(request: object, signup_form: object) -> object:
        user = User(
            username=signup_form.cleaned_data['username'],
            password=make_password(signup_form.cleaned_data['password1'])
        )

        profile = Profile(
            user=user,
        )

        user.is_active = True
        user.save()
        profile.save()

        return JsonResponse({'message': 'ok'})
