from django.template import Library
register = Library()
from meny.models import Meny

from index.models import SalesFeatures

@register.simple_tag
def get_navbar():
    meny_list = Meny.objects.order_by('created_at')
    meny_list_main = Meny.objects.filter(is_main=True)
    last_s_index = len(meny_list_main) - 2
    context = {
        'meny_list': meny_list,
        'last_second_index': last_s_index
    }
    return meny_list



@register.simple_tag
def get_sale():
    sales_list = SalesFeatures.objects.all()
    return sales_list



