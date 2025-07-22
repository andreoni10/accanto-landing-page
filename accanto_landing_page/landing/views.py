from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from landing import forms

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
            print('NAME: ' + name)
            print('EMAIL: ' + email)
            print('TELEPHONE: ' + telephone)
            print('TEXT: ' + text)
            
            # Corpo do e-mail que você receberá
            corpo_email = (
                f"Nome: {name}\n"
                f"Email: {email}\n"
                f"Telefone: {telephone}\n\n"
                f"Mensagem:\n{text}"
            )
            
            try:
                # Envia o e-mail
                send_mail(
                    f"Formulário: {name}",  # Assunto do e-mail que você receberá
                    corpo_email,                              # Corpo da mensagem
                    settings.DEFAULT_FROM_EMAIL,              # Remetente (definido em settings.py)
                    ['lucasandreoni1007@gmail.com'],          # Lista de destinatários (seu e-mail Outlook)
                    fail_silently=False,                      # Para ver exceções se houver problemas
                )

                # Se for uma requisição AJAX, retorna JSON
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Mensagem enviada com sucesso!'})
                    
            except Exception as e:
                 # Aqui você pode logar o erro ou exibir uma mensagem de erro
                print(f"Erro ao enviar e-mail: {e}")
                # Se houver erros no formulário e for AJAX
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'errors': form.errors})

            # Se for uma requisição AJAX, retorna JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Mensagem enviada com sucesso!'})
            else:
                # Se houver erros no formulário e for AJAX
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'landing/index.html', {'form' : form})
