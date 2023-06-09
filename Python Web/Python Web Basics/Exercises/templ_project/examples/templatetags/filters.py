from django import template

register = template.Library()

@register.filter(name='odd')
def show_only_odd(list_numbers):
    return [x for x in list_numbers if x % 2 != 0] 

@register.filter(name='vowels')
def show_only_vowels(list_vowels):
    return [l for l in list_vowels if l in 'aeiouy']
