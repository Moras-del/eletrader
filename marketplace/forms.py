from enum import Enum

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

class SortForm(forms.Form):

    class SORTING_OPTIONS(Enum):

        def sort_orders(**kwargs):
            def inner(orders):
                return sorted(orders, **kwargs)
            return inner

        DATE_NEW = ('date_newest', 'Od najnowszych', sort_orders(key=lambda order: order.created, reverse=True))
        DATE_OLD = ('date_oldest', 'Od najstarszych', sort_orders(key=lambda order: order.created))
        PRICE_LOW = ('lowest_price', 'Od najtańszych', sort_orders(key=lambda order: order.item_price))
        PRICE_HIGH = ('highest_price', 'Od najdroższych', sort_orders(key=lambda order: order.item_price, reverse=True))

        def to_choices(self):
            return (self.value[0], self.value[1])

        @classmethod
        def get_function(cls, selected_option):
            options = list(map(lambda e: e.value, cls))
            return next(option[2] for option in options if option[0]==selected_option)

    sorting = forms.ChoiceField(choices=[option.to_choices() for option in SORTING_OPTIONS], required=False)

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

class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'description', 'item_price', 'quantity')
        labels = {
            'name': 'Nazwa produktu',
            'order_type': 'Rodzaj ogłoszenia',
            'item_type': 'Rodzaj produktu',
            'description': 'Opis ogłoszenia',
            'image': 'Zdjęcie produktu',
            'item_price': 'Cena za sztukę',
            'quantity': 'Ilość produktów',
        }

