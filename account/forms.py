"""This module contain classes for work with forms."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """SignupForm class with meta data for signup."""

    class Meta:
        """Meta data."""

        model = User
        fields = ('username', 'password1', 'password2')
