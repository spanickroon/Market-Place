from django import template

register = template.Library()


@register.simple_tag
def multiplying_values(number: float, factor: int, *args, **kwargs) -> str:
    return f'{number * factor:.2f}'
