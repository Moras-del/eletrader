from django.core.files.temp import NamedTemporaryFile
from django.test import TestCase

from account.models import Profile
from django.urls import reverse

from message.models import Message

from marketplace.models import Order


class MessageTestCase(TestCase):

    def setUp(self):
        self.user1 = Profile.objects.create(username='user1', password='password')
        self.user2 = Profile.objects.create(username='user2', password='password')
        image = NamedTemporaryFile(suffix='.jpg').name
        order = Order.objects.create(id=1, name='order',
                                     slug='order',
                                     description='desc',
                                     item_price=10,
                                     quantity=1,
                                     owner=self.user1,
                                     image=image)
        for i in range(4):
            Message.objects.create(user_from=self.user1, user_to=self.user2, order=order, content='content_%s' % i)
        for i in range(4):
            Message.objects.create(user_from=self.user2, user_to=self.user1, order=order, content='content_%s' % i)

    def test_show_messages_as_owner(self):
        self.client.force_login(user=self.user1, backend=None)
        response = self.client.get(reverse('message:messages-owner', args=[1, 'order', 'user2']))
        context = response.context
        self.assertEquals(len(context['messages']), 8)
        self.assertEquals(response.status_code, 200)

    def test_show_messages_as_customer(self):
        self.client.force_login(user=self.user2, backend=None)
        response = self.client.get(reverse('message:messages-customer', args=[1, 'order']))
        context = response.context
        self.assertEquals(len(context['messages']), 8)
        self.assertEquals(response.status_code, 200)

    def test_add_message_as_owner(self):
        self.client.force_login(user=self.user1, backend=None)
        response = self.client.post(reverse('message:messages-owner', args=[1, 'order', 'user2']),
                                    data={'content': 'content_5'})
        self.assertEquals(len(Message.objects.all()), 9)
        self.assertEquals(response.status_code, 200)

    def test_add_message_as_customer(self):
        self.client.force_login(user=self.user2, backend=None)
        response = self.client.post(reverse('message:messages-customer', args=[1, 'order']),
                                    data={'content': 'content_5'})
        self.assertEquals(len(Message.objects.all()), 9)
        self.assertEquals(response.status_code, 200)
