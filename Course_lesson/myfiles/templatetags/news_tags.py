from django import template

from ..models import Course

register = template.Library()


@register.simple_tag
def all_categories():
    return Course.objects.all()