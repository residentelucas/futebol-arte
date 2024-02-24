from django.contrib import admin
from .models import Clube, Jogador, Competicao, Titulo, Pais, Estado, Cidade
from django.utils.html import format_html

# Register your models here.

class JagadorInline(admin.TabularInline):
    model = Jogador
    extra = 1

class TituloInline(admin.TabularInline):
    model = Titulo
    extra = 1

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ('id', 'escudo','nome', 'ano_fundacao', 'divisao_atual', 'genero', 'pais', 'estado','cidade', 'delete' )

    def escudo(self, obj):
        width, height = 50, 50
        html = '<img src="/{url}" width="{width}" height={height} />'
        return format_html(
            html.format(url=obj.cover.url, width=width, height=height)
        )
    inlines = (JagadorInline, TituloInline,)



#@admin.register(Jogador)
#class JogadorAdmin(admin.ModelAdmin):
    #list_display = ('id', 'nome', 'foto', 'posicao_principal', 'numero_camisa', 'sexo', 'pais', 'estado', 'cidade', 'clube')
    #list_filter = ['clube']



@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo_disputa', 'categoria')



#@admin.register(Titulo)
#class TituloAdmin(admin.ModelAdmin):
    #list_display = ('id', 'resultado', 'ano_conquista', 'data_exata', 'clube', 'competicao')




@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'continente')

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'regiao')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'populacao')
