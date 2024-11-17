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
    descricao = models.TextField(verbose_name='Descrição')
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
        verbose_name = 'Mediação'
        verbose_name_plural = 'Mediação'

class CategoriaBlog(BaseModel):
    titulo = models.CharField('Titulo', max_length=255)

    def __str__(self):
        return f'{self.titulo}'
    
    class Meta:
        verbose_name = 'Categoria do blog'
        verbose_name_plural = 'Categorias do blog'
        


class Blog(BaseModel):
    titulo = models.CharField('Título', max_length=255)
    conteudo = HTMLField(verbose_name='Conteúdo')
    banner = models.ImageField('Banner', upload_to='blog', blank=True, null=True)
    categorias = models.ManyToManyField(
        CategoriaBlog,
        verbose_name='Categorias',
        related_name='%(class)s_categorias',
        blank=True,
    )

    def __str__(self):
        return f'{self.titulo}'
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'