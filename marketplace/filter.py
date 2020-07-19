
from marketplace.models import Order


class OrderFilter:

    def __init__(self, query):
        self.text = query.get('text_search')
        self.price_max = query.get('price_max', Order.MAX_PRICE_VALUE)
        self.price_min = query.get('price_min', 0)
        self.order_type = query.get('order_type')
        self.item_type = query.get('item_type')

    def get_filtered_orders(self):
        return Order.objects.filter(order_type__contains=self.order_type,
                                    item_type__contains=self.item_type,
                                    item_price__lte=self.price_max,
                                    item_price__gte=self.price_min,
                                    name__contains=self.text)

    def __repr__(self):
        return "tekst = {}, cena min = {}, cena max = {}, rodzaje = {}".format(self.text, self.price_min, self.price_max, self.types)



