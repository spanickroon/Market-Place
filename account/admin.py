"""This module contain class for work with model objects in admin panel."""

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    """Profile class with list of filters and meta data."""

    list_filter = ('user', )

    class Meta:
        """Meta data."""

        app_label = 'Profile'
        verbose_name = "Profile"
        base_manager_name = 'Profile'
        verbose_name_plural = "Profile"
        db_table = 'Profile'
        default_manager_name = 'Profile'

    def save_model(self, request, obj, form, change):
        """Conver avatar to avatar binary."""
        try:
            obj.avatar_binary = form.cleaned_data.get('avatar').read()
        except AttributeError:
            obj.avatar_binary = open('static/img/profile.svg', 'rb').read()
        obj.save()

