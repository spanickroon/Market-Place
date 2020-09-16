from django import template

register = template.Library()


@register.simple_tag
def multiplying_values(number: float, factor: int, *args, **kwargs) -> str:
    if type(number) == int:
        return f'{number * factor}'
    return f'{number * factor:.4f}'
