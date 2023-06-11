from django import template

register = template.Library()

@register.filter
def is_admin(user):
    return user.groups.filter(name='admin').exists()

@register.filter
def is_editor(user):
    return user.groups.filter(name='editor').exists()