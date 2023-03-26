from SitePC.models import *

menu = [{'title': 'О нас', 'url_name': 'about'},
        {'title': 'Отзывы', 'url_name': 'reviews'}]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context