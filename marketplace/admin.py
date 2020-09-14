"""This module contain class for work with model objects in admin panel."""

from django.contrib import admin
from .models import Stock


@admin.register(Stock)
class AuthorAdmin(admin.ModelAdmin):
    """Stock class with list of filters and meta data."""

    list_filter = ('name', )

    class Meta:
        """Meta data."""

        app_label = 'Stock'
        verbose_name = "Stock"
        base_manager_name = 'Stock'
        verbose_name_plural = 'Stock'
        db_table = 'Stock'
        default_manager_name = 'Stock'

    def save_model(self, request, obj, form, change):
        obj.save()
