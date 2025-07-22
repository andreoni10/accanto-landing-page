from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from landing import forms

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS')

# Create your views here.
def index(request):
    form = forms.FormContact()

    if request.method == 'POST':
        form = forms.FormContact(request.POST)

        if form.is_valid():
            print('VALIDATION SUCESS!')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            text = form.cleaned_data['text']
            
            # Corpo do e-mail
            corpo_email = (
                f"Nome: {name}\n"
                f"Email: {email}\n"
                f"Telefone: {telephone}\n\n"
                f"Mensagem:\n{text}"
            )
            
            try:
                send_mail(
                    f"Formulário: {name}",
                    corpo_email,
                    settings.DEFAULT_FROM_EMAIL,
                    [EMAIL_RECIPIENTS],
                    fail_silently=False,
                )

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Mensagem enviada com sucesso!'})
                    
            except Exception as e:
                print(f"Erro ao enviar e-mail: {e}")
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'landing/index.html', {'form' : form})
