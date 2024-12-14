from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from apps.publicacoes.models import *
from apps.publicacoes.api.serializers import *


class SimboloFilter(filters.FilterSet):
    class Meta:
        model = Simbolo
        fields = {
            'titulo':['icontains'],
            'classes': ['exact'],
        }

class ProcedimentoMediacaoFilter(filters.FilterSet):
    class Meta:
        model = ProcedimentoMediacao
        fields = {
            'titulo':['icontains'],
        }

class BlogFilter(filters.FilterSet):
    class Meta:
        model = Blog
        fields = {
            'titulo':['icontains'],
            'categorias':['exact']
        }



class SimboloViewSet(ModelViewSet):
    queryset = Simbolo.objects.all()
    serializer_class = SimboloSerializer
    filterset_class = SimboloFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.query_params.get('termo')
        if termo:
            qs = qs.filter(Q(titulo__icontains=termo) | Q(palavras_chave__icontains=termo))

        return qs



class ProcedimentoMediacaoViewSet(ModelViewSet):
    queryset = ProcedimentoMediacao.objects.all()
    serializer_class = ProcedimentoMediacaoSerializer
    filterset_class = ProcedimentoMediacaoFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_class = BlogFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']


class ClasseSimboloViewSet(ModelViewSet):
    queryset = ClasseSimbolo.objects.all()
    serializer_class = ClasseSimboloSerializer
    # filterset_class = BlogFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']

class CategoriaBlogViewSet(ModelViewSet):
    queryset = CategoriaBlog.objects.all()
    serializer_class = CategoriaBlogSerializer
    # filterset_class = BlogFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']


class AgendaEventosViewSet(ModelViewSet):
    queryset = AgendaEventos.objects.all()
    serializer_class = AgendaEventosSerializer
    # filterset_class = ProcedimentoMediacaoFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']


class AgendaEventosCalendarioViewSet(GenericViewSet):

    def list(self, request):
        self.queryset = AgendaEventos.objects.all().values('titulo', 'descricao', 'tipo_evento', 'data', 'hora')
        return Response({'results': self.queryset}, status=status.HTTP_200_OK)