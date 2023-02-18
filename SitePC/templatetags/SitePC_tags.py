from django import template
from SitePC.models import *

register = template.Library()

@register.simple_tag()
def get_PCs():
    return PC.objects.all()
#@register.simple_tag(name='getCats')
#def get_Categoryes(cat_selected = 0):
  #  return Category.objects.all()

@register.inclusion_tag('SitePC/list_cat.html')
def get_Categoryes(cat_selected=0):
    cats = Category.objects.all()
    return {"cats":cats, "cat_selected":cat_selected}