from django import forms
from django.forms import NumberInput

from marketplace.models import Order


class FilterForm(forms.ModelForm):
    text_search = forms.CharField(label="Szukaj", required=False)
    price_max = forms.IntegerField(label="Maksymalna cena", required=False)
    price_min = forms.IntegerField(label="Minimalna cena", required=False)

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['order_type'].required = False
        self.fields['order_type'].label = "Rodzaj ogłoszenia"
        self.fields['item_type'].required = False
        self.fields['item_type'].label = "Rodzaj produktu"


    class Meta:
        model = Order
        fields = ('order_type', 'item_type')


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'order_type', 'item_type', 'description', 'image', 'item_price', 'quantity')
        labels = {
            'name': 'Nazwa produktu',
            'order_type': 'Rodzaj ogłoszenia',
            'item_type': 'Rodzaj produktu',
            'description': 'Opis ogłoszenia',
            'image': 'Zdjęcie produktu',
            'item_price': 'Cena za sztukę',
            'quantity': 'Ilość produktów',
        }
