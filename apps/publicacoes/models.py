from django.db import models
from apps.contrib.mixins import BaseModel
from tinymce.models import HTMLField

class ClasseSimbolo(BaseModel):
    titulo = models.CharField('Titulo', max_length=255)

    def __str__(self):
        return f'{self.titulo}'
    
    class Meta:
        verbose_name = 'Classe de símbolo'
        verbose_name_plural = 'Classes de símbolos'
        

class Simbolo(BaseModel):
    titulo = models.CharField('Título', max_length=255)
    descricao = HTMLField(verbose_name='Descrição')
    imagem = models.ImageField('Imagem', upload_to='simbolo', blank=True, null=True)
    palavras_chave = models.CharField('Palavras-chave', max_length=255)
    classes = models.ManyToManyField(
        ClasseSimbolo,
        verbose_name='Classes',
        related_name='%(class)s_classes',
        blank=True,
    )

    def __str__(self):
        return f'{self.titulo}'
    
    class Meta:
        verbose_name = 'Símbolo'
        verbose_name_plural = 'Símbolos'


class ProcedimentoMediacao(BaseModel):
    titulo = models.CharField('Título', max_length=255)
    descricao = HTMLField(verbose_name='Descrição')

    def __str__(self):
        return f'{self.titulo}'
    
    class Meta:
        verbose_name = 'Procedimento de mediação'
        verbose_name_plural = 'Procedimentos de mediação'