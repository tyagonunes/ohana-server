from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from apps.usuarios.forms import UserChangeForm, UserCreationForm
from apps.contrib.mixins import AuditoriaAdmin
from apps.usuarios.models import *
from apps.atendimento.admin import AtendimentoInline

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("Usuário", {"fields": ("papel", "metodo_registro", "foto_rede_social")}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "is_superuser"]



@admin.register(Trabalhador)
class TrabalhadorAdmin(AuditoriaAdmin):
    search_fields = ('nome', 'cpf' )
    list_filter = ()
    list_display = ('nome', 'cpf', 'email', 'telefone',)
    
    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'email',
                'data_nascimento',
                'telefone',
                'cpf',
                'data_ingresso',
                'endereco',
                'usuario',
                'ativo',
            )
        }),
    )

@admin.register(Consulente)
class ConsulenteAdmin(AuditoriaAdmin):
    search_fields = ('nome', )
    list_filter = ()
    list_display = ('nome', 'email', 'telefone', 'telefone_whatsapp')

    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'nome',
                'email',
                'data_nascimento',
                'telefone',
                'telefone_whatsapp',
                'motivo_atendimento',
                'usuario',

            )
        }),
    )

    inlines = [
        AtendimentoInline,
    ]