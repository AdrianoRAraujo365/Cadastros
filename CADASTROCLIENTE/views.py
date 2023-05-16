from django.shortcuts import render
from CADASTROCLIENTE.models import Cliente, Profissao, Telefone
# Create your views here.
def index(request):
    meu_nome = "Beltrano da Costa"
    lista_frutas = ['Laranja', 'Maça', 'Banana']
    context = {
        
        'nome': meu_nome,
        'frutas': lista_frutas

    }
    return render(request, 'index.html', context)

def lista_Clientes(request):
    #Busca todos os clientes cadastrados na tabela (admin)
    lista_Clientes = Cliente.objects.all()
    lista_Profissoes = Profissao.objects.all()
    #o dicionario (variavel) context é que vai mandar pro template
    context = {
        "clientes": lista_Clientes,
        "profissoes": lista_Profissoes,
    }


    return render(request, 'lista_Clientes.html', context)

def lista_Profissoes(request):
    lista_Profissoes = Profissao.objects.all()
    context = {
        "profissoes": lista_Profissoes,
    }

    return render(request, 'lista_profissoes.html', context)

def detalhar_cliente(request, id):
    #Buscando no banco de dados o cliente pelo id
    cliente = Cliente.objects.get(id = id)
    telefones = Telefone.objects.filter(cliente_id = id)

    context = {
        "cliente": cliente,
        "telefones": telefones,
    }
    return render(request, "cliente_detalhes.html", context)
    
    


