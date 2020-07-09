from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from account.models import Profile


class Order(models.Model):
    ORDER_TYPE = [
        ('Sprzedaż', 'sell'),
        ('Kupno', 'buy'),
        ('Wymiana', 'trade'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('marketplace:detail', args=[self.pk, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Order, self).save(*args, **kwargs)

class Message(models.Model):
    user_from = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    user_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='messages')
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return 'Wiadomość od {} do {} dotycząca {} o {}'.format(self.user_from, self.user_to, self.order, self.post_date)