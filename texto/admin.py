from django.contrib import admin
from .models import Monografia
# Register your models here.

class TextoAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'autor__nome', 'orientador__nome', 'coorientador__nome', 'resumo', 'palavras_chave', 'data_entrega',]
    
    list_display = ['titulo', 'resumo', 'palavras_chave', 'data_entrega']

    def autor_nome(self, obj):
        return obj.autor.nome if obj.autor else ''
    autor_nome.short_description = 'Autor Nome'

    def orientador_nome(self, obj):
        return obj.orientador.nome if obj.orientador else ''
    orientador_nome.short_description = 'Orientador Nome'
    
    def coorientador_nome(self, obj):
        return obj.coorientador.nome if obj.coorientador else ''
    coorientador_nome.short_description = 'Coorientador Nome' 

admin.site.register(Monografia, TextoAdmin)