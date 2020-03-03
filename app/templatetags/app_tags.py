from django import template

register = template.Library()

@register.filter
def capitalize_first(value):

    return value.title()
