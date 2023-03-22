from django import forms
from .models import *

class HelpForm(forms.ModelForm):

    message = forms.CharField(label='Ваше сообщение', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Ваше сообщение'}))
    class Meta:
        model = Help
        fields = ['message', ]
