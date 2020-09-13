from unittest import mock

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.test import TestCase, RequestFactory
from django.urls import reverse
from marketplace.models import Order

from account.models import Profile

from marketplace.views import OrderList


class ManagingOrdersTestCase(TestCase):

    def setUp(self):
        user = Profile.objects.create(username="user", password="password")
        image = NamedTemporaryFile(suffix=".jpg").name
        self.orders = [Order.objects.create(name="order_%s"%i,
                                            description="desc_%s"%i,
                                            item_price=10*i,
                                            quantity=1*i+1,
                                            owner=user,
                                            image=image) for i in range(6)]


    def test_sort_lowest_price(self):
        request = self.client.get(reverse("marketplace:list"), {"sorting": "lowest_price"})
        context = request.context
        self.assertListEqual(context['orders'], self.orders)

    def test_sort_highest_price(self):
        request = self.client.get(reverse("marketplace:list"), {"sorting": "highest_price"})
        context = request.context
        orders = list(reversed(self.orders))
        self.assertListEqual(context['orders'], orders)

    def test_filter_price(self):
        request = self.client.get(reverse("marketplace:list"), {"price_min": 5, "price_max": 35})
        context = request.context
        self.assertCountEqual(list(context['orders']), self.orders[1:4])

    def test_filter_name(self):
        request = self.client.get(reverse("marketplace:list"), {"text_search": "order_3"})
        context = request.context
        self.assertEquals(1, len(context['orders']))
        self.assertEquals(context['orders'][0], self.orders[3])