from decimal import Decimal
from math import pi

from django.db.models import F, ExpressionWrapper, DecimalField
from django.db.models.functions import Sin, ATan2, Sqrt, Cos
from marketplace.models import Order


from marketplace.forms import SortForm


class OrderManagement:

    def __init__(self, orders):
        self.orders = orders

    def filter_orders(self, query):
        text = query.get('text_search')
        price_max = query.get('price_max', Order.MAX_PRICE_VALUE)
        price_min = query.get('price_min', 0)
        order_type = query.get('order_type')
        item_type = query.get('item_type')

        self.orders = Order.objects \
            .filter(order_type__contains=order_type,
                    item_type__contains=item_type,
                    item_price__lte=price_max,
                    item_price__gte=price_min,
                    name__contains=text)

        #
        # for order in orders:
        #     order.location = Location(order.latitude, order.longitude)
        #
        # orders = sorted(orders, key=lambda k:k.location.get_distance(user.get_location()))

    def sort_orders(self, query: dict):
        sort_option = query.get("sorting")
        func = SortForm.SORTING_OPTIONS.get_function(sort_option)
        self.orders = func(self.orders)

    def get_orders(self):
        return self.orders
