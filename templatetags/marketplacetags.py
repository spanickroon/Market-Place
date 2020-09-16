from django import template

register = template.Library()


@register.simple_tag
def multiplying_values(number: float, factor: int, *args, **kwargs):
    return number * factor
