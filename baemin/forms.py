from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, shop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_set'].queryset = self.fields['item_set'].queryset.filter(shop=shop)

    class Meta:
        model = Order
        fields = ('item_set',)
