from django.contrib import admin
from CADASTROCLIENTE.models import Cliente, Profissao, Telefone , Interesses

# Register your models here.
class Telefones(admin.StackedInline):
    model = Telefone

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cidade']
    list_display_links = ['id', 'nome']
    list_filter = ['bairro', 'cidade', 'ativo']
    search_fields = ["nome"]
    inlines= [Telefones]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Profissao)
admin.site.register(Telefone)
admin.site.register(Interesses)