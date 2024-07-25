from django import template

register = template.Library()

@register.filter(name='replace_age')
def replace_age(value, age):
    return value.replace('{age}', str(age))
