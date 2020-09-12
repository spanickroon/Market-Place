"""This module contain classes for work with forms."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """LoginForm class for login."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    """SignupForm class with meta data for signup."""

    class Meta:
        """Meta data."""

        model = User
        fields = ('username', 'password1', 'password2')


class ChangePasswordForm(UserCreationForm):
    """PasswordChangeForm class with meta data for password change."""

    class Meta:
        """Meta data."""

        model = User
        fields = ('password1', 'password2')
