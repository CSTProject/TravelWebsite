from django import template

register = template.Library()

#@register.filter(name='cut')
def cut(value,arg):
    '''
    This cuts all value of arg from string
    :param value: it is value from which arg is to be removed
    :param arg:it is the value to be removed
    :return: value by replacing arg with ''
    '''

    return value.replace(arg,'')

register.filter('cut',cut)
# it takes two arguments one is name of filter and second argument is the function