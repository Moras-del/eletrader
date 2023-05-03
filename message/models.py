from django.db import models

# Create your models here.
from account.models import Profile
from marketplace.models import Order

class Message(models.Model):
    user_from = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    user_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='messages')
    content = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()

    @staticmethod
    def get_active_messages(user):
        return Message.objects.filter(user_to=user, is_active=True)

    class Meta:
        ordering = ('post_date',)
    def __str__(self):
        return 'Message from {} to {} about {}'.format(self.user_from, self.user_to, self.order)