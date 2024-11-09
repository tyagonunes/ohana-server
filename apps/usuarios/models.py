from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings 
from apps.usuarios.choices import (
    CHOICES_USER_PAPEL, 
    USER_PAPEL_COMUM,
    CHOICES_METODO_REGISTRO,
    METODO_REGISTRO_EMAIL
)

from apps.contrib.mixins import BaseModel

class User(AbstractUser):
    papel = models.IntegerField('Papel', choices=CHOICES_USER_PAPEL, default=USER_PAPEL_COMUM)
    email = models.CharField(max_length=250, unique=True, null=False, blank=False)
    metodo_registro = models.IntegerField(choices=CHOICES_METODO_REGISTRO, default=METODO_REGISTRO_EMAIL)
    foto_rede_social = models.URLField('Foto rede social', blank=True, null=True)

    def __str__(self):
       return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    from datetime import datetime, timedelta

    data_expiracao = datetime.now() + timedelta(hours=1)

    dados = {
        'nome': reset_password_token.user.first_name,
        'token': reset_password_token.key,
        'data_expiracao': data_expiracao.strftime('%d/%m/%Y às %H:%M'),
    }

    subject = "Codigo para recuperação de senha"
    message = f'{dados["nome"]} o seu codigo para recuperação de senha é {dados["token"]}. Esse codigo expira em {dados["data_expiracao"]}'
    recipient_list = [reset_password_token.user.email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)


class Trabalhador(BaseModel):
    cols = {
        'nome': 4,
        'email': 4,
        'data_nascimento': 4,
        'cpf': 4,
        'endereco': 4,
        'cidade': 4,
        'telefone': 4,
        'ativo': 1,
    }
    nome = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    data_nascimento = models.DateField('Data de nascimento')
    data_ingresso = models.DateField('Data de ingresso no corpo mediunico', null=True, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=255, null=True, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', null=True, blank=True)
   
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Trabalhador'
        verbose_name_plural = 'Trabalhadores'

class Consulente(BaseModel):
    cols = {
        'nome': 6,
        'data_nascimento': 4,
        'email': 6,
        'telefone': 4,
        'telefone_whatsapp': 4,
        'possui_marcapasso': 12,
        'doencas_preexistentes': 12,
        'descricao_doencas_preexistentes': 12,
        'descricao_medicacao': 12,
        'motivo_atendimento': 12
    }
    
    nome = models.CharField('Nome', max_length=255)
    data_nascimento = models.DateField('Data de nascimento')
    email = models.EmailField('Email', unique=True, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    telefone_whatsapp = models.BooleanField('Telefone é Whatsapp', default=False)
    descricao_medicacao = models.TextField('Quais?', blank=True, null=True)
    motivo_atendimento = models.TextField('Motivo da procura pelo atendimento (o que procura obter?)', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Consulente'
        verbose_name_plural = 'Consulentes'
