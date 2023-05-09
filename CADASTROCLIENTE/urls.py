from django.urls import path
from CADASTROCLIENTE import views


urlpatterns = [

    path("",views.index, name='index'),
]