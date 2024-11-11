from rest_framework.routers import DefaultRouter
from apps.publicacoes.api.viewsets import *


router = DefaultRouter()
router.register(r'simbolos', SimboloViewSet, basename='simbolos')
router.register(r'procedimento-mediacao', ProcedimentoMediacaoViewSet, basename='procedimento_mediacao')

urlpatterns = router.urls