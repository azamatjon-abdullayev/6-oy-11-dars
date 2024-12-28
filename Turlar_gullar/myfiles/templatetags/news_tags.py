from django import template

from ..models import Turlar

register = template.Library()


@register.simple_tag
def all_categories():
    return Turlar.objects.all()