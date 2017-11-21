from django import template
register = template.Library()

@register.filter
def ip():
    import sys
    return sys.argv[-1]