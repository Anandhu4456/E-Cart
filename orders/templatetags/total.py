from django import template

register= template.Library()

@register.simple_tag(name='total')
def total(cart):
    sum = 0
    for item in cart.added_items.all():
        sum += item.quantity * item.product.price
    return sum