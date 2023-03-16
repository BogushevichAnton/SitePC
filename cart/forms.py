from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,6)]

class CartAddPCForm(forms.Form):
    quantity = forms.TypedChoiceField(label="Количество", choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.NumberInput(
                                attrs={'type':'number', 'class':'col-md-5', 'min':'1', 'max':'5'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)