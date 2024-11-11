from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from apps.publicacoes.models import *
from apps.publicacoes.api.serializers import *


class SimboloFilter(filters.FilterSet):
    class Meta:
        model = Simbolo
        fields = {
            'titulo':['icontains'],
        }

class ProcedimentoMediacaoFilter(filters.FilterSet):
    class Meta:
        model = ProcedimentoMediacao
        fields = {
            'titulo':['icontains'],
        }


class SimboloViewSet(ModelViewSet):
    queryset = Simbolo.objects.all()
    serializer_class = SimboloSerializer
    # filterset_class = SimboloFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']


class ProcedimentoMediacaoViewSet(ModelViewSet):
    queryset = ProcedimentoMediacao.objects.all()
    serializer_class = ProcedimentoMediacaoSerializer
    # filterset_class = ProcedimentoMediacaoFilter
    http_method_names = ['get', 'patch', 'post', 'delete','put']

    ProcedimentoMediacao