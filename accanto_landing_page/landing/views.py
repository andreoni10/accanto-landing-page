from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from landing import forms

import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS')

def handle_contact_form(request):
    """
    Processa o formulário de contato e envia email.
    Retorna uma tupla (form, json_response) onde json_response é None se não for AJAX.
    """
    form = forms.FormContact()

    if request.method == 'POST':
        form = forms.FormContact(request.POST)

        if form.is_valid() and form.cleaned_data.get('data_consent') == True:
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
                    print("Email enviado com sucesso!")
                    return form, JsonResponse({'success': True, 'message': 'Mensagem enviada com sucesso!'})
                    
            except Exception as e:
                print(f"Erro ao enviar e-mail: {e}")
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return form, JsonResponse({'success': False, 'errors': form.errors})

    return form, None

def index(request):
    form, json_response = handle_contact_form(request)
    
    if json_response:
        return json_response
        
    return render(request, 'landing/index.html', {'form': form})

def nossos_assessores(request):
    form, json_response = handle_contact_form(request)
    
    if json_response:
        return json_response
        
    return render(request, 'landing/nossa_equipe.html', {'form': form})

def politica_de_privacidade(request):
    return render(request, 'landing/politica_de_privacidade.html')