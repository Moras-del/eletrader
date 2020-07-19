from django.db import models

# Create your models here.
from account.models import Profile
from marketplace.models import Order


class MessageManager(models.Manager):
    def get_queryset(self):
        return super(MessageManager, self).get_queryset().filter(is_active=True)

class Message(models.Model):
    user_from = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    user_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='messages')
    content = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active = MessageManager()

    class Meta:
        ordering = ('post_date',)

    def __str__(self):
        return 'Wiadomość od {} do {} dotycząca {} o {}'.format(self.user_from, self.user_to, self.order, self.post_date)