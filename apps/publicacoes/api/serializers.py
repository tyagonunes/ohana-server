from rest_framework.serializers import ModelSerializer
from apps.publicacoes.models import *

class SimboloSerializer(ModelSerializer):
    
    class Meta:
        model = Simbolo
        fields = '__all__'

class ProcedimentoMediacaoSerializer(ModelSerializer):
    
    class Meta:
        model = ProcedimentoMediacao
        fields = '__all__'

class BlogSerializer(ModelSerializer):
    
    class Meta:
        model = Blog
        fields = '__all__'