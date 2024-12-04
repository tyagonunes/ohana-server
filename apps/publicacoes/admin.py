from django.contrib import admin
from apps.contrib.mixins import AuditoriaAdmin
from apps.publicacoes.models import *


@admin.register(Simbolo)
class SimboloAdmin(AuditoriaAdmin):
    list_filter = ()
    search_fields = ()
    list_display = (
        'titulo',
        'imagem',
    )

@admin.register(ClasseSimbolo)
class ClasseSimboloAdmin(AuditoriaAdmin):
    list_filter = ()
    search_fields = ()
    list_display = (
        'titulo',
    )
    
@admin.register(ProcedimentoMediacao)
class ProcedimentoMediacaoAdmin(AuditoriaAdmin):
    list_filter = ()
    search_fields = ()
    list_display = (
        'titulo',
    )

@admin.register(CategoriaBlog)
class CategoriaBlogAdmin(AuditoriaAdmin):
    list_filter = ()
    search_fields = ()
    list_display = (
        'titulo',
    )

@admin.register(Blog)
class BlogAdmin(AuditoriaAdmin):
    list_filter = ()
    search_fields = ()
    list_display = (
        'titulo',
    )

@admin.register(AgendaEventos)
class BlogAdmin(AuditoriaAdmin):
    list_filter = ()
    search_fields = ()
    list_display = (
        'titulo', 'data'
    )