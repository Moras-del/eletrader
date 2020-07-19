from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image
from account.models import Profile
from numpy import reshape


class Order(models.Model):
    ORDER_TYPE = [
        ('Sprzedam', 'Sprzedam'),
        ('Kupię', 'Kupię'),
    ]

    ITEM_TYPE = [
        ('Układ scalony', 'Układ scalony'),
        ('Półprzewodnik', 'Półprzewodnik'),
        ('LED', 'LED'),
        ('Wyświetlacz', 'Wyświetlacz'),
        ('Element pasywny', 'Element pasywny'),
        ('Złącze', 'Złącze'),
    ]

    MAX_PRICE_VALUE = 9999

    owner = models.ForeignKey(Profile, related_name="orders", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)

    order_type = models.CharField(max_length=20, choices=ORDER_TYPE)
    item_type = models.CharField(max_length=40, choices=ITEM_TYPE)

    item_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=0)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('marketplace:detail', args=[self.pk, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Order, self).save(*args, **kwargs)

