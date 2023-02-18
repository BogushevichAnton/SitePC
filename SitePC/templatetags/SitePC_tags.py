from django import template
from SitePC.models import *

register = template.Library()

@register.simple_tag()
def get_PCs():
    return PC.objects.all()
@register.simple_tag()
def get_Categoryes():
    return Category.objects.all()