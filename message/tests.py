from django.core.files.temp import NamedTemporaryFile
from django.test import TestCase

from account.models import Profile
from django.urls import reverse

from message.models import Message

from marketplace.models import Order


class MessageTestCase(TestCase):

    def setUp(self):
        self.user1 = Profile.objects.create(username="user1", password="password")
        self.user2 = Profile.objects.create(username="user2", password="password")
        image = NamedTemporaryFile(suffix=".jpg").name
        order = Order.objects.create(id=1, name="order",
                                    slug="order",
                                    description="desc",
                                    item_price=10,
                                    quantity=1,
                                    owner=self.user1,
                                    image=image)
        for i in range(4):
            Message.objects.create(user_from=self.user1, user_to=self.user2, order=order, content="content_%s"%i)
        for i in range(4):
            Message.objects.create(user_from=self.user2, user_to=self.user1, order=order, content="content_%s" % i)



    def test_messages_sender(self):
        self.client.force_login(user=self.user1, backend=None)
        request = self.client.get(reverse("message:answer", args=[1, "order", "user2"]))
        context = request.context
        self.assertEquals(8, len(context['messages']))

    def test_messages_receiver(self):
        self.client.force_login(user=self.user2, backend=None)
        request = self.client.get(reverse("message:messages", args=[1, "order"]))
        context = request.context
        self.assertEquals(8, len(context['messages']))

