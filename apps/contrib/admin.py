from django.contrib import admin
from apps.contrib.mixins import AuditoriaAdmin
from apps.contrib.models import *


@admin.register(Entidade)
class EntidadeAdmin(AuditoriaAdmin):
    search_fields = ('nome', )
    list_filter = ('tipo',)
    list_display = ('nome', 'tipo', 'descricao',)

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'tipo',
                'descricao',
            )
        }),
    )

@admin.register(TipoEntidade)
class TipoEntidadeAdmin(AuditoriaAdmin):
    search_fields = ('titulo', 'descricao' )
    list_filter = ()
    list_display = ('titulo', 'descricao', )

@admin.register(Terapia)
class TerapiaAdmin(AuditoriaAdmin):
    search_fields = ('titulo', 'descricao' )
    list_filter = ()
    list_display = ('titulo', 'descricao', )

@admin.register(Cidade)
class CidadeAdmin(AuditoriaAdmin):
    search_fields = ('nome', )
    list_filter = ('estado',)
    list_display = ('nome', 'estado', )

@admin.register(Ingrediente)
class IngredienteAdmin(AuditoriaAdmin):
    search_fields = ('titulo', )
    list_display = ('titulo', 'descricao', )

@admin.register(Banho)
class BanhoAdmin(AuditoriaAdmin):
    search_fields = ('titulo', )
    list_display = ('titulo', 'descricao', )