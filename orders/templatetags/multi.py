from django import template

register=template.Library()

@register.simple_tag(name='multi')
def multi(a,b):
    return a *b