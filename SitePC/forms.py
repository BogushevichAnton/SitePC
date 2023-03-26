from django import forms
from .models import *

class HelpForm(forms.ModelForm):

    message = forms.CharField(label='Ваше сообщение', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Ваше сообщение'}))
    class Meta:
        model = Help
        fields = ['message', ]
class ReviewsForm(forms.ModelForm):
    message = forms.CharField(label='Ваш отзыв', widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Ваш отзыв', 'rows':'2', 'cols':'50', 'maxlength':'255'}))
    class Meta:
        model = Reviews
        fields = ['message', ]
