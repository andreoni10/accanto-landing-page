from django import forms
from django.core import validators

class FormContact(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'name': 'name', 'placeholder': 'Digite seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'id': 'email', 'name': 'email', 'placeholder': 'Digite seu email'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'id': 'telefone', 'name': 'telefone', 'placeholder': 'Digite seu telefone'}))
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={'id': 'message', 'name': 'message', 'placeholder': 'Digite sua mensagem', 'rows': "5"}))
    data_consent = forms.BooleanField(
        required=True,
        label='Autorizo o uso dos meus dados pessoais para contato e envio de informações sobre produtos e serviços da Accanto Investimentos, conforme nossa Política de Privacidade.',
        widget=forms.CheckboxInput(attrs={
            'id': 'data_consent',
            'name': 'data_consent',
            'class': 'form-checkbox'
        })
    )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']

class FormWorkWithUs(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'name': 'name', 'placeholder': 'Digite seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'id': 'email', 'name': 'email', 'placeholder': 'Digite seu email'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'id': 'telefone', 'name': 'telefone', 'placeholder': 'Digite seu telefone'}))
    linkedin = forms.URLField(required=False, widget=forms.URLInput(attrs={'type': 'url', 'id': 'linkedin', 'name': 'linkedin', 'placeholder': 'Link do seu LinkedIn'}))
    curriculum_file = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'type': 'file', 'id': 'curriculum', 'name': 'curriculum'}))
    data_consent = forms.BooleanField(
        required=True,
        label='Autorizo o uso dos meus dados pessoais para contato e envio de informações sobre produtos e serviços da Accanto Investimentos, conforme nossa Política de Privacidade.',
        widget=forms.CheckboxInput(attrs={
            'id': 'data_consent',
            'name': 'data_consent',
            'class': 'form-checkbox'
        })
    )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']