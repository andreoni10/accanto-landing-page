from django import forms
from django.core import validators


class FormContact(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'name': 'name', 'placeholder': 'Digite seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'id': 'email', 'name': 'email', 'placeholder': 'Digite seu email'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'id': 'telefone', 'name': 'telefone', 'placeholder': 'Digite seu telefone'}))
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={'id': 'message', 'name': 'message', 'placeholder': 'Digite sua mensagem', 'rows': "5"}))

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
