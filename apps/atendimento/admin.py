from django.contrib import admin
from .models import *

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    extra = 1

class AtendimentoTerapiaInline(admin.StackedInline):
    model = AtendimentoTerapia
    extra = 1

class AtendimentoBanhoInline(admin.StackedInline):
    model = AtendimentoBanho
    extra = 1
@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    search_fields = ()
    list_filter = ('data', 'precisa_retorno', 'status')
    list_display = ('data', 'consulente', 'status')

    inlines = [
        AtendimentoTerapiaInline,
        AtendimentoBanhoInline
    ]

    fieldsets = (
        (None, {
            'fields': (
                'consulente',
                'medium',
                'guia',
                'mediador',
                'data',
                'status',
                'precisa_retorno',
                'recomendacoes',
            )
        }),
    )
