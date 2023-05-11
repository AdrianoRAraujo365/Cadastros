from django.urls import path
from CADASTROCLIENTE import views


urlpatterns = [

    path("",views.index, name='index'),
    path('clientes', views.lista_Clientes, name= 'clientes'),
    path('Profissao',views.lista_Profissoes, name = 'Profissoes'),
    path('cliente', views.detalhar_cliente, name= 'detalhar'),
    path('cliente/<int:id>', views.detalhar_cliente, name= 'detalhar')
]