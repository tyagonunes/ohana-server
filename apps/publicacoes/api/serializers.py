from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.publicacoes.models import *

class SimboloSerializer(ModelSerializer):
    classes_str = SerializerMethodField()

    def get_classes_str(self, obj):
        return obj.classes.all().values_list('titulo', flat=True)

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

class ClasseSimboloSerializer(ModelSerializer):
    
    class Meta:
        model = ClasseSimbolo
        fields = '__all__'

class CategoriaBlogSerializer(ModelSerializer):
    
    class Meta:
        model = CategoriaBlog
        fields = '__all__'

class AgendaEventosSerializer(ModelSerializer):
    
    class Meta:
        model = AgendaEventos
        fields = '__all__'