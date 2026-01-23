from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nossa-equipe/', views.nossos_assessores, name='nossa_equipe'),
    path('trabalhe-conosco/', views.trabalhe_conosco, name='trabalhe_conosco'),
    path('politica-de-privacidade/', views.politica_de_privacidade, name='politica_de_privacidade'),
]
